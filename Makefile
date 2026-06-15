# Diabetes Prediction System - Makefile
.PHONY: help install test lint format clean run-dashboard run-api docker-build docker-up docker-down

help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run linters"
	@echo "  make format        - Format code"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make run-dashboard - Run Streamlit dashboard"
	@echo "  make run-api       - Run FastAPI server"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-up     - Start Docker containers"
	@echo "  make docker-down   - Stop Docker containers"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v --cov=src --cov-report=html

lint:
	flake8 src/ tests/
	pylint src/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

clean:
	rm -rf build/ dist/ .egg-info/
	rm -rf __pycache__/ .pytest_cache/ .mypy_cache/
	rm -rf htmlcov/ .coverage
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -delete

run-dashboard:
	streamlit run app.py

run-api:
	uvicorn api:app --reload --host 0.0.0.0 --port 8000

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f
