import requests
import base64
import json
from PIL import Image
import io
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

prompt = """
You are a Document Understanding AI. Your job is to analyze a document image and extract structured data.
You must:
1) Detect the document type
2) Extract fields using the correct schema
3) Return strictly valid JSON only

Document Type : [receipt, invoice, id_card, prescription, other] (choose any 1)

STRICT OUTPUT RULES
- Give output only in valid json
- No markdown, explanations, extra text, comments, trailing commas, additional keys.
- If a field is not found -> return null
- If document type cannot be determined -> use "other"
- Dates: use YYYY-MM-DD if clear, otherwise keep original text
- Amounts: include currency symbol if visible (₹, $, etc)
- Medicines must be an array of strings
- In summary give what is written in the document and what is it about.

FIELD EXTRACTION PRIORITY
Ignore logos, decorative text, watermarks, QR codes, barcodes (unless readable text)

OUTPUT SCHEMA SELECTION
Return ONLY the schema matching the detected document type.

RECEIPT SCHEMA
{
"document_type": "receipt",
"store_name": "",
"date": "",
"total_amount": "",
"tax": "",
"payment_method": "",
"summary": ""
}

INVOICE SCHEMA
{
"document_type": "invoice",
"invoice_number": "",
"seller": "",
"buyer": "",
"date": "",
"total_amount": "",
"gst_number": "",
"summary": ""
}

ID CARD SCHEMA
{
"document_type": "id_card",
"name": "",
"date_of_birth": "",
"id_number": "",
"address": "",
"issuer": "",
"summary": ""
}

PRESCRIPTION SCHEMA
{
"document_type": "prescription",
"patient_name": "",
"doctor_name": "",
"hospital": "",
"date": "",
"medicines": [],
"summary": ""
}

OTHER SCHEMA
{
"document_type": "other",
"summary": ""
}

FINAL INSTRUCTION
Analyze the provided document image and return ONLY the JSON output following the rules above.
"""

def doc_inspector(img_path):
    img = Image.open(img_path).convert("RGB")
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-5.2",
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        'type': 'input_text',
                        "text": prompt
                    },
                    {
                        'type': 'input_image',
                        'image_url': f"data:image/jpeg;base64,{image_base64}"
                    }
                ]
            }
        ],
        "temperature": 0
    }

    response = requests.post(url="https://api.openai.com/v1/responses", headers=headers, json=payload)
    resp = response.json()
    raw = resp["output"][0]["content"][0]["text"]
    try:
        # Strip markdown code fences if present
        clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        data = json.loads(clean)
    except:
        print("Model returned invalid JSON")
        print(raw)
        data = None

    return data

# if __name__ == "__main__":
#     doc_inspector('reciept.jpg')
