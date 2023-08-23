from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "2b445de78e5baf012a0793e60bd4fbf5"]
        API_ID = [int, 19099900]
        BOT_TOKEN = [str, "6146904519:AAFtE6fUIDoM9xOKZqmrbs2gA5-2FGdDGh0"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, True]
        AUTH_USERS = [list,[778393824 6265459491 6198858059]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"JujutsuBotUpdates"]
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
