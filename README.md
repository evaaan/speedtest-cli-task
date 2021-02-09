# Speedtest Script

Run speedtest-cli and log to csv.
## Install
```
> pip install -r requirements.txt
```

## Usage
```
> python main.py -h

usage: main.py [-h] csv_file log_file

Run SpeedTest and log to CSV

positional arguments:
  csv_file    CSV filename
  log_file    logging filename

optional arguments:
  -h, --help  show this help message and exit
```

## Example

```
> python main.py results.csv log.txt
```

# Test
```
> python -m unittest test_main.py
```