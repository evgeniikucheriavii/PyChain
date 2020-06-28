from classes.chain import Chain
from classes.node import Node

root = Node("Hello, World!", "")

chain = Chain(root)

chain.add_node("Hello!")
chain.add_node("World!")
chain.add_node("World!123")
chain.add_node("World!321")
chain.add_node("World!123")

chain.print_nodes()
chain.print_full_nodes()

print(chain.validate())