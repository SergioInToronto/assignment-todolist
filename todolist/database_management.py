import os
import uuid

from sqlalchemy import Column, MetaData, Table, create_engine
from sqlalchemy.dialects.postgresql import UUID, JSONB


_metadata = MetaData()

table_todos = Table('todos', _metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('contents', JSONB),  # I'm using postgres as a document store
)


def get_engine():
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError('Required env var "DATABASE_URL" is not set')

    # engine = create_engine('sqlite:///:memory:', echo=True)
    engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
    _metadata.create_all(engine)  # Create tables if needed

    return engine
