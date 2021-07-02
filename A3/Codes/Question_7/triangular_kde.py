import csv
import scipy.stats

filename = 'a3_q7.csv'
data = []
with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(float(row[1]))

data = data[1:]

def triangular_kde(x, h, D = data):
    sum_Ku = 0;

    for xi in D:
        u = ((float)(x-xi))/h

        ku = 0
        abs_u = abs(u)
        if (abs_u <= 1):
            ku = 1-abs_u
            
        sum_Ku = sum_Ku + ku
    
    n = len(D)
    nh = n*h
    kde_pdf = sum_Ku/nh

    return kde_pdf