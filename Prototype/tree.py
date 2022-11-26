from treelib import Tree

def iterasi1():
  tree = Tree()
  node = tree.create_node
  node("Root", "root")
  node("Safety [Low]", "left", parent = "root")
  node("Safety [Med,High]", "right", parent = "root")
  tree.show()

def iterasi2():
  tree = Tree()
  node = tree.create_node
  node("Root", "root")
  node("Safety [Low] unacc", "left", parent = "root")
  node("Safety [Med,High]", "right", parent = "root")
  tree.show()

def iterasi3():
  tree = Tree()
  node = tree.create_node
  node("Root", "root")
  node("Safety [Low] unacc", "left", parent = "root")
  node("Safety [Med,High]", "right", parent = "root")
  node("Safety [High ]", "left2", parent ="right")
  node("Safety [Med ]", "right2", parent ="right")
  tree.show()

def iterasi4():
  tree = Tree()
  node = tree.create_node
  node("Root", "root")
  node("Safety [Low] unacc", "left", parent = "root")
  node("Safety [Med,High]", "right", parent = "root")
  node("Safety [High]", "right2", parent ="left")
  node("Safety [Med]", "left2", parent ="left")
  node("Lugage [Small]", "left3", parent ="left2")
  node("Lugage [Med,High]", "right3", parent ="left2")
  tree.show()