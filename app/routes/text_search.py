from flask import Blueprint, render_template, request
from app.embedding import get_text_embedding
from app.elasticsearch_helper import search_similar_items
from app.elasticsearch_initializer import index_name_image


text_search_routes = Blueprint('text_search_routes', __name__)

@text_search_routes.route('/text_search', methods=['GET', 'POST'])
def text_search():
    search_results = []
    query_text = ''

    if request.method == 'POST':
        query_text = request.form['query']
        
        #Get embedding for the text
        query_embedding = get_text_embedding(query_text)
        
        #Search in elastic cluster for similar items
        search_results = search_similar_items(query_embedding, index_name_image, min_score=0)

    return render_template('text_search.html', query_results=search_results, query_text=query_text)