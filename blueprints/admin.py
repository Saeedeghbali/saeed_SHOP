from flask import Flask
from flask.blueprints import Blueprint

app=Blueprint("admin",__name__)

@app.route('/admin')
def admin():
    """Renders a sample page."""
    return "This is admin page!!"
