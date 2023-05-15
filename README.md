# URL Shortener

URL Shortener enables users to generate short and unique codes for long URLs, making them more convenient for sharing and accessing.

### Installation:

Clone the repository: git clone https://github.com/ismailov0/url-shortener.git
Navigate to the project folder: cd url-shortener
```sh
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

Open your browser to http://localhost:8000/api/short-url/ to view API.

### Endpoints:
Endpoint for retrieving all shorted url:
```sh
http://127.0.0.1:8000/api/short-url/<short_code>
```

Endpoint for create short url:
```sh
http://127.0.0.1:8000/api/short-url/
```

<img width="1162" alt="image" src="https://github.com/ismailov0/url-shortener/assets/98686806/89ea4811-1e6e-40d0-8361-c15864fad35e">