from fastapi import FastAPI
from pydantic import BaseModel
from detoxify import Detoxify
from pymongo import MongoClient
import re
import emoji
import nltk
from nltk.corpus import stopwords
from bson import ObjectId  

nltk.download('stopwords')
stop_words = set(stopwords.words('french')) | set(stopwords.words('english'))

app = FastAPI()
model = Detoxify('original')
client = MongoClient("mongodb://localhost:27017/")



db = client["toxic_comments"]
collection = db["comments"]

class Comment(BaseModel):
    content: str

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.lower()

    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)


@app.post("/analyze")
def analyze_comment(comment: Comment):
    cleaned = clean_text(comment.content)
    toxicity_scores = model.predict(cleaned)
    toxicity_scores_cleaned = {k: float(v) for k, v in toxicity_scores.items()}
    result = {
        "original": comment.content,
        "cleaned": cleaned,
        "toxicity": toxicity_scores_cleaned,
    }
    inserted = collection.insert_one(result)

    # Convert ObjectId en str pour la réponse JSON
    result["_id"] = str(inserted.inserted_id)

    return result

