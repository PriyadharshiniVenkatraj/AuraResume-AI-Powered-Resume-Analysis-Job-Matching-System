import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset.csv")

# Clean column names (important)
df.columns = df.columns.str.strip()

# Combine useful columns into one text input
X = df["Skills"] + " " + df["Education"] + " " + df["YearsExperience"].astype(str)
y = df["JobRole"]

# Convert text to vectors
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split data (VERY IMPORTANT for real accuracy)
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Train models
lr = LogisticRegression(max_iter=1000)
nb = MultinomialNB()

lr.fit(X_train, y_train)
nb.fit(X_train, y_train)

# Evaluate models
lr_acc = lr.score(X_test, y_test)
nb_acc = nb.score(X_test, y_test)

# Plot comparison
models = ["Logistic Regression", "Naive Bayes"]
accuracy = [lr_acc, nb_acc]

plt.figure()
plt.bar(models, accuracy)
plt.title("Model Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.show()

# Print accuracy
print("Logistic Regression Accuracy:", lr_acc)
print("Naive Bayes Accuracy:", nb_acc)
plt.figure()
df["JobRole"].value_counts().plot(kind="bar")
plt.title("Job Role Distribution")
plt.xlabel("Job Role")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
plt.figure()
plt.hist(df["YearsExperience"], bins=10)
plt.title("Years of Experience Distribution")
plt.xlabel("YearsExperience")
plt.ylabel("Frequency")
plt.show()
plt.figure()
df.boxplot(column="YearsExperience", by="JobRole")
plt.title("Experience vs Job Role")
plt.suptitle("")
plt.xlabel("Job Role")
plt.ylabel("YearsExperience")
plt.xticks(rotation=45)
plt.show()