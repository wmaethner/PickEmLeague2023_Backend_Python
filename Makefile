MESSAGE=""

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d .venv || virtualenv .venv
	. .venv/bin/activate; pip install -r requirements.txt
	touch .venv/touchfile

run: venv
	. .venv/bin/activate; \
	flask run

shell: venv
	. .venv/bin/activate; \
	flask shell

clean:
	rm -rf __pycache__
	rm -rf .venv

migrate: venv
	. .venv/bin/activate; \
	flask db migrate -m $(MESSAGE)

upgrade: venv
	. .venv/bin/activate; \
	flask db upgrade

downgrade: venv
	. .venv/bin/activate; \
	flask db downgrade
