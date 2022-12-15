import logging
from settings import API_LOG_PATH, MAIN_LOG_PATH

# Setting the logging level
logging.basicConfig(level=logging.INFO)

# Setting the logging format
formatter = logging.Formatter('%(asctime)s %(funcName)s() [%(levelname)s]:%(message)s')

# Creating 2 loggers for api and main requests
logger_api = logging.getLogger("api")
logger_main = logging.getLogger("main")

# Creating log handlers and setting formatters for them
# file_handler_api = logging.FileHandler(API_LOG_PATH, mode='w')
# file_handler_api.setFormatter(formatter)
# file_handler_main = logging.FileHandler(MAIN_LOG_PATH, mode='w')
# file_handler_main.setFormatter(formatter)

# Adding created handlers for loggers
# logger_api.addHandler(file_handler_api)
# logger_main.addHandler(file_handler_main)
