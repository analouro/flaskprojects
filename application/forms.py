from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    new_task = StringField("Write your task:")
    submit = SubmitField("Submit task")