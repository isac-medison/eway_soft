from domain.unit_of_work import UnitOfWork
from sqlalchemy import text

class BaseService:
    def __init__(self, uow: UnitOfWork, repo_class):
        self.uow = uow
        self.repo = repo_class(uow.session) 

    def add(self, entity):
        self.repo.add(entity)
        self.uow.commit() 

    def get(self, entity_id):
        return self.repo.get(entity_id)

    def get_all(self):
        return self.repo.get_all()

    def update(self, entity):
        self.repo.update(entity)
        self.uow.commit()

    def delete(self, entity):
        self.repo.delete(entity)
        self.uow.commit()
    
    def delete_deprecetad_data(self):
        print("deleting deprecated info from db tables")
        self.uow.session.execute(text("DELETE FROM stop_routes;"))
        self.uow.session.execute(text("DELETE FROM stops;"))
        self.uow.session.execute(text("DELETE FROM routes;"))
