import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app_log.log',
    filemode='w',
    format='%(asctime)s [%(levelname)s]: in %(filename)s (line %(lineno)s), %(message)s'
)
