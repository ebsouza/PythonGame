# -*- coding: utf-8 -*-

from datetime import datetime


class SessionNotStarted(Exception):
    ...

class SessionNotFinished(Exception):
    ...

class SessionAlreadyFinished(Exception):
    ...


class Session:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.data = dict()

    @property
    def elapsed_time(self):
        if self.end_time is None:
            return None

        return (self.end_time - self.start_time).seconds

    def start(self):
        self.start_time = datetime.utcnow()

    def finish(self):
        if self.start is None:
            raise SessionNotStarted()

        self.end_time = datetime.utcnow()
        self.data['elapsed_time'] = self.elapsed_time

    def save_record(self, record):
        if self.end_time is not None:
            raise SessionAlreadyFinished

        for key, value in record.items():
            self.data[key] = value
