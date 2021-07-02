import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

q2_sigma3 = pd.read_csv("q2_sigma3.dat", header = None)
q2_sigma100 = pd.read_csv("q2_sigma100.dat", header = None)
df = pd.DataFrame(columns=['Mean', 'Variance'])

def append_normal_to_plot(mean, variance):
    sigma = np.sqrt(variance)
    x = np.linspace(mean - 6 * sigma, mean + 6 * sigma, 100)
    y = stats.norm.pdf(x, mean, sigma)
    plt.plot(x, y, label = "Posterior" + str(len(df)))

def process_bayesian(data, sigma):
    #prior_0 s
    a_0 = 0
    b_squared_0 = 1
    
    #prior i, start with prior_0 s
    a_i = a_0
    b_squared_i = b_squared_0
    
    for i, row in data.iterrows():
        #observe and get posterior
        #result from Question 1
        se_squared = (sigma ** 2) / row.size
        
        x = (b_squared_i * row.mean() + se_squared * a_i) / (b_squared_i + se_squared)
        y_squared = (b_squared_i * se_squared) / (b_squared_i + se_squared)
        
        #add mean and variance to table
        #append the normal curve to the plot
        df.loc[i] = [x] + [y_squared]
        append_normal_to_plot(x, y_squared)
        
        #update prior to posterior for next step
        a_i = x
        b_squared_i = y_squared
    
    #plot the posteriors
    plt.title('Posterior distributions for sigma = ' + str(sigma))
    plt.gca().set(xlabel = 'X_i', ylabel = 'Posterior')
    plt.legend(loc = "upper right")
    plt.show()
    
    #print the mean variance table
    print('\n')
    print(df.to_string(index = False))

def main():
    #process bayesian trials for the data sheets given
    process_bayesian(q2_sigma3, 3)
    df.drop(df.index, inplace=True)
    process_bayesian(q2_sigma100, 100)
  
if __name__ == "__main__":
    main()
