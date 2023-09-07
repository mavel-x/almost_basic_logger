import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def configure_logger(
        app_logger_name: str, /,
        level=logging.INFO,
        log_dir=Path('logs'),
        fmt="%(asctime)s %(name)s %(levelname)s: %(message)s",
        max_file_size_mb=1,
        backup_count=5,
):
    assert app_logger_name, 'A logger name must be specified.'
    log_dir.mkdir(parents=True, exist_ok=True)
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    app_logger = logging.getLogger(app_logger_name)
    app_logger.setLevel(level)
    formatter = logging.Formatter(
        fmt=fmt,
    )
    file_handler = RotatingFileHandler(
        filename=log_dir / f"{app_logger.name}.log",
        maxBytes=1024 * 1024 * max_file_size_mb,
        backupCount=backup_count,
    )
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    root_logger.addHandler(stream_handler)
    app_logger.addHandler(file_handler)
