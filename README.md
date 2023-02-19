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
<br> This package is used in the [BeautifulSoup](task2/scraper/pipelines.py). |

3. Install the requirements:
    ```shell
    pip install -r requirements.txt
    ```

# postgres settings
1. set user in postgres , open new terminal
2. To connect to PostgreSQL using the postgres role, you switch over to the postgres account on your server by typing:
    ```shell
    sudo -i -u postgres
    ```
3. next command -- PostgreSQL interactive terminal
    ```shell
    psql
    ```

4. by default this user has not LOGIN attributes. 
postgres=# 
    ```shell
    postgres=# CREATE ROLE s1_charmiliun;
    ```

5. to add LOGIN attribute, we can use the next command
    ```shell
    postgres=# ALTER ROLE s1_charmiliun LOGIN;
    ```

6. TO SET UP PASSWORD
    ```shell
    postgres=# ALTER ROLE s1_charmiliun PASSWORD 'GDRT$%&sdZ';
    ```
7. crear base de datos para ese usuario usando el superusuario, but first go out!
    ```shell
        \q
    ```
    ```shell
        createdb QuickstartTestDB --owner=s1_charmiliun;
    ```

createdb QuickstartTestDB --owner=s1_charmiliun;

# makemigrations and migrate, also create superuser
python3 manage.py makemigrations

1. Run the migrations:

    ```shell
    python manage.py migrate
    ```
2. Run the local server:

    ```shell
    python manage.py runserver
    ```
3. If you'd like to access /admin, you'll need a Django superuser. Navigate to the page:
    ```shell
    python manage.py createsuperuser 
    ```
