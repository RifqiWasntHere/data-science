from treelib import Tree

tree = Tree()

tree.create_node("Safety [low] unacc", "parent1")  # No parent means its the root node
tree.create_node("Jane",  "jane"   , parent="parent1")
tree.create_node("Safety [med] acc",  "bill"   , parent="parent1")
tree.create_node("Diane", "diane"  , parent="bill")
tree.create_node("Mary",  "mary"   , parent="diane")
tree.create_node("Mark",  "mark"   , parent="jane")

tree.show()