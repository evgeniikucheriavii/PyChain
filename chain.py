import hashlib

class Node:
	data = ""
	hash = ""
	next = None
	splitter = "__splitter__"

	def __init__(self, data, previous_hash):
		self.data = previous_hash + self.splitter + data
		self.hash = self.get_hash()

	def check(self, previous):
		if(previous != None):
			if(previous.get_hash() == self.get_previous_hash()):
				return True
			else:
				return False
		else:
			return True

	def get_clear(self):
		vals = self.data.split(self.splitter)
		if(len(vals) == 1):
			return vals[0]
		else:
			return vals[1]

	def get_previous_hash(self):
		vals = self.data.split(self.splitter)
		if(len(vals) == 1):
			return ""
		else:
			return vals[0]
	
	def get_hash(self):
		return hashlib.sha256(bytearray(self.data, "UTF-8")).hexdigest()

class Chain: 
	root = None

	def __init__(self, root):
		self.root = root
	
	def add_node(self, data):
		if(not self.validate()):
			print("Chain is corrupted! Node adding aborted")
			return
		
		current_node = self.root

		while current_node.next is not None:
			current_node = current_node.next
		
		current_node.next = Node(data, current_node.get_hash())

	def print_nodes(self):
		current_node = self.root

		print("Nodes: ")

		while current_node is not None:
			print(current_node.get_clear())
			current_node = current_node.next
	
	def print_full_nodes(self):
		current_node = self.root

		print("Nodes with hashes: ")

		while current_node is not None: 
			print(current_node.get_previous_hash() + " | " + current_node.get_clear())
			current_node = current_node.next
	
	def validate(self):
		previous = None
		current_node = self.root

		while current_node is not None:
			if(current_node.check(previous)):
				previous = current_node
				current_node = current_node.next
			else:
				return False

		return True