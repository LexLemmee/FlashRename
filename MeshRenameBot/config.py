from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "postgres://iubxmjfs:XtftA36D6kajzosJinXlepPr40xId6Df@trumpet.db.elephantsql.com/iubxmjfs"]
        API_HASH = [str, "2b445de78e5baf012a0793e60bd4fbf5"]
        API_ID = [int, 19099900]
        BOT_TOKEN = [str, "6295293651:AAEMIVNFEgMwiuzPEoWLRU9arF9kbPzOrA0"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[778393824, 6295293651, 6198858059, 6368899212]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/+Q6vE1zw5qANhYWVl"]
        FORCEJOIN_ID = [int,-1001596651023]

        TRACE_CHANNEL = [int, -1001596651023]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
