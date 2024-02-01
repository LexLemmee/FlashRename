from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://sturdex:123@cluster0.cusrjyp.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "10e3ed833b0d09699973420d45359409"]
        API_ID = [int, 4665778]
        BOT_TOKEN = [str, "6067088569:AAFuJk7fdGfDceeqSHNf964d30hKiwNstoI"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[5531584953]]
        OWNER_ID = [int, 5531584953]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/AnimeMoviesEclipse"]
        FORCEJOIN_ID = [int,-1001926672967]

        TRACE_CHANNEL = [int, -1001940866862]

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
