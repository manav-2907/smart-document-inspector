# Smart Document Inspector API

An AI-powered document analysis API that automatically detects document types and extracts structured data from receipts, invoices, ID cards, and prescriptions using OpenAI's Vision API.

## Features

- **Automatic Document Type Detection**: Identifies receipts, invoices, ID cards, prescriptions, and other documents
- **Structured Data Extraction**: Extracts key information in JSON format
- **Vision AI Powered**: Uses OpenAI's GPT-4 Vision for accurate text extraction
- **REST API**: Easy-to-integrate FastAPI endpoint

## Supported Document Types

1. **Receipt**: Store name, date, total amount, tax, payment method
2. **Invoice**: Invoice number, seller, buyer, date, total amount, GST number
3. **ID Card**: Name, DOB, ID number, address, issuer
4. **Prescription**: Patient name, doctor name, hospital, date, medicines list

## API Endpoints

### Health Check
```
GET /
```
Response:
```json
{
  "status": "running"
}
```

### Analyze Document
```
POST /analyze
```
Upload a document image and get structured JSON output.

**Request**: `multipart/form-data` with file field
**Response**: JSON with extracted fields

Example:
```json
{
  "result": {
    "document_type": "receipt",
    "store_name": "ABC Stores",
    "date": "2024-03-15",
    "total_amount": "₹1,250.00",
    "tax": "₹225.00",
    "payment_method": "Card",
    "summary": "Purchase receipt from ABC Stores"
  }
}
```

## Setup & Installation

### Prerequisites
- Python 3.11+
- OpenAI API Key

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/manav-2907/smart-document-inspector.git
cd smart-document-inspector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the application:
```bash
uvicorn app:app --reload
```

5. Access the API:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## Deployment Options

### Option 1: Deploy to Render (Recommended - Free Tier Available)

1. Create account on [Render.com](https://render.com)

2. Create new **Web Service**:
   - Connect your GitHub repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

3. Add Environment Variable:
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key

4. Deploy!

### Option 2: Deploy to Railway

1. Create account on [Railway.app](https://railway.app)

2. Click "New Project" → "Deploy from GitHub repo"

3. Select your repository

4. Add Environment Variable:
   - `OPENAI_API_KEY`: Your OpenAI API key

5. Railway auto-detects FastAPI and deploys

### Option 3: Deploy to AWS EC2

1. Launch EC2 instance (Ubuntu 22.04)

2. SSH into instance and install dependencies:
```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

3. Clone repository and setup:
```bash
git clone https://github.com/manav-2907/smart-document-inspector.git
cd smart-document-inspector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Create `.env` file with your API key

5. Run with nohup:
```bash
nohup uvicorn app:app --host 0.0.0.0 --port 8000 &
```

6. Configure security group to allow port 8000

### Option 4: Docker Deployment

1. Build Docker image:
```bash
docker build -t doc-inspector .
```

2. Run container:
```bash
docker run -d -p 8000:8000 -e OPENAI_API_KEY=your_key_here doc-inspector
```

## Testing the API

### Using cURL:
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@receipt.jpg"
```

### Using Python:
```python
import requests

url = "http://localhost:8000/analyze"
files = {"file": open("receipt.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

### Using Postman:
1. Method: POST
2. URL: `http://localhost:8000/analyze`
3. Body: form-data
4. Key: `file` (type: File)
5. Value: Upload your document image

## Tech Stack

- **FastAPI**: Modern web framework for building APIs
- **OpenAI GPT-4 Vision**: AI model for image analysis
- **Pillow**: Image processing
- **Python 3.11**: Programming language

## Project Structure

```
smart-document-inspector/
├── app.py                 # FastAPI application
├── doc_inspector.py       # Core document analysis logic
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .env.example          # Environment variables template
├── uploads/              # Temporary upload directory
└── README.md             # This file
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## Error Handling

The API includes error handling for:
- Invalid JSON responses from OpenAI
- API request failures
- File upload errors
- Missing API keys

## Future Enhancements

- [ ] Add support for more document types
- [ ] Implement batch processing
- [ ] Add document validation
- [ ] Support for multiple languages
- [ ] OCR fallback for low-quality images
- [ ] Database integration for storing results
- [ ] User authentication and rate limiting

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

Manav Narula
- GitHub: [@manav-2907](https://github.com/manav-2907)
- LinkedIn: [manav-narula-ai](https://linkedin.com/in/manav-narula-ai)

## Acknowledgments

- OpenAI for GPT-4 Vision API
- FastAPI for the excellent framework
