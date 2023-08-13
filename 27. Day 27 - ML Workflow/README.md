<h1 align="center">Machine Learning Workflow</h1>

<img src ="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/27.%20Day%2027%20-%20ML%20Workflow/Machine_Learning_Workflow_page-0001.jpg" height = "750">

---

## Data Preprocessing:
Data preprocessing is a crucial step in the machine learning workflow. It involves cleaning, transforming, and preparing the raw data to make it suitable for training and evaluating machine learning models. Some common tasks in data preprocessing include:

- **Data Cleaning:** Handling missing values, outliers, and inconsistencies in the data.
- **Feature Selection/Extraction:** Choosing relevant features or creating new features from existing ones to improve model performance.
- **Normalization/Scaling:** Scaling numerical features to the same range to prevent features with larger values from dominating the learning process.
- **Encoding Categorical Variables:** Converting categorical variables into numerical representations (e.g., one-hot encoding) that can be used by the model.
- **Splitting Data:** Dividing the dataset into training, validation, and test sets. The training set is used for model training, the validation set helps tune hyperparameters, and the test set evaluates the final model's performance.


## Model Training:
Model training involves feeding the preprocessed data into a machine learning algorithm to learn patterns and relationships from the data. The goal is for the model to capture these patterns and make accurate predictions on new, unseen data. The process includes the following steps:

- **Selecting a Model:** Choose an appropriate machine learning algorithm based on the problem type (e.g., classification, regression) and the characteristics of the data.
- **Initializing Parameters:** Initialize the model's parameters or weights.
- **Training Loop:** Feed the training data into the model iteratively, adjusting the model's parameters to minimize a chosen loss function that quantifies the difference between predicted and actual values.
- **Gradient Descent (for Optimization):** Many machine learning algorithms use gradient descent or its variants to update model parameters in the direction that reduces the loss function.
- **Hyperparameter Tuning:** Tune hyperparameters (parameters not learned during training) to optimize model performance. This can be done using techniques like grid search or random search.


## Model Evaluation:
Once the model is trained, it's essential to assess its performance to determine how well it will perform on new, unseen data. Evaluation methods vary based on the problem type and the nature of the data. Common evaluation techniques include:

- **Metrics:** Use appropriate evaluation metrics such as accuracy, precision, recall, F1-score for classification; mean squared error (MSE), root mean squared error (RMSE) for regression, etc.
- **Cross-Validation:** Perform cross-validation to get a more robust estimate of the model's performance by splitting the data into multiple train-test folds.
- **Confusion Matrix:** Especially useful for classification problems, it helps visualize the model's performance in terms of true positives, true negatives, false positives, and false negatives.
- **ROC and AUC:** Receiver Operating Characteristic (ROC) curve and Area Under the Curve (AUC) provide insight into a model's ability to distinguish between classes in classification tasks.
- **Overfitting and Underfitting:** Analyze whether the model is overfitting (performing well on training data but poorly on new data) or underfitting (performing poorly on both training and new data).

