from lin_op import LinearOp
import utilities as u
import numpy as np

class index(LinearOp):
	"""Indexing into an expression.
	"""
	def __init__(self, expr, row_slc, col_slc):
		self.row_slc = row_slc
		self.col_slc = col_slc
		rows = self._get_slice_len(expr.size[0], row_slc)
		cols = self._get_slice_len(expr.size[1], col_slc)
		self.shape = u.Shape(rows, cols)
		super(index, self).__init__(expr)

	def _get_slice_len(self, expr_dim, slc):
		selection = range(expr_dim)[slc]
		if isinstance(selection, list):
			return len(selection)
		else: # Integer.
			return 1

	def op_mul(self, expr_val):
		return expr_val[self.row_slc, self.col_slc]

	def op_tmul(self, expr_val):
		result = np.mat(np.zeros(self.args[0].size))
		result[self.row_slc, self.col_slc] = expr_val
		return result
