# LinkedIn Post Impression Predictor 🚀

This is a simple Machine Learning mini-project I created to predict how many impressions a LinkedIn post will get in its first 24 hours. I built it using Python and Scikit-learn to practice building and evaluating Linear Regression models.

## How it Works
I built a Command Line Interface (CLI) where you can paste your drafted LinkedIn post. The Python script automatically scans the text and extracts the features:
1. **Word count** (measuring dwell time)
2. **Number of hashtags** (measuring keyword reach)
3. **Hour posted** (0-23, to factor in audience timing)

The model takes these 3 inputs and predicts the Day 1 impressions.

## Model Performance
I trained the model on a mock dataset of 100+ LinkedIn posts (`linkedin_data.csv`). 

* **R-squared (R²) Score:** 0.86 
* **Mean Absolute Error (MAE):** 437.67 impressions
* **Root Mean Squared Error (RMSE):** 559.81 impressions

![Actual vs Predicted](Actual_VS_Predicted.png)
*(The visualization above shows my test data predictions closely following the perfect accuracy line).*

## 💡 A Cool ML Lesson I Learned
I tested this model on my real "25 DSA Patterns" post. The CLI predicted **1,501 views** for the first day. 

This was actually a highly accurate prediction for standard linear growth! However, because I attached a useful PDF cheat sheet, people started sharing it, and the post entered a viral loop—reaching **21,000+ views** over 7 days. 

**My biggest takeaway:** Linear regression is great at predicting normal, everyday network growth. But it mathematically cannot predict the exponential spikes (power-law curves) that happen when a high-value asset gets shared repeatedly. 

## How to Run It Locally
If you want to test the model yourself:

1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install pandas scikit-learn matplotlib
