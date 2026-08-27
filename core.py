import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load the Data (Swap out for cloud_billing.csv when ready)
df = pd.read_csv('linkedin.csv')

# 2. Define Features (X) and Target (y)
X = df[['word_count', 'hashtags', 'hour_posted']]
y = df['impressions']

# 3. Split and Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)


# 4. Evaluate the Model
predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print(f"\n--- Model Trained! ---")
print(f"R² Score: {r2:.2f}")
print(f"MAE: {mae:.2f} impressions")
print(f"RMSE: {rmse:.2f} impressions\n")


# 5. The Command Line Interface (CLI)
print(" ============ LinkedIn Impression Predictor CLI ============ \n")

# Multi-line input for the post content
print("Paste your post content below.")
print("When you are finished, type the word ( DONE ) on a new empty line and press Enter:")
lines = []
while True:
    line = input()
    # Stop reading only if the user types 'DONE'
    if line.strip().upper() == "DONE":
        break
    lines.append(line)

# Join the lines into one big string
full_post_content = " ".join(lines)
words_list = full_post_content.split()

# 1. Automatically calculate word count
calculated_words = len(words_list)

# 2. Automatically find and count hashtags
# Changed to look for '#' anywhere in the word to catch 'hashtag#DSA'
hashtags_list = [word for word in words_list if '#' in word]
calculated_tags = len(hashtags_list)

# 3. Only ask for the hour!
hour = float(input("\nEnter hour posted (0-23): "))

# Format input for prediction
user_data = pd.DataFrame([[calculated_words, calculated_tags, hour]], columns=['word_count', 'hashtags', 'hour_posted'])
predicted_views = model.predict(user_data)[0]

print("\n--- Results ---")
print(f"📊 Words detected: {calculated_words}")
print(f"🏷️ Hashtags detected: {calculated_tags}")
print(f"🚀 Predicted Impressions (First 24 Hours) : {int(predicted_views)}")


