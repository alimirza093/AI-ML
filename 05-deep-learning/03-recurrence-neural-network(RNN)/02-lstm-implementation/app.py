from pathlib import Path
import pickle

import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

BASE_DIR = Path(__file__).resolve().parent

# ------------------------------
# Load saved files
# ------------------------------
@st.cache_resource
def load_resources():
    model_path = BASE_DIR / "lstm_model.h5"
    tokenizer_path = BASE_DIR / "tokenizer.pkl"
    max_len_path = BASE_DIR / "max_len.pkl"

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    if not tokenizer_path.exists():
        raise FileNotFoundError(f"Tokenizer file not found: {tokenizer_path}")
    if not max_len_path.exists():
        raise FileNotFoundError(f"max_len file not found: {max_len_path}")

    model = load_model(model_path)
    with tokenizer_path.open("rb") as f:
        tokenizer = pickle.load(f)
    with max_len_path.open("rb") as f:
        max_len = pickle.load(f)
    return model, tokenizer, max_len

model, tokenizer, max_len = load_resources()

# ------------------------------
# Prediction function
# ------------------------------
def predict_next_line(text, max_words=12):
    if not text or not text.strip():
        return ""

    generated_text = text.strip()

    for _ in range(max_words):
        sequence = tokenizer.texts_to_sequences([generated_text])[0]
        if len(sequence) > max_len:
            sequence = sequence[-max_len:]

        padded_sequence = pad_sequences([sequence], maxlen=max_len, padding='pre')
        preds = model.predict(padded_sequence, verbose=0)
        predicted_index = int(np.argmax(preds))
        next_word = tokenizer.index_word.get(predicted_index, "")

        if not next_word or next_word == "<PAD>":
            break

        generated_text = f"{generated_text} {next_word}".strip()

        if next_word.endswith((".", "!", "?")):
            break

    return generated_text

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="Next Line Prediction", layout="centered")

st.title("🧠 Next Line Prediction (LSTM)")
st.write("Enter a sentence and the model will generate the **next line**.")

user_input = st.text_input("✍️ Enter text:", placeholder="Type a sentence here...")

if st.button("Predict Next Line"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        predicted_line = predict_next_line(user_input)
        st.success(f"**Predicted Next Line:** {predicted_line}")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("LSTM-based Next Line Prediction using Streamlit")