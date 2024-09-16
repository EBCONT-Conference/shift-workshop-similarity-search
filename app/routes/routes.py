from flask import Blueprint, redirect, url_for

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return redirect(url_for('image_upload_routes.upload'))







