#"25 30 16 150 90 0 200 -12 55 -13 1 2 3"
class tnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bstree:
    def __init__(self):
        self.root=None
    def insert(self,val):
        t=self.root
        if self.root is None:
            self.root=tnode(val)
        elif val>self.root.data:
            self.root=self.root.right
            self.insert(val)
        elif val<self.root.data:
            self.root=self.root.left
            self.insert(val)
                
        self.root=t
        return

    def inorder(self):
        self.ino(self.root)
    def ino(self,root):       
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

        


        

a=list(map(int,("25 30 16 150 90 0 200 -12 55 -13 1 2 3").split()))
print(a)
b=bstree()
for i in a:
    b.insert(i)
b.inorder()
