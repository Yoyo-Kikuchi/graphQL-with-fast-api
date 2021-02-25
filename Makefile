.PHONY: dev

dev:
	uvicorn src.app:app --reload --host 0.0.0.0 --port 3000
