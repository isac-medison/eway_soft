from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def add(self, entity):
        self.session.add(entity)
        return entity

    def get(self, entity_id):
        return self.session.get(self.model, entity_id)

    def list_all(self):
        return self.session.query(self.model).all()

    def delete(self, entity):
        self.session.delete(entity)

    def filter_by(self, **kwargs):
        return self.session.query(self.model).filter_by(**kwargs).all()
