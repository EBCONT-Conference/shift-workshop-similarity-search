from app.elasticsearch_initializer import elasticsearch_client, index_name_image

def save_image(image_id, embedding, image_data, ):
    """
    Function to store an image in the Elasticsearch index with its embedding and image data.
    
    :param image_id: The ID of the image to store in the index
    :param embedding: The embedding vector for the image
    :param image_data: The image data (can be a URL, base64, or any other format you are using)
    """
    # TODO: Implement the logic to save the image and its embedding in Elasticsearch
    #pass
    document = {
        "vector": embedding,
        "image_data": image_data
    }
    
    elasticsearch_client.index(index=index_name_image, id=image_id, document=document)
    

def search_similar_items(query_embedding, index_name, top_k=15, min_score=0.8):
    """
    Function to search for similar items in an Elasticsearch index using vector search.
    
    :param query_embedding: Embedding of the query text/image to search for similar items
    :param index_name: The name of the Elasticsearch index to search
    :param top_k: The number of top results to return (default: 15)
    :param min_score: Minimum score for filtering results (default: 0.8)
    :return: List of search results
    """
    # TODO: Implement the search logic using Elasticsearch's vector search capabilities
    #pass
    return "";

def get_all(offset, per_page, selected_index):
    #function to get all items of an index
    query = {
        "query": {
            "match_all": {}
        },
        "from": offset,
        "size": per_page
    }
    response = elasticsearch_client.search(index=selected_index, body=query)
    return response

def delete_index(selected_index):
    #function to delete an index
    elasticsearch_client.indices.delete(index=selected_index, ignore=[400, 404])

def index_exists(index_name):
    #check if an index exists
    return elasticsearch_client.indices.exists(index=index_name)

def get_relevant_image_data(response):
    return [(hit["_id"], hit["_score"], hit["_source"]['image_data']) for hit in response["hits"]["hits"]]  