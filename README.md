# Bookstore API

## Documentation:
* Home directory (/): http://127.0.0.1:5000/

## Requirements:
* Python3
* Virtualenv

## Installing the requirements
```
sudo apt install virtualenv
sudo apt install python3
```

## Preparing the environment
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

## Configuring the application
```
source env/bin/activate
export FLASK_APP=main.py
export FLASK_DEBUG=1 //run with live reload and debugger
```

## Running the application
```
flask run
```

## Installing new packages
```
pip install <package-name>
```

## Saving installed packages on the environment
```
pip freeze > requirements.txt
```

## Running tests
```
pytest
```
