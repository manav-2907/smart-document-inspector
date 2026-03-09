# Smart Document Inspector

AI-powered document understanding system that analyzes document images and extracts structured information using OpenAI vision models.

## Features

- Detects document type (receipt, invoice, ID card, prescription)
- Extracts structured JSON data
- FastAPI backend API
- Vision-enabled LLM processing

## Tech Stack

Python  
FastAPI  
OpenAI API  
Computer Vision  

## Installation

git clone https://github.com/manav-2907/smart-document-inspector.git

cd smart-document-inspector

pip install -r requirements.txt

## Run Server

uvicorn app:app --reload

## API Endpoint

POST /analyze

Upload a document image to receive structured JSON output.
