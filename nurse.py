from db_bulk_load import nurse_lookup_fp

class Nurse(object):
	"""Nurse class. Initialized by fingerprint md5 hash"""

	def __init__(self, fingerprint):
		self.fingerprint = fingerprint
		self.fp_lookup = nurse_lookup_fp(fingerprint)
		if self.fp_lookup != None:
			for e in self.fp_lookup.items():
				setattr(self, e[0], e[1])

	# def exists(self):
	# 	return self.fp_lookup != None

	# def set_attrs(self):
	# 	for e in n1.fp_lookup.items():
	# 		setattr(self, e[0], e[1])
