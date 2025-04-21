from dotenv import load_dotenv
from domain.services.stop_route_service import StopRouteService
from infrastructure.db_session import init_db
from infrastructure.scraper import get_cf_clearance, get_stops_data
from infrastructure.data_normalization import normalize_stops, normalize_routes
from domain.unit_of_work import UnitOfWork
from infrastructure.db_session import SessionLocal

def run_scrape_pipeline():

        load_dotenv()
        init_db()
        cf_clearance = get_cf_clearance()
        stops_data = get_stops_data(cf_clearance)
        df_stops = normalize_stops(stops_data)
        df_routes = normalize_routes(df_stops)
        try:
            session = SessionLocal()    
            uow = UnitOfWork(session)
            service = StopRouteService(uow)
            service.insert_stops_and_routes(df_stops, df_routes)
            uow.commit()    
        except Exception as e:
            print("Error during running pipeline: {e}")
        finally:
            session.close()
        


if __name__ == "__main__":
    try:
        run_scrape_pipeline()
    except Exception as e:
        print("Error during running pipeline: {e}")
