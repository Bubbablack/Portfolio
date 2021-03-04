# Statistical Thinking Global Enviromental Sustainability

## Project Summary
We take a look at the behavior of different countries over time to help improve environmental sustainability in accordance to goal 7 of the 8 goals set by The Millennium Development for 2015 that were defined by the United Nations to help improve living conditions and the conditions of our planet. We will have a look at some of the key indicators for this, namely carbon dioxide emissions, protected land and sea areas, and forests.

#### Key Sections
* [Data Cleaning](#Data-Cleaning)
* [Exploritory Analysis](#Exploritory-Analysis)
  * [Carbon Emsissions over time](Carbon-Emsissions-over-time)
  * [Area Coverage](Area-Coverage)
* [Conclusion](Conclusion)


For raw project instructions see: https://raw.githubusercontent.com/Umuzi-org/tech-department/master/content/projects/data-science-specific/statistical-thinking/index.md

##  Exploritory Analysis

####  Carbon Emsissions over time

![](https://lh3.googleusercontent.com/gSyXJoMw3_GXa7q6R0YCxMC58mzvh2LLFZVyM8tdWW7oPZuZF7jOyQEWfj3WHp1HxXNE03CfTCAvgrCcJPnJTCv94RNwxybzRbvzk49nOKB_MoyeJrd08gv8gL_x4KkDTfhngotI_w=w2400)

Here are the top 5 polluting countries in 1990 vs how they were doing in 2011. From the offset, we might expect the CO2 levels to rise exponentially over time, however this table shows that most top emitting countries have been increasing their CO2 footprint, relatively slowly over time, with China being the only exception.

![](https://lh3.googleusercontent.com/rLGFlH-bnfYZtzZQjUE8TftK627ukSVhL39He120hNcGruzkfXC1IzbI4G4n038ItT0h6TWY4apT8jR6CtS6GWbcPFcR4SxaaBdhLKgN57ZO4fGNNUYieRsKnDV5PfveGCp2eevqBA=w2400)

The bottom 5 polluting countries in 1990 vs how they were doing in 2011. Once again, the data shows that most countries show a slow rise in the yearly CO2 emissions over time.

I did spot a problem, Yemen has -2999.6.This seems like an anomaly especially since it is rare to have a negative emission level, a negative so high no less, so I have decided to drop the row.

![](https://lh3.googleusercontent.com/LpyOlTdGQhSvaoB76rTMi5Mi8YZWukD6HSRiu_eJCryKKXRNbAqD-EAT7d73JZhMaxNzzeaagnszWw3tULmBCJtyTU_HF03SEDXyM7v4EC1PsVKYy1Vawi9fIJ2OGjVObtMY_dK0hA=w2400)


This histogram is suprising in that we might have not expected the majority of of countries to be grouped together around the same area, The measures of distribution could have us believe that the values would be spread or distributed vastly across the graph, instead it seems that only a few outliers are distorting the general veiw.

The vast majority of countries emit less than 500 000 metric tons of CO2, with only a few countries who are outliers, above that threshold.

![](https://lh3.googleusercontent.com/YsB4AQE6L3J0Uh-c7PdOiiTz2HRGl5pT4aaUXe83XeExIU9rbY2iZETMrEcw_NQLpbXIL3jLzt-p1pPGmoBI6MICHGZf10SDwCfIGVaj_UiAxi3Q1953fS6Iv8IyQjcZgwK0WpZJaQ=w2400)


The highest contributers overtime, are the USA and China. China had a boom in GDP and production from the early 2000s which coincides with its exponential growth in CO2 emissons surpassing even the US by the mid-2000s. Although the USA has not increased its CO2 emisions over time, the US itself is one of the biggest contributers of CO2 overall over time. Since the 90s it has consistently emitted relatively higher emissions than most countries.

Meanwhile countries like Russia seem to be slowly lowering their emissions and countries like India show a gradual increase.

Countries like South Africa and Brazil have managed to keep their emissions low and unchanged over the years.

Overall, most countries do not seem to be increasing ther carbon footprint over time. Only China has shown a sharp rise.
#### Area Coverage
![](https://lh3.googleusercontent.com/sfukGNz-KFnAaOKR2PXmfzsUtCcKA5aaL8Px8niD9M15ZJ5yCtaBVWb-X7ty6LI6C72tKIU-BS3vLHWXtvlKz6hCzjP-SbltTdeuMSy1yomuud3vg5Jx-mO75J-UNapEyVwbBJljNQ=w2400)

This is a scatter plot that compares the proportion of land area covered by forest and the percentage of area protected in 2000. There doesn't seem to be a correlation between the proportion of land area covered by forest and the percentage of area protected. There seems to be many outliers near the x and y margins especially.

## Conclusion
Climate change is and is becoming a bigger problem, it may be easy to assume that this problem is caused by a general increase of emissions across all countries over time, however this data set shows us that, in actuality, the majority of countries have relatively low emissions and it's only a few countries that produce most of the carbon emissons, the outliers. Furthermore, most countries are not increasing their carbon footprint at the rate we might expect, most countries actually only show a slight increase over time, if any. Only China seems to have been increasing its emissions at an exponential rate and has become, by far, the largest emitting country. The USA, however, has most likely emitted more total emissons over time since it has been emittimg high levels of CO2 consistently for longer.
