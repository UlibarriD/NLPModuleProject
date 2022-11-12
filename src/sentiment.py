# Import dependecies
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained(
    'nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained(
    'nlptown/bert-base-multilingual-uncased-sentiment')

def sentimentCalculator(phrase):
    tokens = tokenizer.encode(phrase, return_tensors='pt')
    result = model(tokens)
    rating = int(torch.argmax(result.logits)) + 1
    return "POSITIVE" if rating > 3 else "NEGATIVE"
