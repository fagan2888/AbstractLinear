from lin_op import LinearOp

class add(LinearOp):
	"""Summing arguments.
	"""
	def __init__(self, *args):
		self.shape = args[0].shape
		for arg in args[1:]:
			self.shape += arg.shape
		super(add, self).__init__(*args)

	def op_mul(self, *expr_vals):
		return sum(expr_vals)

	def op_tmul(self, expr_val):
		return expr_val
