from app import app
from flask import render_template, redirect, url_for, request
from app.data import locations, events

@app.route('/')
def hello():
  return 'Hello'

