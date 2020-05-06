
In this project, I worked with anti-cancer pharmaceutical data. This data show results from screening for potential treatments for squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.

In this dataset, 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals' drug of interest, Capomulin, versus the other treatment regimens. I generated all of the tables and figures needed for the technical report of the study.


To complete this task 

* I checked the data for duplicate mice and removed any data associated with that mouse ID.

* I generated a summary statistics table consisting of the mean, median, variance, standard deviation, and SEM of the tumor volume for each drug regimen.

* I generated a bar plot using both Pandas's `DataFrame.plot()` and Matplotlib's `pyplot` that shows the number of data points for each treatment regimen.

* I generated a pie plot using both Pandas's `DataFrame.plot()` and Matplotlib's `pyplot` that shows the distribution of female or male mice in the study.


* I calculated the final tumor volume of each mouse across four of the most promising treatment regimens: Capomulin, Ramicane, Infubinol, and Ceftamin. Calculate the quartiles and IQR and quantitatively determine if there are any potential outliers across all four treatment regimens.

* I used Matplotlib, generated a box and whisker plot of the final tumor volume for all four treatment regimens and highlighted potential outliers in the plot by changing their color and style.

* I generated a line plot of time point versus tumor volume for a single mouse treated with Capomulin.

* I generated a scatter plot of mouse weight versus average tumor volume for the Capomulin treatment regimen.

* I calculated the correlation coefficient and linear regression model between mouse weight and average tumor volume for the Capomulin treatment. Plot the linear regression model on top of the previous scatter plot.

* I looked across all previously generated figures and tables and write at least three observations that could be made from the data. 

