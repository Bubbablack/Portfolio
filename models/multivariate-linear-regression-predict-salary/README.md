Multivariate Linear Regression (233)

language = Python 3.0.8

## Project Summary

This project is part of my [Umuzi](https://www.umuzi.org/) data science bootcamp I  had attended from March 2020 until February 2021, The main aim of  the task was to use multivarient linear regression to predict the salary of individuals using dependent  variables in the data set like years of experiance ,field of work and others.

For raw project instructions see: http://syllabus.africacode.net/projects/data-science-specific/multivariate-linear-regression/


### Exploritory analysis

![](https://lh3.googleusercontent.com/tpbZfnEAchXFFiNcKZK2mRVZDh92Aj_lXIMAzsoCt_4-ld5SrKo6Ak-748-tHS2hLU27-lBYsd9WVJr22LPGqBPMWJsQT8GyU0cwitt44F9frsTEb9TyC893k0x42w7GmuYUlF137A=w2400)

![](https://lh3.googleusercontent.com/7blBr7J4B3Z-PVHwo9MbycuklR-N7wInnyYKGUq56MAO9pGitAivT_iC5sxVspOLqL5isl999I1PfrtTGmtED_-FiW476XSw_T56O75h-6VieI_Jz9XBG57fEH495v_kFKy0fdHSAQ=w2400) ![](https://lh3.googleusercontent.com/0QmGEojMJu0L1kcxTnxvUf8P16aiuOYDdfqSsA7wgfWHUbgNX5WZDKAU0I3QGIe9JJeFmSpvkCdIMSbMJ6HKsDpnnjnZl1bCSjCyFTCB1g2l0BOTTE1E41zfXg7NUAFybvynaoumTw=w2400)

### feature selection


In order to select features the following criteria will be used:

<ul>
<li>correlation with salary must be higher than .5 .</li>
<li>P value based on correlation must be below .05</li>
<li>and the variance inflation factor (VIF) must be below 10.</li>
</ul>
Therefore, all other feature columns are dropped except for yearsrank ,position, market ,male and field since according to our criteria these are the best candidates to fit the model with

chosen features 'Field','yearsrank', 'position','market','male'

### model evaluation

Field_engineering and Field engineering are not statistically significant. they have P values over 0.5.

The difference/variance  in  the RMSE is lower than 5%(2.4%),therefore we can conclude that the extent of overfitting is small enough for us to maintain confidence in the may model to perform well in real world applications.

Overall this is a good model , accounts for 83% of the variation in employee salary, it performs slightly worse on test data , however not too bad , to be ruled off as overfitting,one issue is might be that two of my features are statistically insignificant,maybe an area of improvement would be to find a way to deal or remove these features without totally losing the information provided by the field column.


### conclusion







