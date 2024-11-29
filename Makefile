run:
	@python3 manage.py runserver 0.0.0.0:8000

migrate:
	@python3 manage.py makemigrations $(app)
	@python3 manage.py migrate $(app)

migrate all:
	@python3 manage.py makemigrations obra
	@python3 manage.py makemigrations veiculo
	@python3 manage.py makemigrations funcionario
	@python3 manage.py makemigrations estoque
	@python3 manage.py migrate obra
	@python3 manage.py migrate veiculo
	@python3 manage.py migrate funcionario
	@python3 manage.py migrate estoque

admin:
	@python3 manage.py createsuperuser