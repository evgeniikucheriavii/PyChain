import hashlib

class Node:
	data = ""
	clear_data = ""
	previous_hash = ""
	hash = ""
	next = None
	splitter = "__splitter__"

	def __init__(self, data, previous_hash):
		self.clear_data = data
		self.previous_hash = previous_hash
		self.data = previous_hash + self.splitter + data
		self.hash = hashlib.sha256(bytearray(self.data, "UTF-8")).hexdigest()

	def check(self, previous):
		if(previous != None):
			if(previous.hash == self.previous_hash):
				return True
			else:
				return False
		else:
			return False

