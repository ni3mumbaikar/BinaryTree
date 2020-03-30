from pprint import pprint;
from node import Node; 

layer_count = 0;
nodereferecne = None;
main_list = [];
temp_layer = [];

class Tree(object):
	def __init__(self, root):
		super(Tree, self).__init__()
		self.root = None;


	def addvalue(self,value):
		global nodereferecne
		if self.root is None:
			nodereferecne = Node(value,None,None);
			self.root=nodereferecne;
			print("Added root with the value "+str(nodereferecne.val)+"\n");
		else :
			if value<nodereferecne.val:
				if nodereferecne.left is not None :
					nodereferecne = nodereferecne.left;
					self.addvalue(value);
				else :
					nodereferecne.left = Node(value,None,None);
					print("added "+str(value)+" to left of "+str(nodereferecne.val));
					nodereferecne = self.root;
			elif value > nodereferecne.val:
				if nodereferecne.right is not None :
					nodereferecne = nodereferecne.right;
					self.addvalue(value);
				else :
					nodereferecne.right = Node(value,None,None);
					print("added "+str(value)+" to right of "+str(nodereferecne.val));
					nodereferecne = self.root;

	def generate_tree(self):
		global layer_count,main_list,temp_layer;
		if layer_count == 0 :
			temp_layer = [self.root];
			main_list.append(temp_layer);
			layer_count += 1;
			temp_layer = [];
			self.generate_tree();
		else:
			# print("else")
			for element in main_list[len(main_list)-1] :
				if element.left  or element.right  :
					if element.left :
						temp_layer.append(element.left);
						print("added left "+ str(element.left.val));
					if element.right :
						temp_layer.append(element.right);
						print("added right "+ str(element.right.val));
					# temp_layer = [];
				else :
					temp_layer = [];
			# checking empty list
			if temp_layer :
				main_list.append(temp_layer);
				temp_layer = [];
				self.generate_tree();
				print("done");
				

	def __str__(self):
		self.generate_tree();
		return str(main_list);















