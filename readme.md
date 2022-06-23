# Fast API
<p align="center">
  <a href="https://www.rapidinnovation.io/" target="blank"><img src="static/images/ri_logo.jpeg" width="320" alt="RapidInnovation Logo" /></a>
</p>

Checkout *requirements.txt* for libraries used.

**Versions**
Python: 3.7

### Activate Virtual env
python -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Postgresql must have in your system.

    config.py
> DATABASE_URL = "enigne_name://myuser:mypass@localhost:port_name/db_name

Please change the engine_name, myuser, mypass and db_name


### Run the application

uvicorn main:app --reload

### Test the application

[Click Here](http://127.0.0.1:8000/docs)


### For more detail

https://fastapi.tiangolo.com/