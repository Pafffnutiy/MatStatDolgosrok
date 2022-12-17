import math

from scipy.stats import norm


alpha = 0.1
beta = 0.9
theta0 = 8
theta1 = 9

talpha = norm.ppf(alpha)
tbeta = norm.ppf(beta)

num = tbeta*theta1 - talpha*theta0

denom = theta0-theta1

n = math.ceil(math.pow(num/denom, 2))

print(f'n = {n}')