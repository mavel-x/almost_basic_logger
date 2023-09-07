# almost_basic_logger
The logger config that I'm tired of copypasting.
Utilizes Python's built-in logging library and provides both file and console logging.
Only the logs produced explicitly by your app go into the file. 

## Installation

You can install this package directly from GitHub using pip:
```bash
pip install git+https://github.com/mavel-x/almost_basic_logger.git#egg=almost_basic_logger
```

Or put it in your `requirements.txt` with a version tag:
```
git+https://github.com/mavel-x/almost_basic_logger.git@v0.1#egg=almost_basic_logger
                                        # version tag ^
```

## Usage

In your modules other than main:
```python
import logging


logger = logging.getLogger('your_app.other_module')


def some_other_func():
    # do something else
    logger.info('Log something else to console and file.')
```

In your main module:
```python
import logging

import third_party_lib 
from almost_basic_logger import configure_logger

from your_other_module import some_other_func


logger = logging.getLogger('your_app.main')


def some_func():
    # do something
    logger.info('Log something to console and file.')

    
def main():
    # Configure logging
    configure_logger('your_app')

    # Your application code
    some_func()
    some_other_func()
    # Make a third-party API call that logs a warning
    third_party_lib.do_something()
```
Console Output:
```
2023-08-30 12:34:56,789 your_app.main INFO: Log something to console and file.
2023-08-30 12:34:56,790 your_app.other_module INFO: Log something else to console and file.
2023-08-30 12:34:56,791 third_party_lib WARNING: This is a warning message from third_party_lib.
```
File Output:
```
2023-08-30 12:34:56,789 your_app.main INFO: Log something to console and file.
2023-08-30 12:34:56,790 your_app.other_module INFO: Log something else to console and file.
```



## Parameters

The `configure_logger` function accepts the following parameters:

- `app_logger_name` (`str`, positional-only): The name of the logger you want to configure. This is a required argument.
- `level` (`int`): The logging level. Defaults to `logging.INFO`.
- `log_dir` (`Path`): The directory where log files will be stored. Defaults to a folder named `logs` in the current directory.
- `fmt` (`str`): The logging format string. 
Defaults to `"%(asctime)s %(name)s %(levelname)s: %(message)s"`
- `max_file_size_mb` (`int` or `float`): Maximum log file size in MB before it rolls over. Defaults to `1 MB`.
- `backup_count` (`int`): The number of backup files to keep. Defaults to `5`.



### Example with Custom Parameters

You can also specify custom parameters like so:

```python

from almost_basic_logger import configure_logger

configure_logger(
    'your_application',
    level=logging.DEBUG,
    log_dir=Path('/custom/log/dir'),
    fmt="%(asctime)s %(name)s %(levelname)s: %(message)s",
    max_file_size_mb=5,
    backup_count=10
)
```
