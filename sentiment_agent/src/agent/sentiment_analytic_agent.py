import json

from src.utils import log, ProjectException
from src.agent.clients.client import sentiment_model
from src.agent.prompts.prompt import sentiment_analysis_prompt_v1



def sentiment_analytic(customer_feedback):
    try:
        if isinstance(customer_feedback, dict):
            customer_feedback_str = json.dumps(customer_feedback, indent=2)
        else:
            customer_feedback_str = str(customer_feedback)


        # create a simple LCEL chain for sentiment analytic
        chain = sentiment_analysis_prompt_v1 | sentiment_model
        log.info("Sentiment Analytics Agent Chain ready.")

        # payload
        customer_feedback = {"customer_feedback": customer_feedback_str}

        # Get the initial messages from the prompt
        messages = sentiment_analysis_prompt_v1.invoke(customer_feedback).messages
        log.info("Invoking sentient analytic chain")

        # invoke the model with initial messages
        result = sentiment_model.invoke(messages)

        log.info("Sentiment Analytics Agent Result ready: .")

        return result

    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "Sentiment Analytics Agent",
                "message": "sentiment_analytic_agent failed",
            }
        )

