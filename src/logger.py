import logging
import os


from datetime import datetime

LOG_FILE =f"{os.getcwd()}/logs/{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd() , "logs" , LOG_FILE)

os.makedirs(os.path.dirname(logs_path) , exist_ok=True)

LOG_FILE_PATH  = os.path.join(os.getcwd() , "logs" , LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH , 
    level=logging.INFO
    , format="%(asctime)s:%(levelname)s:%(message)s"
    )


if __name__  == "__main__":
    logging.info("This is a test log message")


    