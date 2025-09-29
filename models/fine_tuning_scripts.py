# models/fine_tuning_scripts.py
from transformers import Trainer, TrainingArguments
import torch
from datasets import Dataset
import json

def load_training_data():
    with open('data/custom_chat_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    formatted_data = []
    for conv in data:
        text = ""
        for msg in conv["conversations"]:
            if msg["from"] == "human":
                text += f"User: {msg['value']}\n"
            else:
                text += f"Assistant: {msg['value']}\n"
        formatted_data.append({"text": text.strip()})
    
    return Dataset.from_list(formatted_data)

def start_fine_tuning():
    # Fine-tuning 
    print("🚀 Fine-tuning starting...")