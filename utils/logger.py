import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter(
    "[%(asctime)s - %(filename)s:%(lineno)d][%(levelname)s] %(message)s"
)

# Create a stream handler and set the formatter
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Add the stream handler to the logger
logger.addHandler(stream_handler)