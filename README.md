# 📩 Spam Message Detection (Experimental Mini Project)

## 🚀 Project Overview

This project is a **Spam Message Detection System** built using the **Multinomial Naive Bayes algorithm**.

⚠️ **Important Note:**
This is an **experimental mini-project** created to evaluate how well **Naive Bayes performs on an imbalanced dataset**, even **without heavy NLP preprocessing techniques**.

---

## 🎯 Objective

The main goal of this project is to analyze:

* Performance of **Naive Bayes on imbalanced data**
* Effectiveness **without advanced NLP preprocessing**

---

## 📊 Dataset Details

* Total Data Points: **5572**
* Not Spam (Ham): **4825**
* Spam: **747**

➡️ The dataset is **highly imbalanced**, making it a good test case for evaluating model robustness.

---

## 🧠 Key Experiment Insight

Unlike typical NLP pipelines, this project intentionally:

* ❌ Does **NOT heavily rely on preprocessing techniques** such as:

  * TF-IDF Vectorization
  * Stopword removal
  * Punctuation removal
  * Stemming/Lemmatization

* ✅ Uses a **basic CountVectorizer approach**

👉 Despite minimal preprocessing, the model still achieves:

**✅ Accuracy: 98.92%**

This demonstrates the surprising effectiveness of **Multinomial Naive Bayes** for text classification tasks.

---

## 🧠 Model Details

* **Algorithm:** Multinomial Naive Bayes
* **Feature Extraction:** Count Vectorizer
* **Accuracy:** 98.92%

---

## ⚙️ Technologies & Libraries Used

| Library          | Purpose                     |
| ---------------- | --------------------------- |
| **Pandas**       | Data preprocessing          |
| **Scikit-learn** | Model training & evaluation |
| **Joblib**       | Model saving/loading        |
| **Streamlit**    | UI & deployment             |

---

## 🔄 Workflow

1. Load dataset using Pandas
2. Minimal text preprocessing
3. Convert text to vectors using CountVectorizer
4. Train model using Multinomial Naive Bayes
5. Evaluate performance
6. Save model using Joblib
7. Deploy using Streamlit

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/spam-detector.git
cd spam-detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
spam-detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── spam.csv
├── requirements.txt
└── README.md
```

---

## 📌 Features

* Simple and lightweight model
* Works well even on imbalanced dataset
* Minimal preprocessing required
* Interactive UI using Streamlit

---

## 🧪 Example

**Input:**

```
"Congratulations! You have won a free lottery ticket"
```

**Output:**

```
Spam
```

---

## 📈 Key Takeaway

This project shows that:

> Even with **imbalanced data** and **minimal NLP preprocessing**,
> **Naive Bayes can still deliver strong performance** in text classification tasks.

---

## 🌐 Deployment

Can be deployed on:

* Streamlit Cloud
* Render
* Railway

---

## 👨‍💻 Author

Developed by **Shrey**

---

⭐ If you found this experiment interesting, consider giving it a star!
