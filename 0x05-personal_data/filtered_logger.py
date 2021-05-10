#!/usr/bin/env python3
"""
The function should use a regex to replace occurrences of certain field values
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """__init___"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Format Function
        """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    function called filter_datum that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(
            r"{}=.+?{}".format(field, separator),
            "{}={}{}".format(field, redaction, separator),
            message,
        )
    return message
