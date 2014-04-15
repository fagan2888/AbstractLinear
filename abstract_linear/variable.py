from lin_op import LinearOp
import utilities as u

class Variable(LinearOp):
	"""A variable.
	"""
	# Global ID counter.
	VAR_ID = 0

	def __init__(self, rows=1, cols=1):
		self.shape = u.Shape(rows, cols)
		self.id = Variable.VAR_ID
		Variable.VAR_ID += 1
		super(Variable, self).__init__()

	def mul(self, val_dict):
		"""Retrieve the value corresponding to id.
		"""
		return val_dict.get(self.id, 0)

	def tmul(self, value):
		"""Add value to dict under id.
		"""
		return {self.id: value}
