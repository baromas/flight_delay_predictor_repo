from run import app
from model import *
from flask import render_template, request, redirect, url_for


@app.route('/')
def main():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        if check_user(username, password):
            return render_template('index.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registrate_user(username, password)
        return redirect(url_for('login'))
    return render_template('register.html')
