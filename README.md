
# Hi, I'm Narapureddy Durga Prasad Reddy! 👋

Diabetes is a prevalent chronic condition that affects millions of people worldwide. Early detection can significantly improve treatment outcomes and quality of life for patients. By leveraging machine learning, this project seeks to:

* Aid healthcare professionals in early diagnosis.

* Enhance the efficiency of medical decision-making processes.

* Provide researchers with data-driven insights into diabetes risk factors.

To solve this challenge, SugarScope, a diabetes prediction model, has been developed. By leveraging machine learning, SugarScope aims to aid in early diagnosis, enhance medical decision-making efficiency, and provide researchers with valuable insights into diabetes risk factors.
# SugarScope - Diabetes Prediction Website

This project is focused on predicting the likelihood of diabetes in patients based on medical and demographic data. Using machine learning models, we aim to assist healthcare professionals in identifying patients at risk of developing diabetes and provide valuable insights for personalized treatment plans. The project also explores relationships between various factors and diabetes, which can be instrumental for researchers in understanding the disease.


## About the Dataset

The Diabetes Prediction dataset contains medical and demographic information of 100,000 patients, including the following features:

* Age
* Gender
* Body Mass Index (BMI)
* Hypertension
* Heart Disease
* Smoking History
* HbA1c Level
* Blood Glucose Level

The dataset also includes the diabetes status of each patient (positive or negative), making it well-suited for classification tasks. Specifically:

Diabetic Instances: 8,500
Non-Diabetic Instances: 91,500
Preprocessing steps included handling missing values, encoding categorical variables, and normalizing numerical features to ensure the dataset is ready for machine learning modeling.

# Project Workflow

## Data Exploration

* Conducted univariate, bivariate, and multivariate analyses.

* Visualized feature distributions, relationships, and correlations.

## Preprocessing

* Handled missing values using the forward-fill method.

* Encoded categorical variables (e.g., gender and smoking history).

* Scaled numerical features for uniformity.

## Feature Engineering

Selected key features: age, hypertension, heart disease, BMI, HbA1c level, blood glucose level, smoking history, and gender.
## Model Training and Evaluation

Trained and compared various machine learning models, including:

- Logistic Regression

- Random Forest

- Gradient Boosting

- Support Vector Machine (SVM)

- XGBoost

- AdaBoost

- Bagging

- Decision Tree

- K-Nearest Neighbors (KNN)

- Voting Classifier


## Visualization

- plotted graphs for statistical information of dataset

- Plotted confusion matrices and correlation matrices.

- Analyzed model performance through comparative visualizations.
# Key Findings

## Best Models

* ### Gradient Boosting - With an accuracy of 97.25%, our results showed that the Gradient Boosting model produced the best results.

* ### Decision Tree: With a ROC-AUC score of 0.8556, the Decision Tree model outperformed the others.

* ### AdaBoost, XGBoost, and Bagging Classifier: A well-balanced performance was also offered by these models, with ROC-AUC scores ranging from 0.8453 to 0.8470 and accuracies between 96.85% and 97.21%.

## Deployment

The Gradient Boosting model was deployed using Flask and hosted on the Render platform, making it accessible as a web application.

To access the website, use the link https://sugarscope.onrender.com/.


## 🛠 Skills

**Backend:**
* Python
* Flask (API development)
* Pandas, NumPy (data processing)
* Scikit-learn, XGBoost, LightGBM (machine learning)

**Frontend:**
* HTML, CSS, JavaScript
* Bootstrap (UI framework)

**Deployment:**
* Render (hosting)




## API Reference

#### Endpoint
* URL: /predict 
* Request Type: POST

```http
  Parameters
```

| Parameter              | Type     | Description                |
| :--------              | :------- | :------------------------- |
| `age`                  | `int`    | Age of the individual |
| `gender`               | `int`    | Gender of the individual                         |
| `bmi`                  | `float`  | Body Mass Index                           |
| `hypertension`         | `int`    | Hypertension status (True/False)                           |
| `heart_disease`        | `int`    | Heart disease status (True/False)                           |
| `smoking_history`      | `int`    | Smoking history                           |
| `hba1c_level`          | `float`  | HbA1c level                           |
| `blood_glucose_level`  | `float`  | Blood glucose level                           |



```http
  Response
```

| Field     | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `diabetes_risk`      | `string` | Risk classification (e.g., diabetic or non-diabetic) |



## Usage/Examples

    1. Input patient data through the web application.

    2. The model predicts whether the patient is at risk of developing diabetes.


## Conclusion

This project demonstrates the potential of machine learning in medical diagnostics. By automating diabetes risk prediction, the solution can:

* Save time for healthcare providers.

* Enable early intervention for at-risk patients.

* Provide a foundation for further research into chronic disease management.


## Feedback

If you have any feedback, please reach out to us at narapureddydurgaprasad818@gmail.com


## Acknowledgements

We thank the contributors and maintainers of the dataset and the tools used in this project for enabling this work.



