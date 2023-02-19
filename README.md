# developer_test

python3 -m venv env_test
source env_test/bin/activate
pip install -r requirements24.txt


# postgres settings
--set user in postgres , open new terminal

-- To connect to PostgreSQL using the postgres role, you switch over to the postgres account on your server by typing:
sudo -i -u postgres
--next command
psql

--by default this user has not LOGIN attributes. 
postgres=# CREATE ROLE s1_charmiliun;
--to add LOGIN attribute, we can use the next command
postgres=# ALTER ROLE s1_charmiliun LOGIN;
--TO SET UP PASSWORD
postgres=# ALTER ROLE s1_charmiliun PASSWORD 'GDRT$%&sdZ';
--crear base de datos para ese usuario usando el superusuario

-- salir
\q

createdb QuickstartTestDB --owner=s1_charmiliun;

# makemigrations and migrate, also create superuser
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser 