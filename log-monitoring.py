import time
import signal
import re
import sys
from collections import Counter

# Function to handle Ctrl+C
def signal_handler(sig, frame):
    print("\nLog monitoring stopped.")
    if log_analysis_enabled:
        analyze_log(log_file)
    sys.exit(0)

# Configure log file path
log_file = "logfile.txt"

# Function to monitor log file
def monitor_log(log_file):
    with open(log_file, "r") as file:
        file.seek(0, 2)  # Move file pointer to the end
        while True:
            line = file.readline()
            if line:
                yield line
            else:
                time.sleep(0.1)

# Function to perform log analysis
def analyze_log(log_file):
    keywords = ["ERROR", "WARNING", "CRITICAL"]  # Add more keywords as needed
    http_status_regex = r'\b\d{3}\b'  # Regular expression to match HTTP status codes
    status_code_count = Counter()

    with open(log_file, "r") as file:
        for line in file:
            # Count occurrences of HTTP status codes
            status_codes = re.findall(http_status_regex, line)
            for code in status_codes:
                status_code_count[code] += 1

            # Count occurrences of other keywords
            for keyword in keywords:
                if re.search(keyword, line):
                    status_code_count[keyword] += 1

    # Print summary report
    print("\nLog Analysis Summary:")
    for item, count in status_code_count.items():
        print(f"{item}: {count}")

# Main function
def main():
    global log_analysis_enabled
    log_analysis_enabled = False

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Start log monitoring loop
    print("Log monitoring started...")
    try:
        for line in monitor_log(log_file):
            print(line.strip())  # Display log line
            log_analysis_enabled = True  # Enable log analysis
    except FileNotFoundError:
        print("Log file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
