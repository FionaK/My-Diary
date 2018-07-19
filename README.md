[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/edcdf0ad2ec49ea2e97b)
[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Maintainability](https://api.codeclimate.com/v1/badges/c418889a39e570ccd2c5/maintainability)](https://codeclimate.com/github/FionaK/My-Diary/maintainability)

# My-Diary
  > Online diary that allows a user to make new entries, delete or modify an existing entry.

## Made with
 * python
     > flask
 * json

### How to run it
 clone the repository first
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
* run 
```sh
 python d_structure.py to start the server
```
####Endpoints
* /api/v1/ - home endpoint
* /api/v1/register/ - register
* /api/v1/login/ - login
* /api/v1/create_entry/ - creating a new entry
* /api/v1/display_entry/ - get all entries
* /api/v1/single_entry/ - get a single entry
* /api/v1/delete_entry/ - delete an entry
* /api/v1/modify_entry/ - modify an entry

