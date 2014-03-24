from dbTools import nurse_lookup_fp
import json
import base64

class Nurse(object):
	"""Nurse class. Initialized by fingerprint md5 hash"""

	def __init__(self, fingerprint):
		self.fingerprint_hash = fingerprint
		self.fp_lookup = nurse_lookup_fp(fingerprint)
		if self.fp_lookup != None:
			for e in self.fp_lookup.items():
				setattr(self, e[0], e[1])
			self.dob = str(self.dob)	#need to convert date object to string object so it can be serialized
			self.fp_lookup = None

	def make_json(self):
		"""
		Dumps the pertinent nurse attributes into a JSON hash table
		Returns the JSON string object
		If the photo id has not been encoded, returns False
		"""
		if self.id_photo_format != 'base64':
			return false
		json_data = json.dumps({'name':self.name,
								'fingerprint_hash':self.fingerprint_hash,
								'dob':self.dob,
								'village':self.village,
								'gender':self.gender,
								'id_photo':self.id_photo,
								'id_photo_format':self.id_photo_format
								})
		return json_data

	def encode_photo(self):
		self.id_photo = base64.b64encode(self.id_photo)
		self.id_photo_format = 'base64'
		return
	#def pack(self):
	#	self.id_photo = str(self.id_photo)
	# def exists(self):
	# 	return self.fp_lookup != None

	# def set_attrs(self):
	# 	for e in n1.fp_lookup.items():
	# 		setattr(self, e[0], e[1])

#Dummy fingerprint: 00372a6fb1a467b54992df4daf0dfa49