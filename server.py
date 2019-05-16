import json as j
import logging
import sqlite3

from sanic import Sanic
from sanic.request import Request
from sanic.response import json

from entitites import create_tables, insert_exception

app = Sanic()


@app.route('/', methods=frozenset({"POST"}))
async def test(request: Request):
    try:
        payload = j.loads(request.json)
    except Exception as err:

        return json({"status": "Malformed request: " +
                               str(err)
                     }, status=400)

    if "err" not in payload:
        return json({"status": "Malformed request: err is missing!"}, status=400)

    if "metadata" not in payload:
        return json({"status": "Malformed request: metadata is missing!"}, status=400)

    try:
        insert_exception(app.db,
                         payload["err"],
                         **payload["metadata"],
                         )
    except Exception:
        logging.exception("Could not persist payload!")
        return json({"status":
                         "Malformed request: could not persist the payload!"},
                    status=400)


    else:
        return json({'status': "Exception successfully persisted"})


if __name__ == '__main__':
    db = sqlite3.connect("exceptd.db")
    create_tables(db)
    app.db = db
    app.run(host='0.0.0.0', port=1337)
