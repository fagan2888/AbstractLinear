import types

class LinearOp(object):
	def __init__(self, *args):
		self.args = args

	def mul(self, val_dict):
		"""Multiply by the given variables.
		"""
		eval_args = []
		for arg in self.args:
			eval_args.append(arg.mul(val_dict))
		return self.op_mul(*eval_args)

	def tmul(self, value):
		"""Multiply the transpose by the given value.
		"""
		result = self.op_tmul(value)
		val_dict = {}
		for arg in self.args:
			val_dict.update(arg.tmul(result))
		return val_dict

	def __getitem__(self, key):
		return types.index()(self, key[0], key[1])

	@property
	def size(self):
		return self.shape.size
