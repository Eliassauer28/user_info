# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


from src.allocation import config
from src.allocation.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    users: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __getattr__(self, name):
        atrr = self.__dict__.get(name, None)
        if name == "session_factory" and not atrr:
            self.session_factory = sessionmaker(
                bind=create_engine(config.get_postgres_uri(), echo=True))
            atrr = self.session_factory
        return atrr

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.users = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
