from db_bulk_load import nurse_lookup_fp

class Nurse(object):
	"""Nurse class. Initialized by fingerprint md5 hash"""

	def __init__(self, fingerprint):
		self.fingerprint = fingerprint
		self.fp_lookup = nurse_lookup_fp(fingerprint)

	def exists(self):
		return self.fp_lookup != None

	# if exists() == True:
	# 	self.name