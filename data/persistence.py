# -*- coding: utf-8 -*-

import os

from config import session_file
from domain.session import SessionNotFinished


def save_session(session):
    if session.end_time is None:
        raise SessionNotFinished

    with open(session_file, mode="a") as file:
        if os.path.getsize(session_file) == 0:
            header = ', '.join(list(session.data.keys()))
            file.write(header)

        data = [str(element) for element in session.data.values()]
        row = ', '.join(data)
        file.write('\n' + row)
