"""main.py"""

import argparse
import csv
import logging
import speedtest
from pathlib import Path


HEADERS = ['timestamp', 'download', 'upload', 'ping', 'bytes_sent', 'bytes_received']

def run_speedtest():
    """Run the speedtest and return the results."""
    s = speedtest.Speedtest()
    s.download()
    s.upload()
    return s.results.dict()
    

def create_csv(csvfile):
    """Create a new CSV file. Warn if it already exists.
    
    Args:
        csvfile (pathlib.Path): Path to csv file.
    """
    if csvfile.exists():
        logging.warning("CSV file '{}' already exists! Overwriting... ".format(csvfile))
    logging.info("Creating new csv file: {}".format(csvfile))
    with open(csvfile, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(HEADERS)


def entrypoint(csvfile):
    """entry point. Call this if run programmatically.
    
    Args:
        csvfile (pathlib.Path): Path to csv file. Create a file if it does not exist.
    """    
    # Create the CSV file with header if does not exist
    if not csvfile.exists():
        create_csv(csvfile)
    
    # Generate CSV row with results
    logging.info("Running speedtest..")
    results_dict = run_speedtest()
    try:
        row = [results_dict[result] for result in HEADERS]
    except KeyError as e:
        logging.error("Speedtest result {} not found! Exiting.".format(e))
        return 
            
    # Write CSV
    with open(csvfile, 'a', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(row)

    logging.info("Speedtest run captured")
    

def main():
    """ main function """
    parser = argparse.ArgumentParser(description='Run SpeedTest and log to CSV')
    parser.add_argument('csv_file', type=str, help='CSV filename')
    parser.add_argument('log_file', type=str, help='logging filename')
    args = parser.parse_args()

    # Configure logger

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s: %(message)s',
                        handlers=[logging.FileHandler(args.log_file), logging.StreamHandler()])
    try:
        entrypoint(Path(args.csv_file))
    except Exception as e:
        logging.error("Encountered exception! {}".format(e))


if __name__ == "__main__":
    main()
