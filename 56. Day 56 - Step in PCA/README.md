<h1 align="center">Steps in PCA (Principal Component Analysis)</h1>


### **Step 1 : Covariance Matrix Computation**

Covariance measures the strength of joint variability between two or more variables, indicating how much they change in relation to each other. To find the covariance we can use the formula:

<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/56.%20Day%2056%20-%20Step%20in%20PCA/covar.svg">

The value of covariance can be positive, negative, or zeros.

- Positive: As the x1 increases x2 also increases.
- Negative: As the x1 increases x2 also decreases.
- Zeros: No direct relation


---


### **Step 2 : Compute Eigenvalues and Eigenvectors of Covariance Matrix to Identify Principal Components**

Let A be a square matrix with n*n dimensions and X be a non-zero vector for which 

<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/56.%20Day%2056%20-%20Step%20in%20PCA/eig1.svg">

for some scalar values \lambda   . then \lambda is known as the eigenvalue of matrix A and X is known as the eigenvector of matrix A for the corresponding eigenvalue.

It can also be written as :

<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/56.%20Day%2056%20-%20Step%20in%20PCA/eig2.svg">

where I am the identity matrix of the same shape as matrix A. And the above conditions will be true only if (A - \lambda I)    will be non-invertible (i.e. singular matrix). That means,

<img src="https://github.com/mankarsnehal/100-Days-of-Code-Data-Science/blob/main/56.%20Day%2056%20-%20Step%20in%20PCA/eig3.svg">

From the above equation, we can find the eigenvalues \lambda, and therefore corresponding eigenvector can be found using the equation AX = \lambda X   .



