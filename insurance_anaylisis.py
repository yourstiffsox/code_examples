import os
import csv
from statistics import mean

# initiate list to hold data
insurance = []
# initiate variables to hold smoker data


total_age_smokers = 0

#Create a list of dictionaries to hold the data
 
os.chdir('/Users/ryanw/OneDrive/desktop')
with open('insurance.csv') as file:
    for line in csv.DictReader(file):
        insurance.append(line)

# insights on smokers
#define function to give a percent proportion of smokers by region
#and return a string describing the relation
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
    
#define a function to find the percentage of smokers in an age range
#and return a string describing the relation
def percent_smoker_by_age(data, start, stop):
    num_customers = 0
    num_smokers = 0
    for row in data:
        if int(row['age']) in range(start, stop):
            num_customers += 1
        if int(row['age']) in range(start, stop) and row['smoker'] == 'yes':
            num_smokers += 1
    print('The number of smokers aged {} to {} is {} out of {} customers in the same age range, which is {} percent'
          .format(start, stop, num_smokers, num_customers, round((num_smokers/num_customers*100), 2)))

#find the average cost for smokers and non smokers
#and then print a discription of the relationship
def mean_smoker_cost(data):
    total_number_smokers = 0
    total_number_non_smokers = 0
    smokers_list = []
    non_smokers_list = []
    for row in data:    
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

#define a function comparing smoking and bmi
#then return a string describing the relationship
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

# define a function comparing cost and region
# and return the mean cost for a region
def mean_cost_by_region(data, region):
    total_cost_region = []
    for row in data:
        if row['region'] == region:
            total_cost_region.append(float(row['charges']))
    mean_cost_region = round(mean(total_cost_region), 2)
    print('The mean cost for {} is {}'.format(region, mean_cost_region) )

def main():
    #call the smokers by region function for each region
    smokers_by_region(insurance, 'southwest')
    smokers_by_region(insurance, 'southeast')
    smokers_by_region(insurance, 'northwest')
    smokers_by_region(insurance, 'northeast')
    
    #call the smoker by age function for each age range
    percent_smoker_by_age(insurance, 18, 24)
    percent_smoker_by_age(insurance, 25, 35)
    percent_smoker_by_age(insurance, 36, 50)
    percent_smoker_by_age(insurance, 51, 100)
    #find the average cost for smokers and non smokers
    #and then print a discription of the relationship
    
    #call the find bmi smoking relation function
    find_relation_bmi_smoking(insurance)
 
    # call smoker by region function for each region
    mean_cost_by_region(insurance, 'southwest')
    mean_cost_by_region(insurance, 'southeast')
    mean_cost_by_region(insurance, 'northwest')
    mean_cost_by_region(insurance, 'northeast')
    #call mean smoker cost function
    mean_smoker_cost(insurance)
if __name__ == '__main__':
    main()
                    
                               

    
    