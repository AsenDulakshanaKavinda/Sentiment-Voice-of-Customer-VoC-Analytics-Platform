
import re
from langchain.tools import tool
from data_ingestion_service.utils.exception_config import ProjectException
from data_ingestion_service.utils.logger_config import log



# Sample slang/abbreviation dictionary (extend as needed)
SLANG_DICT = {
    'a3': 'Anytime, Anywhere, Anyplace',
    'adih': 'Another Day In Hell',
    'afk': 'Away From Keyboard',
    'afaik': 'As Far As I Know',
    'asap': 'As Soon As Possible',
    'asl': 'Age, Sex, Location',
    'atk': 'At The Keyboard',
    'atm': 'At The Moment',
    'bae': 'Before Anyone Else',
    'bak': 'Back At Keyboard',
    'bbl': 'Be Back Later',
    'bbs': 'Be Back Soon',
    'bfn': 'Bye For Now',
    'b4n': 'Bye For Now',
    'brb': 'Be Right Back',
    'bruh': 'Bro',
    'brt': 'Be Right There',
    'bsaaw': 'Big Smile And A Wink',
    'btw': 'By The Way',
    'bwl': 'Bursting With Laughter',
    'csl': "Can’t Stop Laughing",
    'cu': 'See You',
    'cul8r': 'See You Later',
    'cya': 'See You',
    'dm': 'Direct Message',
    'faq': 'Frequently Asked Questions',
    'fc': 'Fingers Crossed',
    'fimh': 'Forever In My Heart',
    'fomo': 'Fear Of Missing Out',
    'fr': 'For Real',
    'fwiw': "For What It's Worth",
    'fyp': 'For You Page',
    'fyi': 'For Your Information',
    'g9': 'Genius',
    'gal': 'Get A Life',
    'gg': 'Good Game',
    'gmta': 'Great Minds Think Alike',
    'gn': 'Good Night',
    'goat': 'Greatest Of All Time',
    'gr8': 'Great!',
    'hbd': 'Happy Birthday',
    'ic': 'I See',
    'icq': 'I Seek You',
    'idc': "I Don’t Care",
    'idk': "I Don't Know",
    'ifyp': 'I Feel Your Pain',
    'ilu': 'I Love You',
    'ily': 'I Love You',
    'imho': 'In My Honest/Humble Opinion',
    'imu': 'I Miss You',
    'imo': 'In My Opinion',
    'iow': 'In Other Words',
    'irl': 'In Real Life',
    'iykyk': 'If You Know, You Know',
    'jk': 'Just Kidding',
    'kiss': 'Keep It Simple, Stupid',
    'l': 'Loss',
    'l8r': 'Later',
    'ldr': 'Long Distance Relationship',
    'lmk': 'Let Me Know',
    'lmao': 'Laughing My A** Off',
    'lol': 'Laughing Out Loud',
    'ltns': 'Long Time No See',
    'm8': 'Mate',
    'mfw': 'My Face When',
    'mid': 'Mediocre',
    'mrw': 'My Reaction When',
    'mte': 'My Thoughts Exactly',
    'nvm': 'Never Mind',
    'nrn': 'No Reply Necessary',
    'npc': 'Non-Player Character',
    'oic': 'Oh I See',
    'op': 'Overpowered',
    'pita': 'Pain In The A**',
    'pov': 'Point Of View',
    'prt': 'Party',
    'prw': 'Parents Are Watching',
    'rofl': 'Rolling On The Floor Laughing',
    'roflol': 'Rolling On The Floor Laughing Out Loud',
    'rotflmao': 'Rolling On The Floor Laughing My A** Off',
    'rn': 'Right Now',
    'sk8': 'Skate',
    'stats': 'Your Sex And Age',
    'sus': 'Suspicious',
    'tbh': 'To Be Honest',
    'tfw': 'That Feeling When',
    'thx': 'Thank You',
    'time': 'Tears In My Eyes',
    'tldr': "Too Long, Didn’t Read",
    'tntl': 'Trying Not To Laugh',
    'ttfn': 'Ta-Ta For Now!',
    'ttyl': 'Talk To You Later',
    'u': 'You',
    'u2': 'You Too',
    'u4e': 'Yours For Ever',
    'w': 'Win',
    'w8': 'Wait...',
    'wb': 'Welcome Back',
    'wtf': 'What The F**k',
    'wtg': 'Way To Go!',
    'wuf': 'Where Are You From?',
    'wyd': 'What You Doing?',
    'wywh': 'Wish You Were Here',
    'zzz': 'Sleeping, Bored, Tired'
    # todo - Add more as needed, e.g., from online lists
}

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
        log.info("Expanded Slang Words: {}".format(expanded))
        return ''.join(expanded)
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "expand_slang",
                "message": "Expanding Slang Word Error",
            }
        )

