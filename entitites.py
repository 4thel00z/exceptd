import json
import typing

CREATE_EXCEPTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS exceptions (
  id        integer primary key autoincrement,
  exception text,
  metadata  text
);
"""
DROP_EXCEPTIONS_TABLE = """DROP TABLE IF EXISTS exceptions;"""
INSERT_EXCEPTIONS_TABLE = """INSERT INTO exceptions ( exception, metadata) VALUES ($0,$1);"""

DELETE_EXEPTIONS_BY_ID = """DELETE FROM exceptions WHERE id = $0;"""
DELETE_EXEPTIONS_BY_EXCEPTION = """DELETE FROM exceptions WHERE exception = $0;"""
DELETE_EXEPTIONS_BY_METADATA = """DELETE FROM exceptions WHERE metadata = $0;"""
DELETE_EXEPTIONS = """DELETE FROM exceptions;"""


def create_tables(db, ):
    db.execute(CREATE_EXCEPTIONS_TABLE)
    db.commit()


def drop_tables(db, ):
    db.execute(DROP_EXCEPTIONS_TABLE)
    db.commit()


def insert_exception(db, exception: Exception, **metadata: typing.Union[int, float, str, bool], ):
    serialized = str(exception), json.dumps(metadata)
    db.execute(INSERT_EXCEPTIONS_TABLE, serialized)
    db.commit()


def delete_tables(db, ):
    db.execute(DELETE_EXEPTIONS)
    db.commit()


def delete_exceptions_by_id(db, id_: int, ):
    db.execute(DELETE_EXEPTIONS_BY_ID, (id_,))
    db.commit()


def delete_exceptions_by_exception(db, exception: Exception, ):
    db.execute(DELETE_EXEPTIONS_BY_EXCEPTION, (str(exception, ),))
    db.commit()


def delete_exceptions_by_metadata(db, metadata: typing.Dict, ):
    db.execute(DELETE_EXEPTIONS_BY_METADATA, (json.dumps(metadata),))
    db.commit()
