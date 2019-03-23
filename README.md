# richest


[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/mkfeuhrer/richest/master/LICENSE)
[![PyPI Downloads](https://img.shields.io/pypi/dm/richest.svg)](https://pypi.org/project/richest/)
[![PyPI](https://img.shields.io/pypi/v/richest.svg)](https://pypi.org/project/richest/)

A Python package to extract World's Richest People (Based on Forbes Rankings)

### Dependencies

+ requests

## Installation Instruction

- Chef-CLI is available as a python package.

- Open terminal and run ```pip install richest```

- This installs the CLI app.

- Now run richest --help to know the available commands

- Enjoy !!

### Example

**To extract Top 20 Richest People**

```
richest --current
```

**To extract Top 20 Youngest Richest People**

```
richest --youngest
```

**Complete option list**

```
richest -h
usage: richest [-h] [--current] [--youngest] [--oldest] [--male] [--female]

optional arguments:
  -h, --help  show this help message and exit
  --current   Get richest people currently
  --youngest  Get youngest richest people
  --oldest    Get oldest richest people
  --male      Get richest males
  --female    Get richest females
```

## Feedback

Feel free to send feedback on [Email](mailto:mohitfeuhrer@gmail.com) or [file an issue](https://github.com/mkfeuhrer/richest/issues).

## Contributors

- [Mohit Khare](https://github.com/mkfeuhrer)

## Contribute

- Feel free to report issues and bugs.It will be helpful for future launches of application.
- All Suggestions are welcome.
- Fork repository and Contribute.


## Acknowledgment

Thanks to awesome api - https://forbes400.herokuapp.com/
