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
http://127.0.0.1:5000/api/v2/create_entry/?access_token={}
```
  * title
  * entry
  * username
```sh
http://127.0.0.1:5000/api/v2/display_entry/?access_token={}
```
```sh
http://127.0.0.1:5000/api/v2/single_entry/5?access_token={}
```
```sh
http://127.0.0.1:5000/api/v2/delete_entry/1?access_token={}
```
```sh
http://127.0.0.1:5000/api/v2/modify_entry/2?access_token={}
```
 * title
 * entry
 * username
```sh
http://127.0.0.1:5000/api/v2/get_user/?access_token={}
```

