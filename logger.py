import logging
import time
import random

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "HTTP {status} - {method} {url}",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

status_codes = [200, 404, 500]
methods = ["GET", "POST"]

# Open the log file in append mode
with open("logfile.txt", "a") as file:
    try:
        # Main loop to log messages
        while True:
            # Randomly select a log level
            log_level = random.choice(log_levels)
            if log_level == logging.INFO:
                status = random.choice(status_codes)
                method = random.choice(methods)
                url = "https://www.google.com/" if method == "GET" else "https://www.google.com/"
                log_message = formats[log_level].format(status=status, method=method, url=url)
            else:
                log_message = formats[log_level]
            # Get the log message format for the selected log level
            # Log the message
            logger.log(log_level, log_message)
            # Write the log message to the file
            file.write(f"{log_level}: {log_message}\n")
            # Sleep for a short interval
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nLogging interrupted. Exiting.")
