ff_SR = lambda s, r, q : (q and not r) or s
ff_JK = lambda j, k, q : (q and not k) or (j and not q)
ff_D  = lambda d, q, x : d
ff_T  = lambda t, q, x : (t and not q) or (not t and q)


if __name__ == "__main__":
	x = [int(item) for item in input('').split()]
	print("Qnext: " + str(ff_D(x[0], x[1], x[2])))
