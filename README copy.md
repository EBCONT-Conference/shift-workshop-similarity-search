# Build a Similarity Search Engine for Images and Text in 1 Hour Using AI Models and Vector Databases

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Workshop Workflow](#workshop-workflow)
- [URLs](#urls)
- [Contributors](#contributors)

## Introduction

Welcome to the similarity search workshop! 

Imagine if you could build a search engine where you upload a picture to find similar content - like a shirt looking like one you saw online in a webshop - or get matching search results on similar descriptions, even if the actual text is different. This is what AI models and Vector Databases help you accomplish. In this workshop, you will learn to build a similarity search engine that leverages AI models and vector databases. The project will involve setting up Docker containers for necessary services, processing images and text data, and implementing search functionalities based on vector similarity.

## Prerequisites

- **Docker**: Required to run the containerized services.
- **Git**: Required to clone the repository.
- **Setup**: Follow the [Setup Instructions](#setup) to prepare your environment. We recommend completing this step beforehand, as a stable connection is required to install the necessary Docker containers.
- **Basic Knowledge**: Familiarity with AI models, Docker, and vector databases is helpful but not necessary.

## Setup

1. **Clone Repository**: Open your terminal and run:  
   ```bash
   git clone <repository-link>
    ``` 
2. **Navigate to Directory**:
   ```bash
   cd shift-similaritysearch-workspace/
    ``` 
3. **Set Up Docker**: Download and set up the required Docker images:
   ```bash
   docker compose up -d
    ``` 
4. **Download Sample Data**: Obtain sample data from this [link](https://www.kaggle.com/datasets/kunalgupta2616/dog-vs-cat-images-data?resource=download) or other relevant sources.
5. Ensure Docker is running and all necessary services are up.
6. Verify that the web application is accessible at [http://localhost:5000/upload](http://localhost:5000/upload).

## Workshop Workflow

1. **Setting Up the Environment**: Learn how to configure Docker and integrate with the Elastic vector search engine.
2. **Introduction to Vector Search**: Understand the basics of vector search and how it applies to images and text.
3. **Processing Data**: Work with sample images and text data to create vectors.
4. **Building the Search Engine**: Implement the search engine functionality and test it with the sample data.

## URLs
- Webapp: [http://localhost:5000](http://localhost:5000)
- Kibana: [Kibana Console](http://localhost:5601/app/dev_tools#/console)
- Local Image Sample Data (Partial data): [Nike fashion products Images](sample_data/fashion_products/), [Dog vs Cat Images](sample_data/dog_cat_images/)
- Full Sample Data Download URLs: [Nike fashion products Images](https://www.kaggle.com/datasets/crawlfeeds/nike-fashion-products-dataset), [Dog vs Cat Images](https://www.kaggle.com/datasets/kunalgupta2616/dog-vs-cat-images-data)


## Contributors

- **Christoph Eder**
- **Patrick Iszovits**
- **Dino Duranovic**