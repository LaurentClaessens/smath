from scipy import stats

X=stats.binom(5,0.25)

for k in range(0,6):
    print(k,X.cdf(k))

