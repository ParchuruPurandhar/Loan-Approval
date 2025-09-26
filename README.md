# Loan-Approval
This is a simple ML and Data Science based project that is used to predict the approval of loan 
1. EDA and Visualization
⫸ Data Set Overview
   » Shape: 10,000 rows × 21 columns

   » Target column: target_default_risk
⫸ Missing Values
   » Present in: income, savings, credit_score, monthly_expenses

   » Missingness of the values is not extreme (mostly <5%)
⫸ Target Balance
   »target_default_risk:
        ◊ 1 → ~51%
        ◊ 0 → ~49%
⫸ Skewness Summary
Skewness tells us if a distribution is symmetric (≈0), right-skewed (>0), or left-skewed (<0).
    ● Highly right-skewed:
        loan_amount , monthly_expenses , recent_default , savings , income
    ● Moderate right-skewed:
        debt_to_income , num_dependents  , employment_years
    ● Nearly symmetric:
        age , credit_score , signup_dayofweek.
    ● Left-skewed:
        loan_term_months , has_credit_card
From this We can observe that age and credit_score is in Normal Distribution and signup days of week is in uniform distribution
⫸ Outliers
    ● Outliers are data points that differ greatly from the majority of observations.
    ● In models like (SVM, Logistic Regression), they can distort model performance ,Tree-based models (Decision Tree, Random Forest, XGBoost) are less sensitive to outliers.
    ● The Boxplot is used to find the outliers in the data set , from our box plots we can see that there are various no of outliers are present in our dataset.We need to remove or use some other techniques to manage them
    ● It is necessary for some models to manage outliers to build a better model
⫸ Correlation in Our Dataset
    ● Strong positive correlation: income «–» target_default_risk.
    ● Moderate negative correlation: debt_to_income «–» target_default_risk .
    ● Moderate positive correlation: income «–» savings .
    ● other features had weak correlations with the target.
Ⅱ. Data Preprocessing
Steps Followed in Preprocessing
 ▶ Categories Typos :
         The Typos in Categorical features can be handled by using replace function
 ▶ Outlier treatment :
        The outliers are treated using the caping technique
 ▶ Feature engineering:
        signup_recency_days from signup_date for getting better accuracy
 ▶ Handling Null Values :
        The percentile of null values is small , so we are going to use Simple Imputer
 ▶ Scaling :
        The values are scaled to smallest values within the range of Standard Scaler Using the Standard Scaler
 ▶ Ordinal Encoding :
        The Ordinal type of features in our dataset can be converted into ML Model Understandable language using ordinal encode
 ▶ One Hot Encoding :
        The Data of Nominal type is converted by using the technique called one hot Encoder
Ⅲ . Model Building and Evaluation
▶ Involves creating Different type of machine learning models and training that models with the training data that we split before
▶ The Models we are going to train and build are :
    ◊ Logistic Regression
    ◊ RandomForestClassifier
    ◊ Decision Tree
    ◊ SVM
    ◊ XGBoost
▶ After completion of Building of the model and training the model. we need to predict the output and evaluate that model by using different metrics
    ◊ accuracy
    ◊ precision
    ◊ recall
    ◊ F1-score
    ◊confusion matrix
