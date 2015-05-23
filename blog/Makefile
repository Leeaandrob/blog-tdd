run: clean
	python manage.py runserver

shell: clean
	python manage.py shell

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrate: clean
	python manage.py migrate

tests: clean
	python manage.py test --settings=blog.settings_tests
