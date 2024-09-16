from flask import Blueprint, render_template, request
from app.elasticsearch_helper import get_all, delete_index, index_exists
from app.elasticsearch_initializer import index_name_image

browse_routes = Blueprint('browse_routes', __name__)

@browse_routes.route('/browse', methods=['GET', 'POST'])
def browse():
    if not index_exists(index_name_image):
        message = f"'{index_name_image}' doesn't exist."
        return render_template('browse.html', images=[], message=message, index=index_name_image)

    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page

    response = get_all(offset, per_page, index_name_image)

    images = [(hit["_id"], hit["_source"]["image_data"], None, None) for hit in response["hits"]["hits"]]

    total_hits = response['hits']['total']['value']
    total_pages = (total_hits + per_page - 1) // per_page

    return render_template('browse.html', images=images, page=page, total_pages=total_pages, index=index_name_image)

@browse_routes.route('/delete_all_images', methods=['POST'])
def delete_all_images():
    delete_index(index_name_image)
    message = f"'{index_name_image}' doesn't exist."
    return render_template('browse.html', images=[], message=message, index=index_name_image)
