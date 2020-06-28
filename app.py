from chain import Chain
from chain import Node

# Initializing Chain with a first node
chain = Chain(Node("First node", ""))

#Adding nodes
chain.add_node("Second node")
chain.add_node("Thrird node")
chain.add_node("Fourth node")
chain.add_node("Fiveth node")
chain.add_node("Sixth node")

#Printing clear data of every node
chain.print_nodes()
print()
#Printing full data: previous hash and current data
chain.print_full_nodes()
print()

#Validationg chain
print("Is valid: " + str(chain.validate()))

chain.add_node("Second node")

print(chain.find("Sixth node").data)
print(chain.find_all("Second node"))

#Making changes
chain.root.next.next.data = "sdads"

#Now chain could not be validated - because data was changed
print("Is valid: " + str(chain.validate()))

#You can't add nodes to a corrupted chain
chain.add_node("Seventh node")