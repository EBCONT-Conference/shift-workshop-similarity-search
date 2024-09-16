from flask import Blueprint, render_template, request
from app.embedding import get_image_embedding
from app.elasticsearch_helper import search_similar_items
from app.elasticsearch_initializer import index_name_image
from PIL import Image
from app.helper_functions import convert_image_to_data_uri

image_similarity_routes = Blueprint('image_similarity_routes', __name__)

@image_similarity_routes.route('/similarity', methods=['GET', 'POST'])
def similarity():
    search_results = []
    query_image_id = ''

    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image = Image.open(uploaded_file)
            
            # Get embedding for the image
            query_embedding = get_image_embedding(image)
            
            # Search in elastic cluster for similar items
            search_results = search_similar_items(query_embedding, index_name_image, top_k=15, min_score=0.012)

            # Convert the uploaded image into a data URI in Base64 format 
            query_image_uri = convert_image_to_data_uri(image)

            query_image_id = uploaded_file.filename
    else:
        search_results = []
        query_image_uri = ''
        query_image_id = ''

    if query_image_id:
        query_image_uri = convert_image_to_data_uri(Image.open(uploaded_file))

    return render_template('image_similarity_search.html', query_results=search_results, query_image=query_image_uri)

