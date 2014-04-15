from lin_op import LinearOp

class neg(LinearOp):
	"""Negating an expression.
	"""
	def __init__(self, expr):
		self.shape = expr.shape
		super(neg, self).__init__(expr)

	def op_mul(self, expr_val):
		return -expr_val

	def op_tmul(self, expr_val):
		return -expr_val
