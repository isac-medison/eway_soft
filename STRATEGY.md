# Data Analysis Strategy

## Objective
Objective: Identify the most high-traffic locations in the city that would be suitable for opening a commercial point (e.g., a coffee shop or a retail store).

## Analysis Goals
List clear, concrete goals of your analysis.

## Pipeline Overview
| Step                 | Tool                                     | Description                |
|:---------------------|:-----------------------------------------|:---------------------------|
| Data Collection      | requests + selenium to bypass cloudflare | Scrape stop and route data |
| Data Storage         | MySQL                                    | Normalize and store        |
| Data Processing      | pandas                                   | Load and group             |
| Data Analysis        | SQL pandas                               | Count and rank             |
| Output               | Tables / Charts                          | Present top stops          |

## Data Model
- stops
- routes
- stop_routes
- scrape_sessions

## Analysis Method
The analysis of stop usage is performed by determining how many distinct public transport routes pass through each stop. The higher the number of routes connected to a stop, the more significant and potentially high-traffic the stop is assumed to be.

## Data Update Strategy
For this demo project, the scraping process is manual, triggered by the user through a console desktop application. This setup provides a simple and interactive way for the user to scrape the latest data when needed.

## Output Format
The results of the data analysis is presented in a clear and concise manner to help identify the most high-traffic stops and routes in the city. The output is structured in the following ways:
- Tabular Data
- PIE Chart
- GEO Chart

## Documentation
This project includes comprehensive documentation to ensure transparency and clarity of the process, as well as to provide easy guidance for future developers or analysts. The documentation consists of readme.
