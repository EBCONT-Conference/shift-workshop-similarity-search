from elasticsearch import Elasticsearch
import os

es_host = os.getenv('ELASTICSEARCH_HOST', 'http://localhost:9200')

elasticsearch_client = Elasticsearch([es_host])

# image embeddings index
index_name_image = "image_index"

image_mapping = {
    "mappings": {
        "properties": {
            "vector": {
                "type": "dense_vector",
                "dims": 512,
                "similarity": "cosine"
            },
            "image_data": {
                "type": "text"
            }
        }
    }
}

# Check and create image_embeddings index
if not elasticsearch_client.indices.exists(index=index_name_image):
    elasticsearch_client.indices.create(index=index_name_image, body=image_mapping)