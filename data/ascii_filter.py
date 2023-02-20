import logging
import string


class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> int:
        for sym in record.msg:
            if sym not in string.printable:
                return 0
            return 1