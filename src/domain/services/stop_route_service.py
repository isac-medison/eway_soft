from datetime import datetime
from domain.models.scrape_session import ScrapeSession
from domain.repositories.route_repository import RouteRepository
from domain.repositories.scrape_session_repository import ScrapeSessionRepository
from domain.repositories.stop_repository import StopRepository
from domain.unit_of_work import UnitOfWork
from domain.repositories.stop_route_repository import StopRouteRepository
from .base_service import BaseService
from domain.models import StopRoute, Stop, Route

class StopRouteService(BaseService):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow, StopRouteRepository)
        self.route_repo = RouteRepository(uow.session)
        self.stop_repo = StopRepository(uow.session)
        self.scrape_repo = ScrapeSessionRepository(uow.session)
        
    def link_stop_route(self, stop_id, route_id):
        stop_route = StopRoute(stop_id=stop_id, route_id=route_id)
        self.add(stop_route)

    def insert_stops_and_routes(self, df_stops, df_routes):
        try:
            super().delete_deprecetad_data()
            print("inserting stops and routes into db")
            scrape_session = ScrapeSession(timestamp=datetime.utcnow())
            self.scrape_repo.add(scrape_session)
            stop_map = {}
            route_map = {}
            for _, row in df_stops.iterrows():
                stop = Stop(
                    eway_id=row['id'],
                    name=row['name'],
                    latitude=row['latitude'],
                    longitude=row['longitude']
                )
                self.route_repo.add(stop)
                stop_map[row['id']] = stop

            for _, row in df_routes.drop_duplicates(subset=['transport_type', 'name']).iterrows():
                route = Route(
                    transport_type=row['transport_type'],
                    name=row['name']
                )
                self.stop_repo.add(route)
                route_map[(row['transport_type'], row['name'])] = route

            self.uow.session.flush()

            for _, row in df_routes.iterrows():
                stop = stop_map.get(row['stop_id'])
                route = route_map.get((row['transport_type'], row['name']))
                if stop and route:
                    stop_route = StopRoute(
                        stop=stop,
                        route=route
                    )
                    self.repo.add(stop_route)

            self.uow.commit()

        except Exception as e:
            self.uow.session.rollback()
            print(f"Error during insert: {e}")
                
