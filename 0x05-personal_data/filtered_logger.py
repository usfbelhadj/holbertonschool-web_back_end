#!/usr/bin/env python3
import re

"""
filtered_logger
"""


def filter_datum(fields, redaction, message, separator):
    '''
    function called filter_datum that returns the log message obfuscated
    '''
    for field in fields:
        message = re.sub(r'{}=.+?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message
