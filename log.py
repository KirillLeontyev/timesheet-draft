import logging

logging.basicConfig(
    level=logging.WARNING,
    filename='app_log.log',
    filemode='w',
    format='%(asctime)s [%(levelname)s]: in %(filename)s (line %(lineno)s), %(message)s'
)
