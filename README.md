# Log-monitoring

A script that automates the analysis and monitoring of log files

Prerequisites

1. Python version 3 (3.12.3)
2. A log file which has log entries. (Eg: logfile.txt, an example used to test the script is present in the repo)

Usage

1. Clone the repo.
2. Check for the Python version.
4. Run the script from the directory containing the script using the command: python log-monitoring.py
5. A text says the script has started and the script is in play.
6. Run the script logger.py using the command: python logger.py (which creates a log file and use Ctrl+C to stop logging.)
8. On stopping the log-monitoring script, a logfile is created and the log-monitoring script reflects a summary report on terminal and generates a report.txt.
9. To close the monitoring Ctrl+C can be used and this would give a sumarry report including count error messages, HTTP status codes.
