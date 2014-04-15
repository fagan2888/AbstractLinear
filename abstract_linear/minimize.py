def add_dicts(lh_dict, rh_dict, alpha):
	"""lh_dict + alpha*rh_dict
	"""
	result = {}
	for key, val in lh_dict.items():
		val += alpha*rh_dict.get(key, 0)
		result[key] = val
	return result

def minimize(sum_sq_terms):
	"""Solves the least-squares problem using CG.
	"""
	obj = sum_sq_terms[0]
	A = obj.A
	b = obj.b
	# CG algorithm.
	x = {} # x0 = 0
	r = add_dicts(b, A.mul(x), -1)
	p = r
	# k = 0
	# while True:
	# 	pass
