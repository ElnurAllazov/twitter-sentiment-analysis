def predict_sentiment(text):
    # Convert text to sequence of integers
    seq = tokenizer.texts_to_sequences([text])
    # Pad sequence to match input length
    padded = pad_sequences(seq, maxlen=max_len, padding='post', truncating='post')
    # Predict
    prediction = model.predict(padded)[0][0]
    
    # Interpret result
    if prediction > 0.5:
        return f"Positive 😊 (confidence: {prediction:.2f})"
    return f"Negative 😞 (confidence: {prediction:.2f})"

# === Run from terminal ===
if __name__ == "__main__":
    print("Twitter Sentiment Predictor (type 'quit' to exit)")
    while True:
        text = input("\nEnter a tweet: ")
        if text.lower() == "quit":
            break
        print(predict_sentiment(text))
