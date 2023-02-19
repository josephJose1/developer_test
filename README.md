# developer_test
### Local development

python3 -m venv env_test
source env_test/bin/activate

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [pyscopg2-binary](https://pypi.org/project/psycopg-binary/) | PostgreSQL database adapter for Python. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, those variables describe how to connect to the database locally. <br><br> This package is used in the [manage.py](./manage.py) file to load environment variables. |
| [requests](https://pypi.org/project/requests/) | Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method! <br>
<br> This package is used in the [BeautifulSoup](task2/scraper/pipelines.py) file. |

3. Install the requirements:
    ```shell
    pip install -r requirements.txt
    ```
4. Create an `.env` file using `.env.sample` as a guide. Set the value of `DBNAME` to the name of an existing database in your local PostgreSQL instance. Set the values of `DBHOST`, `DBUSER`, and `DBPASS` as appropriate for your local PostgreSQL instance.

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

3. Run the migrations:

    ```shell
    python manage.py migrate
    ```
4. Run the local server:

    ```shell
    python manage.py runserver
    ```
python manage.py createsuperuser 