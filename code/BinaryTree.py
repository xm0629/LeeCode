# Python3.6 实现二叉树算法

import numpy as np


class BinaryTree(object):
    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def setRoot(self, rootobj):
        self.root = rootobj

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.leftChild = self.leftChild
            self.leftChild = tree

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.rightChild = self.rightChild
            self.rightChild = tree

    def getRootCell(self):
        return self.root

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
#
#    def preOrder(self):
#        print(self.root)
#        if self.leftChild:
#            self.leftChild.preOrder()
#        if self.rightChild:
#            self.rightChild.preOrder()
#

# test data 
if __name__ == "__main__":
    tree = BinaryTree('a')
    print(tree.getRootCell())
    tree.insertLeft('b')
    print(tree.getLeftChild().getRootCell())
    tree.insertRight('c')
    print(tree.getLeftChild().getRootCell())
    tree.getLeftChild().setRoot('d')
    print(tree.getLeftChild().getRootCell())


# 二叉树的前序遍历、中序遍历、后序遍历

