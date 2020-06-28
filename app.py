from chain import Chain
from chain import Node

root = Node("First node", "")

chain = Chain(root)

chain.add_node("Second node")
chain.add_node("Thrird node")
chain.add_node("Fourth node")
chain.add_node("Fiveth node")
chain.add_node("Sixth node")

chain.print_nodes()
print()
chain.print_full_nodes()
print()

print("Is valid: " + str(chain.validate()))

chain.root.next.next.data = "sdads"

chain.print_nodes()

print("Is valid: " + str(chain.validate()))

chain.add_node("Seventh node")