import logging
import os

logging.basicConfig(
    filename='log_files.log',
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="w"
    )
