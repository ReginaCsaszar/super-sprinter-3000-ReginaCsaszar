from flask import render_template
from app import app


@app.route('/')
@app.route('/list')
def list():
    return render_template("list.html")


@app.route('/story')
def story():
    return render_template("form.html", title="Add new Story")
