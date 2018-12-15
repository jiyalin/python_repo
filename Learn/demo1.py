import logging
import io

for i in range(10):
    logging.basicConfig(filename='test.log', level=logging.DEBUG)
    logging.warning("this is warning msg")
    logging.info("this is info msg")
    logging.debug("this is debug msg")