# Logistic Regression (252) Predict credit card approvals

## Project summary

Commercial banks receive a lot of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. In this notebook, we will build an automatic credit card approval predictor using machine learning techniques, just like the real banks do.

#### key 
* [Data Cleaning](Data_Cleaning)
* [Model Evaluation](Model_Evaluation)
* [Model Optimasation](Model_Optimasation)
* [Conclusion](Conclusion)

For raw project instructions see: http://syllabus.africacode.net/projects/data-science-specific/logistic-regression/credit-card-approvals/

### Data Cleaning

First, we will be converting all the non-numeric values into numeric ones. We do this because not only it results in a faster computation but also many machine learning models (like XGBoost) (and especially the ones developed using scikit-learn) require the data to be in a strictly numeric format. We will do this by using a technique called label encoding.


![](https://lh3.googleusercontent.com/awVG0zTwoYPdqbIcLfIa3RMnU6-3Nm_SAraVs9pnm3somOcKVjXhPOPvtKXvsEs8YtAwm93ZGv-tGS_CIBwOWlBar_u9wxhTjyS5PXjZXegiH3ExfthHQ9q2ygb2MHgKDEutcijN-Q=w2400)

![](https://lh3.googleusercontent.com/N2hjbqycZFegLghUQ6TEROcaoqeT9C4EVWKUHq2rbhcZLrvQVXHuC4-Wo4hIKxoQ6nhz540x7hLZRzMcfLsc2sL4FmOclnOVJhGohNRkADNz255nQ2wBqpohddInhvxdVhsbyCfmQg=w2400)

![](https://lh3.googleusercontent.com/YqTQfIxJnvZhEHbfD_PyufQyKaSVe0D_1CwUUwIsDjzhz9N-aITUeqRcuPWfJoTtTqQJMyS81IGuLVPE755ccPQShaFbffViqtiLxPNgNdhSS65pWsDK7_6fxcbg39bQDu5yIE5PMQ=w2400)

### Model Evaluation
We will now evaluate our model on the test set with respect to classification accuracy. But we will also take a look the model's confusion matrix. In the case of predicting credit card applications, it is equally important to see if our machine learning model is able to predict the approval status of the applications as denied that originally got denied. If our model is not performing well in this aspect, then it might end up approving the application that should have been approved. The confusion matrix helps us to view our model's performance from these aspects.

For the confusion matrix, the first element of the of the first row of the confusion matrix denotes the true negatives meaning the number of negative instances (denied applications) predicted by the model correctly. And the last element of the second row of the confusion matrix denotes the true positives meaning the number of positive instances (approved applications) predicted by the model correctly.



### Model Optimasation


We have defined the grid of hyperparameter values and converted them into a single dictionary format which GridSearchCV() expects as one of its parameters. Now, we will begin the grid search to see which values perform best.

We will instantiate GridSearchCV() with our earlier logreg model with all the data we have. Instead of passing train and test sets separately, we will supply X (scaled version) and y. We will also instruct GridSearchCV() to perform a cross-validation of five folds.

### Conclusion
While building this credit card predictor, we tackled some of the most widely-known preprocessing steps such as scaling, label encoding, and missing value imputation. We finished with some machine learning to predict if a person's application for a credit card would get approved or not given some information about that person.
