from .node import Node

class Chain:
	root = None

	def __init__(self, root):
		self.root = root
	
	def add_node(self, data):
		
		current_node = self.root

		while current_node.next is not None:
			current_node = current_node.next
		
		current_node.next = Node(data, current_node.hash)

	def print_nodes(self):
		current_node = self.root

		while current_node is not None:
			print(current_node.clear_data)
			current_node = current_node.next
	
	def print_full_nodes(self):
		current_node = self.root

		while current_node is not None:
			print(current_node.hash + " | " + current_node.clear_data)
			current_node = current_node.next