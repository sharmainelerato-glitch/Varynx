.PHONY: run
run:
	docker build -t varynx .
	docker run --rm -p 5000:5000 --env-file .env varynx
