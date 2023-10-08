
from fastapi import FastAPI
from google.transliteration import transliterate_word

app = FastAPI(
    title="NLP Based Project",
    description="This is an API that generates NLP variations in hindi specially for name matching",
    version="2.5.0",
)


@app.get("/")
def home():
    return {"Data": "Home Page"}

@app.get("/get_NLP_Variations/{namebyeng},{namebyhindi}")
def get_NLP_Variations(namebyeng: str,namebyhindi:str):
    word=namebyeng.strip()
    suggestions = transliterate_word(word, lang_code='hi')
    a=namebyhindi.strip()
    if a in suggestions :
        return{"Data":"Matched","Variations":suggestions}
    else :
        return{"Data":"Not Matched"}


