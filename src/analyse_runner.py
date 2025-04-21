import sys
from domain.analysis import *
from dotenv import load_dotenv

if __name__ == "__main__":
    try:
        load_dotenv()
        args = sys.argv[1:]
        df = fetch_traffic_data()
        if not args:
            plot_geo_chart(df)
        else:
            if "-table" in args:
                show_table(df)
            if "-pie" in args:
                plot_pie_chart(df)
            if "-map" in args:
                plot_geo_chart(df)
    except Exception as e:
        print("Error during running pipeline: {e}")
