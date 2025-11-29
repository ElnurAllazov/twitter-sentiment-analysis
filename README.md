# Twitter Sentiment Analysis  

Deep Learning model for sentiment analysis of tweets using **Bidirectional LSTM**.

---

## 📊 Model Performance
- **Test Accuracy:** 82%
- **Training Accuracy:** 88%
- **Dataset:** Sentiment140 (1.6M tweets)
- **Architecture:** Bi-LSTM with embeddings



## 🧠 Model Summary



---

## 🔧 Hyperparameters

| Parameter | Value |
|----------|-------|
| Vocabulary Size | 10,000 words |
| Sequence Length | 100 tokens |
| Embedding Dimension | 64 |
| LSTM Units | 128 (→ 256 Bi-LSTM) |
| Dropout Rate | 0.3 |
| Learning Rate | 0.0005 |
| Batch Size | 128 |
| Optimizer | Adam |

---

## 📈 Training Details

### Dataset
[Sentiment140 (1.6M tweets)](https://www.kaggle.com/datasets/kazanova/sentiment140)  
- 800K negative tweets  
- 800K positive tweets  

### Train/Test Split
- 80% training  
- 20% testing  

### Preprocessing Steps
- Lowercase conversion  
- URL removal  
- Mention removal (@username)  
- Special character removal *(except ! and ?)*  
- Whitespace normalization  







