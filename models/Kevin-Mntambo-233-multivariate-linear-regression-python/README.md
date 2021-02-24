Multivariate Linear Regression (233)

language = Python 3.0.8

## Project Summary

This project is part of my [Umuzi](https://www.umuzi.org/) data science bootcamp I  had attended from March 2020 until February 2021, The main aim of  the task was to use multivarient linear regression to predict the salary of individuals using dependent  variables in the data set like years of experiance ,field of work and others.

For raw project instructions see: http://syllabus.africacode.net/projects/data-science-specific/multivariate-linear-regression/


### Exploritory analysis
<img src="../images/matrix.png" width="350" title="hover text">
![](https://photos.app.goo.gl/RABCyatoShGpHixe6)


### feature selection


In order to select features the following criteria will be used:

correlation with salary must be higher than .5 .
P value based on correlation must be below .05
and the variance inflation factor (VIF) must be below 10.

Therefore, all other feature columns are dropped except for yearsrank ,position, market ,male and field since according to our criteria these are the best candidates to fit the model with

chosen features 'Field','yearsrank', 'position','market','male'

### model evaluation

Field_engineering and Field engineering are not statistically significant. they have P values over 0.5.

The difference/variance  in  the RMSE is lower than 5%(2.4%),therefore we can conclude that the extent of overfitting is small enough for us to maintain confidence in the may model to perform well in real world applications.

Overall this is a good model , accounts for 83% of the variation in employee salary, it performs slightly worse on test data , however not too bad , to be ruled off as overfitting,one issue is might be that two of my features are statistically insignificant,maybe an area of improvement would be to find a way to deal or remove these features without totally losing the information provided by the field column.


### conclusion







