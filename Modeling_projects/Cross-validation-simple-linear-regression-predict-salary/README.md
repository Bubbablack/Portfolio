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

This project is part of my Umuzi data science bootcamp I had attended from March 2020 until February 2021, The main aim of the task was to use linear regression to predict the salary of individuals using the dependent variable (Yearsworked) in the data set like years of experiance .Below find the key findings of the project where i have further summarized the main pointts of my findings.

##### key sections

* [Data Cleaning](#Data-Cleaning)
* [Exploritory Data Analysis](#Exploritory-Data-Analysis)
* [Model Evaluation](#Model-Evaluation)
* [Conclusion](#Conclusion)

For raw project instructions see: https://raw.githubusercontent.com/Umuzi-org/tech-department/master/content/projects/data-science-specific/cross-validation-and-simple-linear-regression/_index.md


### Data Cleaning 
![](https://lh3.googleusercontent.com/U_m1L8UZIn9DIkaKEhAIav0KfSbVM_pTX7oezbaGzTE4fClXQN0ZlF7XnufqGeVSUs-RiYU7mt0GF7OYzV9ug5-1-uf35SGje5hFDWQwiVVXOXOyx5zanTjo53PTlQvRJbT7UDRNvw=w2400)

Salary is the dependent variable we want to predict ,all the other columns are potential independent variable however for this project we are only interested in years worked as a feature.

![](https://lh3.googleusercontent.com/wAuG_x4mxh9-85kYuwT94apLXsJhPJh_9xVuJJDcf51tV5kUORriY5zBwePJhIXiOP0VA_C0qnEhvkiTDfOEjDUnCt4qluYMBCDKI3u3tAltxkVqPuFf6nDNBPKiKuKiOVLMdaRpvA=w2400)

There is one missing value under the salary column, therefore, the missing values are replaced with the mean of all the values in that column.

![](https://lh3.googleusercontent.com/XIodawGKJG5gO01l3dP4F9Pv0MG2TAmXzchigPmDlT5RrAQUmarU2ojNpVCjzTykxusBTmiFGSz8c9GT0ZxPK9mKecnu1jCHNCxRtYa6xZYD03Vj5UvpNpRIKxVAgQRzIXnqQ61ryQ=w2400)


There are two extreme values in the salary column.The extreme values are removed, because extreme values are unlikely observations in a dataset,if not removed extreme values may cause overfitting, as they do not represent what is typical for that data set.

### Exploritory Data Analysis


![](https://lh3.googleusercontent.com/gR_ZtsPmvHWsoEw4xDio5q5p_VZ0sUSG0EoWXPS0fwFUwpELh_aOc3baKR-6KBxvWH79uUArxR5Bc7-N5YBhZiSr7jSX2ogebf_yWX70_X8h-iVgNbUbOeIYnK3dh2dyhzzu8GYjEg=w2400)

The distributions are posetively skewed.This means the majority of the values lies in the lower half of the distribution.

![](https://lh3.googleusercontent.com/uNFqEiCWMAaS1a8lnQy9qK9a0JNp9iOdl0JDfBvevFu07ymwIvzYqhF7p7HGwJoPNUgnDJhu7tewfwJy1vX-M2x3LbEP6MCSJpiqvXSUT3NWcP4AJBthI95oZ162LvgKODs-e3HBAw=w2400)


 There is a linear nomial relationship between years worked and salary,We can draw a line of best fit that is not curved  therefore we can use linear regression to model this relationship.

### Model Evaluation
#### OLS model summary
![](https://lh3.googleusercontent.com/xtfoP5pUD4nZTAIDT3NX4hcyngin9wo1KDVuaTQJ_SfTswUPp-VKHcJlRjwphT5ap6QS2rqsmTuSXBjttSosu0bQUecS-Ca6WRH1cbyAKUHSbMywZuBhVn4ut7sG4jhtP07glOOxnA=w2400)


Years worked is a significant feature since the p value is 0 (less than .05), therefore we can reject the null hypothesis and conclude that there is a correlation between years worked and salary.

39% of varience in employee salaries are accounted for by number of years worked.

For every year worked ,we can expect an employee's salary to increas by about 809.3844.

We can be 95% confident that the coeficiant or constant change in salary per year worked, lies between 703.980 and 914.789, and since the coeficeiant of our model is 809.3844, this is further confirmation on the validity of the model, and we can more confidently reject the null hypothesize.

The difference between the two RMSE's is very small , less than 1.5 percent (1.3279012795801126) , therfore we can conclude that our model is not overfitting since , the test model does not perform that much diferently from the training model.


### conclusion
Although significant ,The predicting power of this model is just too low (39%), to be reliably used in any decision making proccess This would have to be a tool used in conjucture with other tools and research . 


![](https://lh3.googleusercontent.com/Cs_wtw8s2xc12ityinLULza0PUidGn3N-KzKCYq4exrlJNRlaiBCGlMw3EIQh2w4DwMATgQ40rQEbidOd4i-8HJP2xSea-OtGdhD-WWA2Z69dyTcuyr63zIHopOO-zgAj4-iTeo_ng=w2400)

There is an orportunity to improve the model by using multivarient linear regression as salary corelates with many other features besides years work,including these features may improve the predicting power and therefore usefulness of this model.
