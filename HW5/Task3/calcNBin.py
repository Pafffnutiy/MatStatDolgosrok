import math

from scipy.stats import norm


alpha = 0.01
beta  = 0.99

theta0 = 0.5
theta1 = 0.53

talpha = norm.ppf(alpha)
tbeta = norm.ppf(beta)

pt1 = tbeta*math.sqrt(theta1*(1-theta1))
pt2 = talpha*math.sqrt(theta0*(1-theta0))

denom = math.sqrt(71)*(theta0-theta1)

n = math.ceil(math.pow((pt1-pt2)/denom, 2))

print(f'{talpha}, {tbeta}, {pt1}, {pt2}, {n}')