from .relational_database_abc import RelationalDatabaseABC
from ...config.config import Config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class RelationalDatabase(RelationalDatabaseABC):
    def __init__(self, config = Config):
        self.session_local = self._session_local(config)
        self.base = self._base()

    def _session_local(self, config: Config):
        engine = create_engine(config.database_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return SessionLocal()

    def _base(self):
        return declarative_base()