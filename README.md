[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/edcdf0ad2ec49ea2e97b)
[![Build Status](https://travis-ci.org/FionaK/My-Diary.svg?branch=challenge3)](https://travis-ci.org/FionaK/My-Diary)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Maintainability](https://api.codeclimate.com/v1/badges/c418889a39e570ccd2c5/maintainability)](https://codeclimate.com/github/FionaK/My-Diary/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/FionaK/My-Diary/badge.svg?branch=challenge3)](https://coveralls.io/github/FionaK/My-Diary?branch=challenge3)
# My-Diary
  > Online diary that allows a user to make new entries, delete or modify an existing entry.

## Made With
   * python
      > flask
   * json
   * postgres database

### How to run it
  > clone the repository first
```sh
git clone https://github.com/FionaK/My-Diary.git
```
* cd into the project folder

* create virtual environment
```sh
virtualenv venv
```
* activate the virtual environment
```sh
source venv/bib/activate
```
* run pip freeze > requirements.txt to install the required external modules

* install the required modules using the following command;
```sh
pip install -r requirements.txt
```
* Run
```sh
python run.py to start the server
```
* Open postgreSQL, start its server and create a database called 'diary'
```sh
$ service postgresql start
$ sudo -u postgres psql
$ CREATE DATABASE diary;
```
* Create a connection;
```sh
conn = psycopg2.connect("dbname='diary' user = 'postgres' password = 'fifi' host = 'localhost' port = '5432'")
```

###Endpoints
```sh
http://127.0.0.1:5000/api/v2/
```
```sh
http://127.0.0.1:5000/api/v2/register/
```
  * name
  * username
  * password
  * email
```sh
http://127.0.0.1:5000/api/v2/login/
```
  * username
  * password
```sh
http://127.0.0.1:5000/api/v2/create_entry/
```
  * title
  * entry
  * username
```sh
http://127.0.0.1:5000/api/v2/display_entry/
```
```sh
http://127.0.0.1:5000/api/v2/single_entry/5
```
```sh
http://127.0.0.1:5000/api/v2/delete_entry/1
```
```sh
http://127.0.0.1:5000/api/v2/modify_entry/2
```
 * title
 * entry
 * username
```sh
http://127.0.0.1:5000/api/v2/get_user/
```
### heroku link
[link to heroku](https://diary25.herokuapp.com/api/v2/)


