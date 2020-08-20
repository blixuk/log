# log

A simple Python script for logging stdin to a file.

Pipe into log to save any output from a command to a log file.
If no name or path is given the log will be written to the current directory with the current date and time as the file name. A log name or a specific path and be provided and the log file will be written with that information. if the verbose argument is used the file location will be printed to the terminal.

```
usage: log [-h] [-n NAME] [-p PATH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  output file name
  -p PATH, --path PATH  output file path
  -v, --verbose         return output file path
```

### Planned features
- File / Directory checking before writing