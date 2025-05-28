# qa_engine/model_handler.py

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
# import torch
import os

# Cache tokenizer and model globally
# _tokenizer = None
# _model = None
_qa_pipeline = None


# def load_model():
#     global _tokenizer, _model
#     if _tokenizer is None or _model is None:
#         model_path = os.path.join("local_model", "model")
#         tokenizer_path = os.path.join("local_model", "tokenizer")
#         _tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
#         _model = AutoModelForQuestionAnswering.from_pretrained(model_path)
#     return _tokenizer, _model

def load_model():
    global _qa_pipeline
    if _qa_pipeline is None:
        print("🔄 Loading model and tokenizer...")
        model_path = os.path.join("local_model", "model")
        tokenizer_path = os.path.join("local_model", "tokenizer")
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        model = AutoModelForQuestionAnswering.from_pretrained(model_path)
        _qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
    return _qa_pipeline

def get_answer(context: str, question: str) -> str:
    qa = load_model()
    try:
        result = qa(question=question, context=context)
        return result["answer"]
    except Exception as e:
        return f"பிழை: {str(e)}"