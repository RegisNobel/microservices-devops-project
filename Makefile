# Variables
PYTHON = python3
FLASK_ENV = development

# Targets
.PHONY: all clean run

all: clean install

install:
	cd frontend_service && pip install -r requirements.txt
	cd storage_service && pip install -r requirements.txt
	cd auto_mail_service && pip install -r requirements.txt

run:
	$(PYTHON) frontend_service/app.py &
	$(PYTHON) storage_service/app.py &
	$(PYTHON) auto_mail_service/app.py

stop:
	@-pkill -f "python3 frontend_service/app.py" || true
	@-pkill -f "python3 storage_service/app.py" || true
	@-pkill -f "python3 auto_mail_service/app.py" || true

clean:
	rm -rf *.pyc __pycache__ .pytest_cache

test:
	pytest tests/

lint:
	flake8 .

docs:
	pdoc --html --output-dir docs --force frontend_service storage_service auto_mail_service

# Other

