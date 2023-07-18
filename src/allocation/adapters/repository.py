import abc
from src.allocation.domain import model


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user_info(self, user: model.User, role: model.Role, claim: model.Claim, user_claim: model.UserClaim):
        raise NotImplementedError
    
    @abc.abstractmethod
    def add_user_role(self, role: model.Role):
        raise NotImplementedError

    @abc.abstractmethod
    def get_role_by_id(self, role_id: int) -> model.Role:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_info(self):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def get_user_info(self):
        return (
            self.session.query(
                model.User.name,
                model.User.email,
                model.Role.description.label('role_description'),
                model.Claim.description.label('claim_description')
            )
            .join(model.Role)
            .join(model.UserClaim)
            .join(model.Claim)
            .all()
        )

    def get_role_by_id(self, role_id: int) -> dict:
        role = self.session.query(model.Role).filter_by(role_id=role_id).first()
        if role:
            return {
                "role_id": role.role_id,
                "description": role.description
            }
        return {}

    def add_user_info(self, user: model.User, claim: model.Claim, user_claim: model.UserClaim):
        self.session.add_all([user, claim])
        self.session.flush()
        user_claim.user_id = user.id
        user_claim.claim_id = claim.id
        self.session.add(user_claim)

    def add_user_role(self, role: model.Role):
        self.session.add(role)
