#!/usr/bin/env python
#app.py

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSSWORD'] = 'example'
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



mysql = MySQL(app)

@app.route("/")
def index():
    return "hello world !"


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0',debug = True)
