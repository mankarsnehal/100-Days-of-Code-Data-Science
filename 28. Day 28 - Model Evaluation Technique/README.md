



<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/28.%20Day%2028%20-%20Model%20Evaluation%20Technique/evaluation.png">


## 1. Accuracy:

Accuracy measures the ratio of correctly predicted instances to the total instances. It's suitable for balanced datasets but can be misleading for imbalanced ones.

## 2. Precision:
Precision measures the proportion of correctly predicted positive instances out of all instances predicted as positive. It's important when false positives are costly.

## 3. Recall (Sensitivity or True Positive Rate):
Recall measures the proportion of correctly predicted positive instances out of all actual positive instances. It's important when false negatives are costly.

## 4. F1-Score:
F1-score is the harmonic mean of precision and recall. It balances precision and recall, making it useful when you want to consider both false positives and false negatives.

## 5. Specificity (True Negative Rate):
Specificity measures the proportion of correctly predicted negative instances out of all actual negative instances.

## 6. ROC Curve (Receiver Operating Characteristic):
The ROC curve visualizes the tradeoff between true positive rate (recall) and false positive rate as the classification threshold changes.

## 7. AUC (Area Under the ROC Curve):
AUC quantifies the area under the ROC curve. It's a single value that measures the model's ability to distinguish between classes.

## 8. Confusion Matrix:
A confusion matrix displays the counts of true positives, true negatives, false positives, and false negatives. It's useful for understanding model performance in classification tasks.

## 9. Mean Squared Error (MSE):
MSE measures the average squared difference between predicted and actual values in regression tasks. It quantifies the model's predictive accuracy.

## 10. Root Mean Squared Error (RMSE):
RMSE is the square root of MSE. It's more interpretable as it's in the same unit as the target variable.

## 11. R-squared (Coefficient of Determination):
R-squared measures the proportion of the variance in the dependent variable that's explained by the model. It assesses the model's goodness of fit.

## 12. Mean Absolute Error (MAE):
MAE calculates the average absolute difference between predicted and actual values. It's another metric for evaluating regression models.

## 13. Cross-Validation:
Cross-validation involves dividing the dataset into multiple subsets and training/evaluating the model on different combinations of training and test sets. It provides more robust performance estimates.

## 14. Stratified K-Fold Cross-Validation:
Similar to k-fold cross-validation, but ensures that class proportions are maintained in each fold for classification tasks.

## 15. Bias-Variance Tradeoff Analysis:
Analyzes the tradeoff between bias (simplification) and variance (flexibility) in models. It helps understand whether a model is underfitting or overfitting.

## 16. Learning Curves:
Learning curves show how model performance changes with the size of the training data. They help diagnose underfitting or overfitting.

## 17. Feature Importance Analysis:
Identifies the importance of each feature in influencing model predictions. Useful for understanding feature relevance and potential model improvements.

## 18. Residual Analysis:
In regression tasks, residual analysis examines the patterns in the model's errors (residuals) to check for any systematic deviations.

## 19. Hyperparameter Tuning:
Adjusting hyperparameters to optimize model performance. Techniques include grid search, random search, and Bayesian optimization.

## 20. Ensemble Methods:
Using combinations of multiple models to improve overall predictive performance. Techniques include bagging, boosting, and stacking.

## 21. Domain-Specific Metrics:
Some domains have specialized evaluation metrics. For example, Mean Average Precision (MAP) in information retrieval or Gini coefficient in economics.
