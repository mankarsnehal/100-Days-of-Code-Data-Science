<h1 align="center">Multiple Linear Regression</h1>


<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/31.%20Day%2031%20-%20Multiple%20Linear%20Regression/MLR%20Implementation.jpg" height="750px">

---

# Multiple Linear Regression:

- Models Linear relationship between single Independent continuous variable and multiple Independent Variable.

- It is Simple Linear Regression extension, takes more than one predictor (Independent) variables to predict 1 target variable.


# Implementation Steps:

1. **Import libraries :** Import the important libraries like - pandas, numpy and matplotlib for further use.
   
2. **Gather Data :** Then, import the dataset.
   
3. **EDA (Exploratory Data Analysis) :** Handle null/missing values, remove duplicates and encoding of categorical data.
   
4. **Split the dataset :** Firstly, extract Dependent and Independent variables from the dataset. Then, split the data into training and testing data.
   
5. **Training model :** Use LinearRegression( ) to train the model using the data reserved for training the model.
   
6. **Result prediction :** Using the model, predict output for testing data.
  
7. **Model Evaluation :** Make use of R2-Score and mean squared error metrics to find goodness of fit of the model.



# Real-world Application: Student Performance Analysis -

Imagine predicting student performance based on factors like study time, attendance, and socioeconomic background. Multiple Linear Regression allows us to model these relationships, offering insights for improving academic outcomes.
