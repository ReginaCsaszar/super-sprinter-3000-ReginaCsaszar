"""This file accepts HTTP request and maps them to functions based on their path"""

from flask import render_template
from app import app, data_manager


@app.route('/')
@app.route('/list')
def list():
    """Contents for index and list page"""
    story = data_manager.get_table_from_file()
    return render_template("list.html", data=story)


@app.route('/story')
def story():
    """Contets for story page: add and modify new story"""
    return render_template("form.html", title="Add new Story")
