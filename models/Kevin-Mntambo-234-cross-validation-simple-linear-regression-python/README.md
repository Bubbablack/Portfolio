# Cross-validation & Simple Linear Regression (234) Predicting employee salary

![](https://img.shields.io/badge/python-3.0.8-blue)
![](https://img.shields.io/badge/jupyter-1.0.0-blue)
![](https://img.shields.io/badge/matplotlib-3.0.3-blue)
![](https://img.shields.io/badge/numpy-1.16.2-blue)
![](https://img.shields.io/badge/pandas-0.24.0-blue)
![](https://img.shields.io/badge/scikit-learn-0.20.3-blue)
![](https://img.shields.io/badge/scipy-1.2.1-blue)
![](https://img.shields.io/badge/seaborn-0.9.0-blue)
![](https://img.shields.io/badge/statsmodels-0.9.0-blue)

## Prioject summary

This project is part of my Umuzi data science bootcamp I had attended from March 2020 until February 2021, The main aim of the task was to use multivarient linear regression to predict the salary of individuals using dependent variables in the data set like years of experiance ,field of work and others.Below find the key findings of the project.

##### key sections

* [data cleanin](#Data-Cleaning)
* [Exploritory Data Analysis](#Exploritory-Data-Analysis)
* [model evaluation](#Model-Evaluation)
* [conclusion](#Conclusion)

For raw project instructions see: https://raw.githubusercontent.com/Umuzi-org/tech-department/master/content/projects/data-science-specific/cross-validation-and-simple-linear-regression/_index.md


### Data Cleaning 
![](https://lh3.googleusercontent.com/U_m1L8UZIn9DIkaKEhAIav0KfSbVM_pTX7oezbaGzTE4fClXQN0ZlF7XnufqGeVSUs-RiYU7mt0GF7OYzV9ug5-1-uf35SGje5hFDWQwiVVXOXOyx5zanTjo53PTlQvRJbT7UDRNvw=w2400)

![](https://lh3.googleusercontent.com/wAuG_x4mxh9-85kYuwT94apLXsJhPJh_9xVuJJDcf51tV5kUORriY5zBwePJhIXiOP0VA_C0qnEhvkiTDfOEjDUnCt4qluYMBCDKI3u3tAltxkVqPuFf6nDNBPKiKuKiOVLMdaRpvA=w2400)

There is one missing value under the salary column

The missing values are replaced with the mean of all the values in that column.

We use the mean becuase salary has continues numerical values .Ideally we don't want to lose any information that can help us analyze or create a better a model, and so if the particular feature like salary is numerical and continueos, we can replace with the mean becuase, no matter how many times we add the mean it still gets conserved,it doesn't change, for none numeric and/or discrete features however we would have to drop the values or replace them with a placeholder.

![](https://lh3.googleusercontent.com/XIodawGKJG5gO01l3dP4F9Pv0MG2TAmXzchigPmDlT5RrAQUmarU2ojNpVCjzTykxusBTmiFGSz8c9GT0ZxPK9mKecnu1jCHNCxRtYa6xZYD03Vj5UvpNpRIKxVAgQRzIXnqQ61ryQ=w2400)


There are two extreme values in the salary column.


The extreme values are removed, because extreme values are unlikely observations in a dataset,if not removed extreme values may cause overfitting, as they do not represent what is typical for that data set.Extreme values tend to streach the mean to one direction , whereby the mean then no longer represents the distribution of the majaority of the data point which in turn makes the model poorly when given new data.


### Exploritory Data Analysis


![](https://lh3.googleusercontent.com/gR_ZtsPmvHWsoEw4xDio5q5p_VZ0sUSG0EoWXPS0fwFUwpELh_aOc3baKR-6KBxvWH79uUArxR5Bc7-N5YBhZiSr7jSX2ogebf_yWX70_X8h-iVgNbUbOeIYnK3dh2dyhzzu8GYjEg=w2400)

The distributions are posetively skewed.This means the majority of the values lies in the lower half of the distribution.

![](https://lh3.googleusercontent.com/uNFqEiCWMAaS1a8lnQy9qK9a0JNp9iOdl0JDfBvevFu07ymwIvzYqhF7p7HGwJoPNUgnDJhu7tewfwJy1vX-M2x3LbEP6MCSJpiqvXSUT3NWcP4AJBthI95oZ162LvgKODs-e3HBAw=w2400)


We can draw a line of best fit that is not curved , which confirms that there is a linear nomial relationship exists between years worked and salary. therefore this confirms using linear regression to model this would work. It is a positive and modearte association.

### Model Evaluation

![](https://lh3.googleusercontent.com/xtfoP5pUD4nZTAIDT3NX4hcyngin9wo1KDVuaTQJ_SfTswUPp-VKHcJlRjwphT5ap6QS2rqsmTuSXBjttSosu0bQUecS-Ca6WRH1cbyAKUHSbMywZuBhVn4ut7sG4jhtP07glOOxnA=w2400)


The null hypothesis states that there is no relationship between the two variables being studied (salary and years worked). It states that the results are due to chance and are not significant in that one does not affect the other.

A p-value is a measure of the probability that an observed difference could have occurred just by random chance. A p-value less than 0.05 is considered strong evidence against the null hypothesis since there is less than a 5% probability that the null hypothesis is correct and the results are random.

Years worked is a significant feature since the p value is 0 (less than .05), therefore we can reject the null hypothesis and conclude that there is a correlation between years worked and salary.

R-squared tells us that 39% of varience in employee salaries are accounted for by number of years worked.

The unstandardized coefficient, tells us that for every year worked ,an employee's salary increases by about 809.3844.

The 95% interval tells us that we can be 95% confident that the coeficiant or constant change in salary per year worked, lies between 703.980 and 914.789, and since the coeficeiant of our model is 809.3844, this is further confirmation on the validity of the model, and we can more confidently reject the null hypothesize.



### conclusion
The difference between the RMSE of the training data and that of the test data :  1.3279012795801126
The difference between the two RMSE's is very small , less than 1.5 percent , therfore we can conclude that our model is not overfitting since , the test model does not perform that much diferently from the training model.

![](https://lh3.googleusercontent.com/Cs_wtw8s2xc12ityinLULza0PUidGn3N-KzKCYq4exrlJNRlaiBCGlMw3EIQh2w4DwMATgQ40rQEbidOd4i-8HJP2xSea-OtGdhD-WWA2Z69dyTcuyr63zIHopOO-zgAj4-iTeo_ng=w2400)
