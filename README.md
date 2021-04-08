# Flask File Uploads

One feature of web applications is the ability to upload a file to an app. Flask provides for such implementations. [In this article](https://github.com/GitauHarrison/notes/blob/master/file_upload_in_flask.md), I show how one can create a simple Flask app from scratch and allow for file uploads.

Kindly note that this project assumes you have a basic understinding of Flask. You need to at least know how to structure a flask application and use various flask and Python packages. If you are not already familiar with Flask, consider looking at this introdutory [personal blog web development tutorial](https://github.com/GitauHarrison/notes/blob/master/web_development/personal_blog/personal_blog.md) to learn more.

### Features

* File Upload

### Tools Used

* Flask Framework
* Twitter Bootstrap for styling
* Python3 for programming
* Flask-WTF for form creation
* DropzoneJS for simpler file upload

### Contributors
* [Gitau Harrison](https://github.com/GitauHarrison)

### Testing

To test the project, youcan clone this repo to your local machine by running the command below in your terminal:

```python
$ git clone git@github.com:GitauHarrison/handling-file-uploads-in-flask.git
```

Create and activate your virtual environment before running the flask server:

```python
$ mkvirtualenv file_upload  # I am using virtualenvwrapper 
```

Install used dependancies by running:

```python
(file_upload)$ pip3 install -r requirements.txt
```

Run the application:

```python
(file_upload)$ flask run
```