
import re
from langchain.tools import tool
from src.utils import log, ProjectException


from src.constants.constant import SLANG_DICT



import re

@tool
def expand_slang(text):
    """ Handle slag and abbreviation, when received a such a text convert it to expand_slang/meaning and return it """

    try:
        # Split text into words, preserving punctuation
        words = re.findall(r'\w+|[^\w\s]', text)
        expanded = []
        for word in words:
            # Check if word (case-insensitive) is in dict
            key = word.lower()
            if key in SLANG_DICT:
                expanded.append(SLANG_DICT[key])
            else:
                expanded.append(word)
        # log.info("Expanded Slang Words: {}".format(expanded))
        log.info("Expanded Slang Words")
        return ''.join(expanded)
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "expand_slang",
                "message": "Expanding Slang Word Error",
            }
        )

