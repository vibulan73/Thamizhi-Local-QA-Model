# download_model.py
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import os
from dotenv import load_dotenv
# from huggingface_hub import snapshot_download

# Load .env variables
load_dotenv()

model_name = "RajeevanL/tamil-distilled-roberta-v3"
# Get token from .env
access_token = os.getenv("hf_token")


tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
model = AutoModelForQuestionAnswering.from_pretrained(model_name, token=access_token)

tokenizer.save_pretrained("local_model/tokenizer")
model.save_pretrained("local_model/model")

print("✅ Model downloaded and saved locally.")