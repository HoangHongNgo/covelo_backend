# Covelo Backend

## Installation

Create a new virtual environment using the following command:

```bash
python -m venv env
```

Activate the virtual environment by running the activate script. On Windows, run the following command:

```bash
env\Scripts\activate
```

Once the virtual environment is activated, you can install the packages listed in the requirements.txt file using the following command:

```bash
pip install -r requirements.txt
```

Update the requirements.txt by:
```bash
pip freeze > requirements.txt
```

Run the server:

```bash
python manage.py runserver
```

Customize database connection in **settings.py**:

```python
DATABASES = {
    'default': {
    }
}
```

To access the API documentation:

```bash
http://localhost:8000/docs/
```
