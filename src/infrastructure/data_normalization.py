import pandas as pd

def normalize_stops(data):
    print("normalizing stops")
    stops_list = []
    for id, stop_data in data.items():
        routes = stop_data[3]
        if routes and (set(routes.keys()) - {"train"}):
            stop_entry = {
                "id": int(id),
                "latitude": stop_data[0] / 1e6,
                "longitude": stop_data[1] / 1e6,
                "name": stop_data[2],
                "routes": routes
            }
            stops_list.append(stop_entry)
    return pd.DataFrame(stops_list)

def normalize_routes(df):
    print("normalizing routes")
    records = []
    for _, row in df.iterrows():
        for transport_type, route_names in row['routes'].items():
            route_numbers = [r.strip() for r in route_names.split(',')]
            for route_number in route_numbers:
                records.append({
                    "name": route_number,
                    "stop_id": row["id"],
                    "transport_type": transport_type,
                })
    return pd.DataFrame(records)
