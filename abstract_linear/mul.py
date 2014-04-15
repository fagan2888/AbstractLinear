from lin_op import LinearOp
import utilities as u

class mul(LinearOp):
	"""Multiplication by a matrix.

	mat: The matrix (a Numpy matrix).
	expr: The expression multiplied by the matrix.
	"""
	def __init__(self, mat, expr):
		self.mat = mat
		mat_shape = u.Shape(*mat.shape)
		self.shape = mat_shape*expr.shape
		super(mul, self).__init__(expr)

	def op_mul(self, expr_val):
		return self.mat * expr_val

	def op_tmul(self, expr_val):
		return self.mat.T * expr_val
