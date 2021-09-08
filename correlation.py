import csv
import numpy as np

def getDataSource(data_path):
    cups_of_coffee=[]
    average_hours_slept=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            average_hours_slept.append(float(row["sleep in hours"]))
    
    return{"x":cups_of_coffee,"y":average_hours_slept}

def findCorrelation(datasource): 
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between Cups of Coffee and Average Hours of Sleep:- \n--->",correlation[0,1]) 
    
def setup(): 
    data_path = "cups of coffee vs hours of sleep.csv" 
    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 
    
setup()