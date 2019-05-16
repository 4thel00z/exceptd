import json
import logging
import sqlite3
from contextlib import contextmanager

import requests

from entitites import insert_exception
logging.basicConfig(level=logging.DEBUG)

@contextmanager
def catch_locally(url, *exc_cls: type, **metadata):
    db = None
    if not exc_cls:
        exc_cls = (Exception,)
    try:
        db = sqlite3.connect(url)
        yield
    except exc_cls as err:
        if err and db:
            insert_exception(db, err, **metadata)
    finally:
        if db:
            db.close()


@contextmanager
def catch_remote(url, *exc_cls: type, **metadata):
    if not exc_cls:
        exc_cls = (Exception,)
    try:
        yield
    except exc_cls as err:
        payload = {"err": str(err), "metadata": metadata}
        response = requests.post(url, json=json.dumps(payload))
        logging.debug(response.json())
    finally:
        pass


if __name__ == '__main__':
    with catch_remote("http://0.0.0.0:1337", ):
        raise Exception("works")
