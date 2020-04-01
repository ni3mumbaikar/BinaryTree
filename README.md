# BinaryTree
  In computer science, a [binary tree][1] is a  hierarchical data structure in which each node has at most two children, which are referred to as the left child and the right child.

## Binary Tree.py
The only file you need to execute as the logic is hidden in other files :)

## node.py
  Just a simple class implementation to represent a node in the tree.

## tree.py
  Representation of a binary tree or network which consists of objects of node class. This file responsible for almost everything core happens on tree e.g.
 - Add new values (**with addvalue()**)
 - Search
 - Traversal

## addvalue()
  This is a function inside tree.py responsible for adding values inside the tree based on binary tree standards.
The values of nodes are hardcoded for now will update soon.

## search()
  Search values inside tree with just node reference using binary search algo. To know more on how binary search works check [this][2] link.

## traverse() or visit()
  traverse() is wrapper method in tree.py for visit() which is present in node.py responsible to visit each and every node of the tree or sort it in ascending order

[1]:https://en.wikipedia.org/wiki/Binary_tree
[2]:https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
