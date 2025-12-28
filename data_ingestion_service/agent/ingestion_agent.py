
import json

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException
from data_ingestion_service.agent.prompts.prompt import data_ingestion_prompt
from data_ingestion_service.agent.clients.client import loaded_model_with_tools
from langchain_core.messages import AIMessage, ToolMessage

from data_ingestion_service.agent.tools.handle_slang import expand_slang
from data_ingestion_service.agent.tools.language_detector import detect_language_translate
from data_ingestion_service.agent.tools.clean_and_anonymize import clean_and_anonymize_text
from data_ingestion_service.agent.tools.generate_timestamp import generate_timestamp
from data_ingestion_service.agent.tools.generate_id import generate_id

# Assuming you have a dictionary mapping tool names to their callable functions
# Replace with your actual tools, e.g., from langchain.tools import expand_slang, detect_language_translate, clean_and_anonymize_text
tools_dict = {
    "expand_slang": expand_slang,  # Import and add your tools here
    "detect_language_translate": detect_language_translate,
    "clean_and_anonymize_text": clean_and_anonymize_text,
    "generate_timestamp": generate_timestamp,
    "generate_id": generate_id
    # Add any other tools mentioned in the prompt
}


def ingest_logs(log_data):
    """  """

    try:

        # Handle log_data as dict by converting to JSON string for prompt formatting
        if isinstance(log_data, dict):
            log_data_str = json.dumps(log_data, indent=2)
        else:
            log_data_str = str(log_data)  # Fallback for non-dict

        # create a simple LCEL chain
        chain = data_ingestion_prompt | loaded_model_with_tools
        log.info("ingesting logs chain created")

        # Prepare initial input for the prompt
        initial_input = {"log_data": log_data_str}

        # Get the initial messages from the prompt
        messages = data_ingestion_prompt.invoke(initial_input).messages
        log.info("Invoking data ingestion chain")

        # Invoke the model with initial messages
        result = loaded_model_with_tools.invoke(messages)

        # Handle tool calls in a loop if the model supports and returns them
        while isinstance(result, AIMessage) and result.tool_calls:
            messages.append(result)  # Add the AI's response (with tool calls)

            for tool_call in result.tool_calls:
                # Execute the tool: Map tool names to actual functions
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                tool_id = tool_call["id"]

                if tool_name in tools_dict:
                    tool_result = tools_dict[tool_name].invoke(tool_args)
                    log.info(f"use tool: {tool_name}")
                else:
                    tool_result = "Tool not found."

                # Append the tool result as a ToolMessage
                messages.append(ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_id
                ))

            # Re-invoke the model (not the full chain) with updated messages
            result = loaded_model_with_tools.invoke(messages)

        log.info(f'result: {result.content}')
        log.info("Invoking data ingestion complete...")

        return result

    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "ingest_logs",
                "message": "ingesting logs failed",
            }
        )






