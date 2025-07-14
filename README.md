
# 🩺 Medical Insurance Cost Prediction

This project predicts medical insurance costs based on a user's demographic and lifestyle inputs using a trained machine learning model and a simple Streamlit web app interface.

---

## 📂 Project Structure

```
Medical_Insurance_Cost_Prediction/
│
├── app.py                   # Streamlit app file
├── model.pkl                # Trained model file
├── insurance.csv            # Dataset used for training
├── Medical_Insurance_Cost_Prediction.ipynb  # Jupyter notebook (EDA + training)
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 📌 Features

- Linear Regression model to predict insurance cost.
- Encodes categorical features like sex, smoker, region.
- Streamlit UI for input and instant prediction.
- Trained using publicly available dataset on Kaggle.

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/atulmodi1509/Medical_Insurance_Cost_Prediction.git
cd Medical_Insurance_Cost_Prediction
```

### 2. Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

Your browser will open automatically with the prediction interface.

---

## 📈 Dataset

Dataset used: [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)  
- Columns: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`

---

## 📊 Model Info

- Algorithm: `Linear Regression`
- Preprocessing: One-hot encoding for categorical variables
- Target: `charges`

---

## 🙌 Acknowledgements

- Kaggle for the dataset
- Streamlit for UI deployment
- Scikit-learn for model training

---

## 🧠 Author

- **Atul Modi**
- [Your GitHub Profile](https://github.com/atulmodi1509)
