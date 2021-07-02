import csv
import scipy.stats

filename = 'a3_q7.csv'
data = []
with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(float(row[1]))

data = data[1:]

def normal_kde(x, h, D = data):
    sum_Ku = 0;
    std_normal = scipy.stats.norm(0, 1)

    for xi in D:
        u = ((float)(x-xi))/h

        ku = std_normal.pdf(u)
        
        sum_Ku = sum_Ku + ku
    
    n = len(D)
    nh = n*h
    kde_pdf = sum_Ku/nh

    return kde_pdf