# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
from application import app
# from application import routes
# from application.forms import TaskForm
# from wtforms import StringField, SubmitField

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
