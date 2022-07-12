import pandas as pd
from matplotlib import pyplot as plt


# load data into data frame

gdp_data = pd.read_csv('/Users/ryanw/all_data.csv')
gdp_data.columns = ['country', 'year', 'life_expectancy', 'gdp']

years = ('2000', '2001', '2002', '2003', '2004', '2005', '2006',
         '2007', '2008', '2009', '2010', '2011', '2012', '2013',
         '2014', '2015')

# Get gdp from top 3 gdp earners

american_gdp = gdp_data.gdp[gdp_data.country ==
                            'United States of America'].reset_index()
china_gdp = gdp_data.gdp[gdp_data.country == 'China'].reset_index()
germany_gdp = gdp_data.gdp[gdp_data.country == 'Germany'].reset_index()

# get life expectancy from top 3 gdp earners

american_life_expectancy = gdp_data.life_expectancy[
    gdp_data.country == 'United States of America'].reset_index()
china_life_expectancy = gdp_data.life_expectancy[
    gdp_data.country == 'China'].reset_index()
germany_life_expectancy = gdp_data.life_expectancy[
    gdp_data.country == 'Germany'].reset_index()

# get gdp from bottom 3 gdp earners

chile_gdp = gdp_data.gdp[gdp_data.country == 'Chile'].reset_index()
mexico_gdp = gdp_data.gdp[gdp_data.country == 'Mexico'].reset_index()
zimbabwe_gdp = gdp_data.gdp[gdp_data.country == 'Zimbabwe'].reset_index()

# get life expectancy from bottom 3 gdp earners

chile_life_expectancy = gdp_data.life_expectancy[
    gdp_data.country == 'Chile'].reset_index()
mexico_life_expectancy = gdp_data.life_expectancy[
    gdp_data.country == 'Mexico'].reset_index()
zimbabwe_life_expectancy = gdp_data.life_expectancy[
    gdp_data.country == 'Zimbabwe'].reset_index()

# plot graph comparing year to gdp of the top three gdp earners

plt.figure(figsize=(13, 13))
ax1 = plt.subplot(2, 2, 1)
ax1.plot(american_gdp.gdp, color='blue')
ax1.plot(china_gdp.gdp, color='red')
ax1.plot(germany_gdp.gdp, color='green')
ax1.legend(('America', 'China', 'Germany'))
plt.xlabel('Year')
plt.ylabel('GDP')
plt.xticks(rotation=45)
ax1.set_xticks(range(16))
ax1.set_xticklabels(years)
plt.title('GDP of Top 3 Earners')

# plot graph comparing year to life expectancy of top three gdp earners

ax2 = plt.subplot(2, 2, 2)
ax2.plot(american_life_expectancy.life_expectancy, color='blue')
ax2.plot(china_life_expectancy.life_expectancy, color='red')
ax2.plot(germany_life_expectancy.life_expectancy, color='green')
ax2.set_xticks(range(16))
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel('Life Expectancy (years)')
ax2.set_xticklabels(years)
ax2.legend(('America', 'China', 'Germany'))
plt.title('Life Expectancy of Top 3 Earners')

# plot graph comparing year to gdp of the bottom three gdp earners

ax3 = plt.subplot(2, 2, 3)
ax3.plot(chile_gdp.gdp, color='red')
ax3.plot(mexico_gdp.gdp, color='green')
ax3.plot(zimbabwe_gdp.gdp, color='blue')
ax3.set_xticks(range(16))
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel('GDP')
ax3.set_xticklabels(years)
ax3.legend(('Chile', 'Mexico', 'Zimbabwe'))
plt.title('GDP of bottom 3 Earners')

# plot graph comparing year to life expectancy of the bottom three gdp earners

ax4 = plt.subplot(2, 2, 4)
ax4.plot(chile_life_expectancy.life_expectancy, color='red')
ax4.plot(mexico_life_expectancy.life_expectancy, color='green')
ax4.plot(zimbabwe_life_expectancy.life_expectancy, color='blue')
ax4.set_xticks(range(16))
ax4.set_xticklabels(years)
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel(('life Expectancy (years)'))
ax4.legend(('Chile', 'Mexico', 'Zimbabwe'))
plt.title('Life Expectancy of bottom 3 earners')
plt.savefig('/Users/ryanw/Gdp.png')
plt.show()
plt.clf()

# plot all life expectancies except zimbabwe vs year

plt.figure(figsize=(12, 10))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(american_life_expectancy.life_expectancy, color='blue')
ax1.plot(chile_life_expectancy.life_expectancy, color='red')
ax1.plot(germany_life_expectancy.life_expectancy, color='green')
ax1.plot(chile_life_expectancy.life_expectancy, color='orange')
ax1.plot(mexico_life_expectancy.life_expectancy, color='purple')
ax1.set_xticks(range(16))
ax1.set_xticklabels(years)
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over The Years')
ax1.legend(('America', 'China', 'Germany', 'Chile', 'Mexico'))

# plot all life expectancies with zimbabwe vs year

ax2 = plt.subplot(1, 2, 2)
ax2.plot(american_life_expectancy.life_expectancy, color='blue')
ax2.plot(chile_life_expectancy.life_expectancy, color='red')
ax2.plot(germany_life_expectancy.life_expectancy, color='green')
ax2.plot(chile_life_expectancy.life_expectancy, color='orange')
ax2.plot(mexico_life_expectancy.life_expectancy, color='purple')
ax2.plot(zimbabwe_life_expectancy.life_expectancy, color='pink')
ax2.legend(('America', 'China', 'Germany', 'Chile', 'Mexico', 'Zimbabwe'))
ax2.set_xticks(range(16))
ax2.set_xticklabels(years)
plt.xticks(rotation=45)
plt.xlabel('Years')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over The Years')
plt.savefig('/Users/ryanw/life_expectancy.png')
plt.show()
