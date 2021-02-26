# Multivariate Linear Regression (233) Predict employee salary

https://img.shields.io/badge/pthon-3.0.8-blue 
Python 3.0.8

## Project Summary

This project is part of my [Umuzi](https://www.umuzi.org/) data science bootcamp I  had attended from March 2020 until February 2021, The main aim of  the task was to use multivarient linear regression to predict the salary of individuals using dependent  variables in the data set like years of experiance ,field of work and others.Below find the key findings of the project.

##### key sections

* [feature selection](#feature-selection)
* [model evaluation](#model-evaluation)
* [conclusion](#conclusion)


For raw project instructions see: http://syllabus.africacode.net/projects/data-science-specific/multivariate-linear-regression/


## feature selection

![](https://lh3.googleusercontent.com/Uam0wOCdoT9BnewYWyUD7R_o2V0LqinlRtTyFIhxgMZAjOp-20Di2PW4oM4vADSzjNp9D02inYBT5zSstzUTRTjWtzcb1sXVZBv_e_wnCQ2pq8OXtWqPF5ygNGOPaWpAF1ZiM5ERBQ=w2400)

Salary is  the dependent variable we want to predict , which means all the other columns are potential independent variable . Feature Selection has to be performed in order to select those variables ,which contribute the most to the dependent variables outcome.

<b>Criteria</b>

1. Correlation with salary must be higher than .5<br>
![](https://lh3.googleusercontent.com/tpbZfnEAchXFFiNcKZK2mRVZDh92Aj_lXIMAzsoCt_4-ld5SrKo6Ak-748-tHS2hLU27-lBYsd9WVJr22LPGqBPMWJsQT8GyU0cwitt44F9frsTEb9TyC893k0x42w7GmuYUlF137A=w2400)

This correlation matrix shows salary to have a strong to medium correlation with yearsworked, yearsrank , position, market,male and field. The correlation matrix shows correlations between years worked, years rank and position.

2.The  P value based on correlation must be below .05 <br>
 ![](https://lh3.googleusercontent.com/0QmGEojMJu0L1kcxTnxvUf8P16aiuOYDdfqSsA7wgfWHUbgNX5WZDKAU0I3QGIe9JJeFmSpvkCdIMSbMJ6HKsDpnnjnZl1bCSjCyFTCB1g2l0BOTTE1E41zfXg7NUAFybvynaoumTw=w2400)

 A p-value is a measure of the probability that an observed difference could have occurred just by random chance. A p-value less than 0.05 is considered strong evidence against the null hypothesis since there is less than a 5% probability that the null hypothesis is correct and the results are random.All the P-values of the correlation coefficients are well below 0.5 therefore we can reject the null hypothesis and and assume that these correlation coefficients are not by chance.

3. The variance inflation factor (VIF) must be below 10 <br>
 ![VIF](https://lh3.googleusercontent.com/7blBr7J4B3Z-PVHwo9MbycuklR-N7wInnyYKGUq56MAO9pGitAivT_iC5sxVspOLqL5isl999I1PfrtTGmtED_-FiW476XSw_T56O75h-6VieI_Jz9XBG57fEH495v_kFKy0fdHSAQ=w2400 "VIF")


Variance inflation factor (VIF), measures multicollinearity,generally a VIF score of 10 and higher might cause problems for the model as the feature might be too correlated with other features, this might in turn cause the model to be too sensitive to certain changes as there will be multiple features measuring the same phenomenon.Therefore yearsworked might not be the best candidate as it has too high of correlation with the other features.Therefore according to our criteria These features were selected to train the model: Field,yearsrank, position,market and male


## model evaluation

 ![](https://lh3.googleusercontent.com/0Nc7ESYmfJqeENnBkR5kNOR5GFEUO6h8ciulo2blbX8PNCa-sGRFK6P1r4zmYsKULCHkLI5eiDPyrjtLMHSpTO25L1PxoxJz7xhqvUh3kRNlG9ptSxeO0q51y9-b09Q2ThWd1RkPXQ=w2400)

Field_engineering and Field engineering are not statistically significant. they have P values over 0.5.R-squared tells us that 83% of variance in employee salaries is accounted for b y this model.The difference/variance  in  the RMSE is lower than 5% (2.4%),therefore we can conclude that the extent of overfitting is small enough for us to maintain confidence in the may model to perform well in real world applications.



##### residue plots
 ![](https://lh3.googleusercontent.com/jil7p3NubKnIFmyTFfx0u-23OWxmeojAK4MDzgp3brefM8E8VgIGKtcayXNxsPGpMwrtP86BtneUMucQpNg97zOni3VccJfiP-jUX6Hi58YoLVTJ5ya_P4JC-J8Ii9iUiNqiRBjcyQ=w2400) ![](https://lh3.googleusercontent.com/V2kSiHO5dBA_1g9zBoL330QKz3ze0zFC9mit1dn--6LoESyrPXVOJ8iJpS_e7Ll1aTKhexjXerxkHvQYS8CPuzUzBsEwjPwaVDFAxBRAD_6Iwdz0_u0JMkcsZcG4EErO-2i67S5clg=w2400)


The line of best fit for the fitted values lies below the actual values , this means that the fitted values tend to be smaller than the actual values.
The model seems to have more variance in its predictions on the test date, it also seems to do better for the lower to mid predictions , but does increasingly badly for the higher the predictions.This might indicate overfitting.

## conclusion


Overall this is a good model as it accounts for 83% of the variation in employee salary. However one point of improvement would be using other models on this data set and comparing which one works best.