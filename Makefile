runserver:
	. venv/bin/activate; cd testproject; python manage.py runserver

test:
	. venv/bin/activate; cd testproject; python manage.py test tests --with-yanc