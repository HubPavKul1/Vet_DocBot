import logging
import shlex
import subprocess


class CustomFileHandler(logging.Handler):
    def __init__(self, filename, mode='a'):
        super().__init__()
        self.filename = filename
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        with open(self.filename, mode=self.mode) as f:
            f.write(message + '\n')


class ServerHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.url = "http://127.0.0.1:5000/logs"
        self.method = "POST"

    def emit(self, record: logging.LogRecord) -> None:
        log = self.format(record)
        command_str = f'curl -X {self.method} {self.url} --data "log={log}" \n'
        command = shlex.split(command_str)
        subprocess.run(command)

