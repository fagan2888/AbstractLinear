from abstract_linear import *
import numpy as np

n = 2
ones = np.mat(np.ones((n, n)))

x = Variable(n, n)
A = np.matrix("1 2; 3 4")
expr = mul(A, x)


val_dict = {x.id: ones}

result = expr.mul(val_dict)
assert (result == A*ones).all()

result = expr.tmul(result)
assert (result[x.id] == A.T*A*ones).all()

y = Variable(n, n)
expr = add(y, expr)
val_dict = {x.id: np.ones((n, n)),
			y.id: np.ones((n, n))}

result = expr.mul(val_dict)
assert (result == A*ones + ones).all()

result_dict = expr.tmul(result)
assert (result_dict[y.id] == result).all()
assert (result_dict[x.id] == A.T*result).all()

val_dict = {x.id: A,
			y.id: A}

expr = add(x[:, 0], y[:, 1])
result = expr.mul(val_dict)
assert (result == A[:, 0] + A[:, 1]).all()

result_dict = expr.tmul(result)
mat = ones
mat[:, 0] = result
mat[:, 1] = 0
assert (result_dict[x.id] == mat).all()

val_dict = {x.id: A}
expr = neg(x)

result = expr.mul(val_dict)
assert (result == -A).all()

result_dict = expr.tmul(result)
assert (result_dict[x.id] == A).all()