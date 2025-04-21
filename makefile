.PHONY: scrape install
scrape:
	python src/scrape_runner.py

analyse:
	python src/analyse_runner.py $(ARGS)

install:
	pip install -r requirements.txt
