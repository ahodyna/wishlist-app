# Description

The Wish List App allows user to create a wish list, update it (e.g., change the status to completed), and delete wishes. You can also view all wishes and sort them by created_at, priority, and status.

Check the functionality of basic endpoints using swagger:

```
127.0.0.1:8000/docs
```

## Installation

You can run the project in several ways:

```
docker-compose up
```

Or use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```
pip install -r requirements.txt         
```
And then run the project

```
uvicorn app.main:app --reload --port 8080         
``` 
