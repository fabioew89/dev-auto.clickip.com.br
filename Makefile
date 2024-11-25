flask-run:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@python3 -m flask --app run.py run --debug