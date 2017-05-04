"""This file accepts HTTP request and maps them to functions based on their path"""

from flask import render_template, request, redirect
from app import app, data_manager


@app.route('/')
@app.route('/list')
def list():
    """Contents for index and list page"""
    story = data_manager.get_table_from_file()
    return render_template("list.html", data=story)


@app.route('/story')
def story():
    """Contets for add new story page"""
    return render_template("form.html", title="Add new Story", data="", action="/new")


@app.route('/story/<int:ident>', methods=["GET"])
def modify(ident):
    """Contets for modify existing story page"""
    story = data_manager.get_table_from_file()
    for row in story:
        if row[0] == str(ident):
            data = row
    return render_template("form.html", title="Edit Story", data=data, action="/modify/" + data[0])


@app.route('/new', methods=['POST'])
def new():
    """Add new story to list, then redirect to /list page"""
    data = data_manager.get_table_from_file()
    data.append([str(len(data)+1), request.form['title'], request.form['story'], request.form['criteria'],
                 request.form['value'], request.form['estimation'], request.form['status']
                 ])
    data_manager.write_table_to_file(data)
    return redirect("/list")


@app.route('/modify/<int:ident>', methods=['POST'])
def edit(ident):
    """Modify story, save, then redirect to /list page"""
    data = data_manager.get_table_from_file()
    for row in data:
        if row[0] == str(ident):
            useless = row
    data.remove(useless)
    data.append([str(ident), request.form['title'], request.form['story'], request.form['criteria'],
                 request.form['value'], request.form['estimation'], request.form['status']
                 ])
    data_manager.write_table_to_file(data)
    return redirect("/list")


@app.route('/delete/<int:ident>')
def delete(ident):
    """Delete story, save, then redirect to /list page"""
    data = data_manager.get_table_from_file()
    for row in data:
        if row[0] == str(ident):
            useless = row
    data.remove(useless)
    for index, row in enumerate(data):
        row[0] = str(index+1)
    data_manager.write_table_to_file(data)
    return redirect("/list")
