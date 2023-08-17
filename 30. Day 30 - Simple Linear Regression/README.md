<h1 align="center">Simple Linear Regression</h1>

<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/30.%20Day%2030%20-%20Simple%20Linear%20Regression/SLR%20Implementation.jpg" height="750px">

---

# **Linear Regression**

**Supervised machine learning algorithms:** It is a type of machine learning, where the algorithm learns from labeled data.  

* **Labeled data** means the dataset whose respective target value is already known.

* Supervised learning has two types:

  * **Classification:** It predicts the class of the dataset based on the independent input variable. Class is the categorical or discrete values. like the image of an animal is a cat or dog?

  * **Regression:** It predicts the continuous output variables based on the independent input variable. like the prediction of house prices based on different parameters like house age, distance from the main road, location, area, etc.

---

<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/30.%20Day%2030%20-%20Simple%20Linear%20Regression/download.png" width="500px">


The above diagram is an example of Simple Linear Regression, where change in the value of feature 'Y' is proportional to value of 'X'.

* **Y :** Dependent or Target Variable.

* **X :** Independent Variable.

* **Regression Line:** It is best-fit line of the model, by which we can predict value of 'Y' for new values of 'X'.

---

> **Assumption of Linear Regression:**

Linear regression makes several key assumptions about the data and the relationships it models. Violations of these assumptions can affect the validity and reliability of the regression results. Here are the main assumptions of linear regression:

* **Linearity:** The relationship between the independent variable(s) and the dependent variable is linear. This means that the change in the dependent variable for a unit change in the independent variable is constant.

* **Independence of Errors:** The errors (residuals) of the model are assumed to be independent of each other. In other words, the error of one observation should not be influenced by the errors of other observations.

* **Homoscedasticity:** Homoscedasticity refers to the assumption that the variance of the residuals is constant across all levels of the independent variables. This means that the spread of residuals should be roughly the same throughout the range of the predictor variables.

* **Normality of Errors:** The errors (residuals) should be normally distributed. This assumption is important for hypothesis testing and constructing confidence intervals.

* **No or Little Multicollinearity:** Multicollinearity occurs when two or more independent variables in the model are highly correlated. This can make it difficult to interpret the individual effects of each variable on the dependent variable.

* **No Endogeneity:** Endogeneity refers to the situation where an independent variable is correlated with the error term. This can arise due to omitted variable bias or simultaneous causation and can lead to biased and inconsistent coefficient estimates.

* **No Autocorrelation:** Autocorrelation occurs when the residuals of the model are correlated with each other. This assumption is important when dealing with time series data, where observations are dependent on previous observations.

* **Constant Variance of Residuals (Homoscedasticity):** Also known as homoscedasticity, this assumption states that the variance of the residuals is consistent across all levels of the independent variables. This is crucial for accurate hypothesis testing and confidence interval estimation.

* **No Perfect Collinearity:** Perfect collinearity exists when one independent variable can be perfectly predicted by a linear combination of other independent variables. This situation leads to a rank-deficient matrix, making it impossible to estimate unique regression coefficients.






