In this repository are examples of code that I have written
below I will explain what each script does

Billingcode.py:         This is a script that I wrote for myself to generate bills for labor and reciepts.
                        This script takes input for each category of labor and adds them together
                        to get a total and then generates an itemized bill as a pdf.

insurance_anaylisis.py: This script uses the insurance.csv file to create a pandas dataframe and 
                        analyze the data to generate insights.

Linear_reg_example.py:  This script uses the diabetes.csv file to create a dataframe and compare bmi
                        to blood pressure with a scatter plot and then use statsmodels.api to create
                        an ordinary least squares line and then plot it over the scatter plot

syslogproject.py:       This script was written for a google certificate course project, It takes a
                        system log, which I simulated in the test.txt file, and it parses it making
                        two csv files, error_message.csv lists each error and the frequency they occur
                        and user_statistics.csv lists the users and each INFO and ERROR entry for each
                        user.

gdp_project.py:         This script was written for a data analysis course on codecademy, It takes 
                        all_data.csv, uses pandas to make a dataframe and with that dataframe then, 
                        uses pyplot to make two figures. The first figure compares gdp and life expectancy
                        over time, splitting it into two categories: top 3 gdp earners and bottom
                        3 gdp earners. The second figure has two plots, the first one compares 
                        the life expectancy over time for all countries excluding the outlier zimbabwe. 
                        The second one plots life expectancy over time of all countries including the
                        outlier zimbabwe.
