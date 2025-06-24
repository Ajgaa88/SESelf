from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Орчуулгын загвар: Англиас Франц (эсвэл сольж болно)
translator = pipeline("translation_en_to_fr")  

class InputText(BaseModel):
    text: str

@app.post("/translate/")
def translate_text(data: InputText):
    result = translator(data.text)
    return {"translated": result[0]['translation_text']}
