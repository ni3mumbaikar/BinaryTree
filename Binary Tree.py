from node import Node;
from tree import Tree;

def main() :
	mylist = [10,3,9,12,31,27,25,4,5];
	my_tree = Tree(None);
	for element in mylist :
			my_tree.addvalue(element);

	print(my_tree);
main();