import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("6378816084:AAF5kKmEjxLI5DkA_ZVjmMu97NpPjco-RTI", "")
    
    API_ID = int(os.environ.get("22847778", ""))
    
    API_HASH = os.environ.get("355c5bea2732922d393047c4c04b0487", "")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("mongodb+srv://ksrmobile123:ksrmobile123@cluster0.f7tuhes.mongodb.net/?retryWrites=true&w=majority", "")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("-1002018357931", ""))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("-1002038299137", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5452549957"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("ksr_uploader_v2bot", "")
                                  
