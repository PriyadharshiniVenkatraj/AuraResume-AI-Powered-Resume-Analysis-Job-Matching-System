import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load dataset
df = pd.read_csv("dataset.csv")

# Split data
X = df["resume_text"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Predictions
y_pred = model.predict(X_vec)

# -----------------------------
# 1. Label Distribution Graph
# -----------------------------
plt.figure()
df["label"].value_counts().plot(kind="bar")
plt.title("Label Distribution")
plt.xlabel("Class (0 = Not Suitable, 1 = Suitable)")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 2. Confusion Matrix
# -----------------------------
cm = confusion_matrix(y, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.show()

# -----------------------------
# 3. Top Features Graph
# -----------------------------
feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

top_indices = coefficients.argsort()[-10:]

plt.figure()
plt.barh([feature_names[i] for i in top_indices], coefficients[top_indices])
plt.title("Top Important Skills")
plt.xlabel("Weight")
plt.show()

# -----------------------------
# 4. Word Count Distribution
# -----------------------------
word_counts = df["resume_text"].apply(lambda x: len(x.split()))

plt.figure()
word_counts.plot(kind="hist")
plt.title("Resume Word Count Distribution")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 5. Model Accuracy Display
# -----------------------------
accuracy = model.score(X_vec, y)
print("Model Accuracy:", accuracy)