import logging
import os
from datetime import datetime

# Define the directory where log files will be stored
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it does not already exist
os.makedirs(logs_dir, exist_ok=True)

# Generate a log file name with the current timestamp for uniqueness
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(logs_dir, log_file)

# Configure the logging module to write logs to the file
# - filename: path to the log file
# - format: log message format with timestamp, log level, and message
# - level: minimum log level to capture (INFO and above)
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example usage: log a message when the script is run directly
if __name__ == "__main__":
    logging.info("Logging has started")