def c(p,r,t):
	if t==0:
		return p
	else:
		return c(p+(p*r)/100,r,t-1)
print(c(1000,10,2))
