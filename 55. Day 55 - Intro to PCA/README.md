<h1 align="center">Principal Component Analysis (PCA)</h1>

- Principal Component Analysis is an unsupervised learning algorithm that is used for the dimensionality reduction in Machine Learning.

- It is a statistical process that converts the observations of correlated features into a set of linearly uncorrelated features with the help of orthogonal transformation. These new transformed features are called the **Principal Components**.

- It is one of the popular tools that is used for exploratory data analysis and predictive modeling.

- Some real-world applications of PCA are **image processing, movie recommendation system, optimizing the power allocation in various communication channels**.


### **PCA algorithm is based on some mathematical concepts such as :**
  - Variance and Covariance
  - Eigenvalues and Eigen factors

---

### **Some common terms used in PCA algorithm :**
  - **Dimensionality:** It is the number of features or variables present in the given dataset. More easily, it is the number of columns present in the dataset.
  - **Correlation:** It signifies that how strongly two variables are related to each other. Such as if one changes, the other variable also gets changed. The correlation value ranges from -1 to +1. Here, -1 occurs if variables are inversely proportional to each other, and +1 indicates that variables are directly proportional to each other.
  - **Orthogonal:** It defines that variables are not correlated to each other, and hence the correlation between the pair of variables is zero.
  - **Eigenvectors:** If there is a square matrix M, and a non-zero vector v is given. Then v will be eigenvector if Av is the scalar multiple of v.
  - **Covariance Matrix:** A matrix containing the covariance between the pair of variables is called the Covariance Matrix.

---

### **Uses of PCA :**
  PCA is a widely used technique in data analysis and has a variety of applications, including:

- **Data compression:** PCA can be used to reduce the dimensionality of high-dimensional datasets, making them easier to store and analyze.
- **Feature extraction:** PCA can be used to identify the most important features in a dataset, which can be used to build predictive models.
- **Visualization:** PCA can be used to visualize high-dimensional data in two or three dimensions, making it easier to understand and interpret.
- **Data pre-processing:** PCA can be used as a pre-processing step for other machine learning algorithms, such as clustering and classification.

---

### **Advantages of Principal Component Analysis :**

- **Dimensionality Reduction:** Principal Component Analysis is a popular technique used for dimensionality reduction, which is the process of reducing the number of variables in a dataset. 
- **Feature Selection:** Principal Component Analysis can be used for feature selection, which is the process of selecting the most important variables in a dataset. This is useful in machine learning, where the number of variables can be very large, and it is difficult to identify the most important variables.
- **Data Visualization:** Principal Component Analysis can be used for data visualization. By reducing the number of variables, PCA can plot high-dimensional data in two or three dimensions, making it easier to interpret.
- **Multicollinearity:** Principal Component Analysis can be used to deal with multicollinearity, which is a common problem in a regression analysis where two or more independent variables are highly correlated. PCA can help identify the underlying structure in the data and create new, uncorrelated variables that can be used in the regression model.
- **Noise Reduction:** Principal Component Analysis can be used to reduce the noise in data. By removing the principal components with low variance, which are assumed to represent noise, Principal Component Analysis can improve the signal-to-noise ratio and make it easier to identify the underlying structure in the data.
- **Data Compression:** Principal Component Analysis can be used for data compression. By representing the data using a smaller number of principal components, which capture most of the variation in the data, PCA can reduce the storage requirements and speed up processing.
- **Outlier Detection:** Principal Component Analysis can be used for outlier detection. Outliers are data points that are significantly different from the other data points in the dataset. Principal Component Analysis can identify these outliers by looking for data points that are far from the other points in the principal component space.

---

### **Limitations of Principal Component Analysis :**

- **Interpretation of Principal Components:** The principal components created by Principal Component Analysis are linear combinations of the original variables, and it is often difficult to interpret them in terms of the original variables. This can make it difficult to explain the results of PCA to others.
- **Data Scaling:** Principal Component Analysis is sensitive to the scale of the data. If the data is not properly scaled, then PCA may not work well. Therefore, it is important to scale the data before applying Principal Component Analysis.
- **Information Loss:** Principal Component Analysis can result in information loss. While Principal Component Analysis reduces the number of variables, it can also lead to loss of information. The degree of information loss depends on the number of principal components selected. Therefore, it is important to carefully select the number of principal components to retain.
- **Non-linear Relationships:** Principal Component Analysis assumes that the relationships between variables are linear. However, if there are non-linear relationships between variables, Principal Component Analysis may not work well.
- **Computational Complexity:** Computing Principal Component Analysis can be computationally expensive for large datasets. This is especially true if the number of variables in the dataset is large.
- **Overfitting:** Principal Component Analysis can sometimes result in overfitting, which is when the model fits the training data too well and performs poorly on new data. This can happen if too many principal components are used or if the model is trained on a small dataset.






