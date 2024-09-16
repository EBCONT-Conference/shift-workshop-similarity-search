from flask import Flask
from app.routes.routes import app_routes
from app.routes.text_search import text_search_routes
from app.routes.image_upload import image_upload_routes
from app.routes.browse import browse_routes
from app.routes.image_similarity_search  import image_similarity_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_routes)
    app.register_blueprint(browse_routes)
    app.register_blueprint(text_search_routes)
    app.register_blueprint(image_upload_routes)
    app.register_blueprint(image_similarity_routes)
    
    return app
