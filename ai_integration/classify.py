from transformers import pipeline
import pandas as pd
from tabulate import tabulate

# 🔹 Model Load karein (Best Accuracy)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# 🔹 Sentences ka List (Example)
sentences = [
    "I love this AI tool, it's very useful!",
    "The weather is okay today.",
    "I hate getting stuck in traffic.",
    "This product is neither good nor bad.",
    "I'm excited about the new iPhone launch!",
    "The food at the restaurant was terrible.",
    "This movie was an absolute masterpiece!",
    "I don't know how to feel about this.",
]

# 🔹 Labels (Categories)
candidate_labels = ["positive", "negative", "neutral"]

# 🔹 Results Store karne ke liye List
results = []

for sentence in sentences:
    prediction = classifier(sentence, candidate_labels)
    label = prediction['labels'][0]  # Best Label
    confidence = round(prediction['scores'][0] * 100, 2)  # Confidence %
    results.append([sentence, label, confidence])

# 🔹 DataFrame Create karein
df = pd.DataFrame(results, columns=["Sentence", "Predicted Label", "Confidence (%)"])

# 🔹 CSV File Save karein
csv_filename = "classification_results.csv"
df.to_csv(csv_filename, index=False)

# 🔹 Terminal Output Print karein (Table Format)
print("\n🔹 **Classification Results:**")
print(tabulate(df, headers="keys", tablefmt="grid"))

print(f"\n✅ Results successfully saved in `{csv_filename}`")
