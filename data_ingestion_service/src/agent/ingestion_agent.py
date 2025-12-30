
import json

from src.utils import log, ProjectException

from src.agent.tools import expand_slang, detect_language_translate, clean_and_anonymize_text, generate_timestamp, generate_id
from src.agent.clients.client import loaded_model_with_tools
from src.agent.prompts.prompt import data_ingestion_prompt

from langchain_core.messages import AIMessage, ToolMessage


tools_dict = {
    "expand_slang": expand_slang, 
    "detect_language_translate": detect_language_translate,
    "clean_and_anonymize_text": clean_and_anonymize_text,
    "generate_timestamp": generate_timestamp,
    "generate_id": generate_id,
    # todo - Add any other tools mentioned in the prompt
}


def ingest_logs(log_data):
    """ Data ingestion agent that read, clean and stucture log data for sentiment analysis """

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






