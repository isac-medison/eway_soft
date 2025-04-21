import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
from pandasgui import show
import numpy as np
import matplotlib.pyplot as plt
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
def fetch_traffic_data():
    query = """
        SELECT s.id, s.name, COUNT(sr.route_id) AS route_count, s.latitude, s.longitude, s.eway_id
        FROM stops s
        JOIN stop_routes sr ON s.id = sr.stop_id
        GROUP BY s.id
        ORDER BY route_count DESC
    """
    return pd.read_sql(query, engine)

def show_table(df):
    show(df[['name', 'route_count', 'longitude', 'latitude', 'eway_id']])

def plot_pie_chart(df):
    total_stops = df.shape[0]
    top_stops = df.head(10)

    others_count = df['route_count'].iloc[10:].sum()

    values = top_stops['route_count'].tolist() + [others_count]
    labels = top_stops['name'].tolist() + ['Others']

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Top 10 High Traffic Stops (out of {total_stops} total stops)')
    plt.axis('equal')
    plt.show()


def plot_geo_chart(df):
    df_sorted = df.sort_values('route_count')

    lat_q1, lat_q3 = df_sorted['latitude'].quantile([0.25, 0.75])
    lat_iqr = lat_q3 - lat_q1
    lat_lower_bound = lat_q1 - 1.5 * lat_iqr
    lat_upper_bound = lat_q3 + 1.5 * lat_iqr

    lon_q1, lon_q3 = df_sorted['longitude'].quantile([0.25, 0.75])
    lon_iqr = lon_q3 - lon_q1
    lon_lower_bound = lon_q1 - 1.5 * lon_iqr
    lon_upper_bound = lon_q3 + 1.5 * lon_iqr

    df_filtered = df_sorted[
        (df_sorted['latitude'] >= lat_lower_bound) & (df_sorted['latitude'] <= lat_upper_bound) &
        (df_sorted['longitude'] >= lon_lower_bound) & (df_sorted['longitude'] <= lon_upper_bound)
    ]

    colors = df_filtered['route_count']
    sizes = df_filtered['route_count']

    plt.figure(figsize=(12, 10))
    scatter = plt.scatter(
        df_filtered['longitude'],
        df_filtered['latitude'],
        c=colors,
        cmap='coolwarm',
        s=sizes,
        alpha=0.8,
        edgecolors='k'
    )

    plt.colorbar(scatter, label='Number of Routes')

    plt.xticks(np.round(np.linspace(df_filtered['longitude'].min(), df_filtered['longitude'].max(), 10), 5))
    plt.yticks(np.round(np.linspace(df_filtered['latitude'].min(), df_filtered['latitude'].max(), 10), 5))

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Stop Traffic Intensity Map (scaled by route count)')
    plt.grid(True)
    plt.show()

