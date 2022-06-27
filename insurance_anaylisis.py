import os
import csv
from statistics import mean

# initiate list to hold data
insurance = []
# initiate variables to hold smoker data

total_number_smokers = 0
total_number_non_smokers = 0
total_age_smokers = 0

#Create a list of dictionaries to hold the data
 
os.chdir('/Users/ryanw/OneDrive/desktop')
with open('insurance.csv') as file:
    for line in csv.DictReader(file):
        insurance.append(line)
smokers_list = []
non_smokers_list = []

# insights on smokers

def smokers_by_region(data, region):
    total_smokers = 0
    total_customers = 0
    for row in data:
        if row['region'] == region:
            total_customers += 1
        if row['region'] == region and row['smoker'] == 'yes':
            total_smokers += 1
    percent_smokers = round(total_smokers/total_customers*100, 2)
    print('the percentage of smokers in the {} is {}'
          .format(region, percent_smokers))

smokers_by_region(insurance, 'southwest')
smokers_by_region(insurance, 'southeast')
smokers_by_region(insurance, 'northwest')
smokers_by_region(insurance, 'northeast')

def find_age_range_averages_by_age(data, start, stop):
    num_customers = 0
    num_smokers = 0
    for row in data:
        if int(row['age']) in range(start, stop):
            num_customers += 1
        if int(row['age']) in range(start, stop) and row['smoker'] == 'yes':
            num_smokers += 1
    print('The number of smokers aged {} to {} is {} out of {} customers in the same age range, which is {} percent'
          .format(start, stop, num_smokers, num_customers, round((num_smokers/num_customers*100), 2)))

find_age_range_averages_by_age(insurance, 18, 24)
find_age_range_averages_by_age(insurance, 25, 35)
find_age_range_averages_by_age(insurance, 36, 50)
find_age_range_averages_by_age(insurance, 51, 100)

for row in insurance:    
    if row['smoker'] == 'yes':
            smokers_list.append(float(row['charges']))
    if row['smoker'] == 'no':
            non_smokers_list.append(float(row['charges']))
    if row['smoker'] == 'yes':
        total_number_smokers += 1
    if row['smoker'] == 'no':
        total_number_non_smokers += 1

mean_non_smoker_cost = mean(non_smokers_list)
mean_smoker_cost = mean(smokers_list)   
print('The mean cost for smokers is {} times the mean cost of non smokers.'.format(round(mean_smoker_cost / mean_non_smoker_cost, 1)))
# insights on bmi and smoking

def find_relation_bmi_smoking(data):
    smoker_bmi = []
    non_smoker_bmi = []
    for row in data:
        if row['smoker'] == 'yes':
            smoker_bmi.append(float(row['bmi']))
        if row['smoker'] == 'no':
            non_smoker_bmi.append(float(row['bmi']))
    mean_smoker_bmi = round(mean(smoker_bmi), 2)
    mean_non_smoker_bmi = round(mean(non_smoker_bmi), 2)
    print('The mean bmi of smokers is {} compared to a mean of {} for non smokers'
          .format(mean_smoker_bmi, mean_non_smoker_bmi))

find_relation_bmi_smoking(insurance) 

# looking at mean age in each region

def mean_cost_by_region(data, region):
    total_cost_region = []
    for row in data:
        if row['region'] == region:
            total_cost_region.append(float(row['charges']))
    mean_cost_region = round(mean(total_cost_region), 2)
    print('The mean cost for {} is {}'.format(region, mean_cost_region) )
        
mean_cost_by_region(insurance, 'southwest')
mean_cost_by_region(insurance, 'southeast')
mean_cost_by_region(insurance, 'northwest')
mean_cost_by_region(insurance, 'northeast')
 



                    
                               

    
    