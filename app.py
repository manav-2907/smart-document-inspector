from fastapi import FastAPI, UploadFile, File
import shutil
import os
from doc_inspector import doc_inspector

app = FastAPI(title="Smart Document Inspector API")

upload_folder = "uploads"
os.makedirs(upload_folder,exist_ok=True)

@app.get("/")
def health():
    return {"status":"running"}

@app.post('/analyze')
async def analyze_document(file:UploadFile=File(...)):
    file_path = os.path.join(upload_folder,file.filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    result = doc_inspector(file_path)

    return {"result":result}


