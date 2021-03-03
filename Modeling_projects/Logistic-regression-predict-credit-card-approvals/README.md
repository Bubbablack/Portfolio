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

![](https://lh3.googleusercontent.com/awVG0zTwoYPdqbIcLfIa3RMnU6-3Nm_SAraVs9pnm3somOcKVjXhPOPvtKXvsEs8YtAwm93ZGv-tGS_CIBwOWlBar_u9wxhTjyS5PXjZXegiH3ExfthHQ9q2ygb2MHgKDEutcijN-Q=w2400)

Some Columns have non numeric values, we will be converting all the non-numeric values into numeric ones. We do this because not only it results in a faster computation but also many machine learning models (like XGBoost) (and especially the ones developed using scikit-learn) require the data to be in a strictly numeric format. We will do this by using a technique called label encoding.

![](https://lh3.googleusercontent.com/YqTQfIxJnvZhEHbfD_PyufQyKaSVe0D_1CwUUwIsDjzhz9N-aITUeqRcuPWfJoTtTqQJMyS81IGuLVPE755ccPQShaFbffViqtiLxPNgNdhSS65pWsDK7_6fxcbg39bQDu5yIE5PMQ=w2400)

There are  some missing values to be imputed for columns 0, 1, 3, 4, 5, 6 and 13. We are going to impute these missing values with the most frequent values as present in the respective columns. 
### Model Evaluation

#### Accuracy of logistic regression classifier:  0.8377192982456141

Our model perfoms very well It was able to yield an accuracy score of almost 84%. We will now evaluate the model's confusion matrix. In the case of predicting credit card applications, it is equally important to see if our machine learning model is able to predict the approval status of the applications as denied that originally got denied. If our model is not performing well in this aspect, then it might end up approving the application that should have been approved. The confusion matrix helps us to view our model's performance from these aspects.

#### array([[92, 11], [26, 99]])


For the confusion matrix, the first element of the of the first row of the confusion matrix denotes the true negatives meaning the number of negative instances (denied applications) predicted by the model correctly. And the last element of the second row of the confusion matrix denotes the true positives meaning the number of positive instances (approved applications) predicted by the model correctly.Overall I think our model has performed reall well in getting only a few false negetives and false posetives.
however more specificall we can tell from the confusion matrics ,percent wise it is more likely to to give a false positive than a false negetive , 
It is more likely to be wrong on clients who should get aproved than wrong on clients that shouldn't.

#### Best: 0.853623 using {'max_iter': 100, 'tol': 0.01}

We have instantiate GridSearchCV() with our earlier logreg model with all the data we have. Instead of passing train and test sets separately, we Have supply X (scaled version) and y. And have managed to slightly improve our model up to  85% acuraccy.



### Conclusion

While building this credit card predictor, we tackled some of the most widely-known preprocessing steps such as scaling, label encoding, and missing value imputation. We finished with some machine learning to predict if a person's application for a credit card would get approved or not given some information about that person.

Points of improvemt: ROC curves can be used in future to give more clarity and visualise the models performance .
According To the clients descretion we The threshold of the model can be tweaked  towards having less false posetives , This will probably increase the number of false negetives as well, However in a case like this one , we would rather reject more people but insure that the right people are aproved.
