# Objective

The goal of this project is to analyze public transport route coverage at various stops in Lviv. It identifies high-traffic locations suitable for commercial points by:
- Scraping stops and their associated routes from a public API.
- Storing the data in a relational database.
- Tracking scrape sessions with timestamps.
- Visualizing the top stops by route connections via:
  - Scrollable tables.
  - Pie charts with grouped "others".
  - Geo scatter plots, color-graded by route count.

---
## Dependencies
### This project requires Python 3.11 or newer and libraries stated in requirements.txt

Install them using:

```
pip install -r requirements.txt
```
or 
```
make install
```

## Usage

### Install Dependencies:
```
make install
```

### To scrape public transport stops and routes into your database (city of scraping could be changed in config file /config/config.yaml):
```
make scrape
```

## Analyze Data:
### Run analysis and visualization tasks. You can pass optional flags via ARGS to control the type of visualization.

### Examples:

## Show interactive table:
```
make analyse ARGS="-table"
```
<p align="center">
  <img src="./images/table.jpg" alt="Table example" width="500"/>
</p>

## Show pie chart of top 10 stops:
```
make analyse ARGS="-pie"
```
<p align="center">
  <img src="./images/pie.jpg" alt="Pie example" width="500"/>
</p>

## Show geo scatter plot of traffic density:
```
make analyse ARGS="-map"
```
<p align="center">
  <img src="./images/map.jpg" alt="Map example" width="500"/>
</p>

## If no flag is passed, by default it will show the geo scatter plot.

## Notes

## The project assumes a MySQL database connection string is provided via the DATABASE_URL environment variable. Uses IQR filtering to remove spatial outliers from the geo scatter plot. Colors on geo plots are scaled using a logarithmic scale to better reflect differences in high-traffic areas.

## .env file needed in project folder
```
DATABASE_URL="mysql+pymysql://user:password@host/eway"
DATABASE_ENGINE="mysql+pymysql://user:password@host/"
```

## Patterns and Code Style
### This project follows clean, modular, and scalable design principles, with consistent application of several architectural patterns and conventions:

## Service-Repository
### Business logic is encapsulated within service classes, which depend on repository classes to handle all database access. This ensures separation of concerns and clean, testable code. All services, repositories etc inherit from base abstract classes to share abstract logic. Services are used to integrate business logic and repositories work with db session directly.

## Unit of Work Pattern
### A Unit of Work class manages database transactions, ensuring that changes are committed or rolled back as a single unit. Services receive a Unit of Work instance to guarantee transactional integrity.

## Command Pattern (in Makefile)
## The Makefile acts as a command dispatcher for key project actions like scraping data, running analysis, and installing dependencies, providing a clear, documented interface for executing tasks.

## Environment-Driven Configuration
### All database connections and environment-specific values are controlled via environment variables, loaded using os.getenv(). Mandatory variables like DATABASE_URL trigger explicit errors if not provided.

### Consistent Code Style

- Clean, explicit imports
- Flat service method structures
- No inline or anonymous lambdas for clarity
- Descriptive method names reflecting their actions
- No type annotations or docstrings unless absolutely necessary, to keep the code concise
- Error handling via try-except blocks around database transactions, with rollback on failure
- Separation of data models, repositories, and services within a clear project structure

