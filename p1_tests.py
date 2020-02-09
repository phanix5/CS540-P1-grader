import unittest
from p1_statespace import fill,empty,xfer,succ

class TestP1(unittest.TestCase):

    ## fill method
    def testFill(self):
        maxs= [5,7]
        state=[1,1]
        self.assertEqual(fill(state,maxs,0),[5,1],'wrong output from fill')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[1,1],'state list modified')
        state=[1,1]
        self.assertEqual(fill(state,maxs,1),[1,7],'wrong output from fill')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[1,1],'state list modified')
        state=[1,7]
        self.assertEqual(fill(state,maxs,1),[1,7],'wrong output from fill')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[1,7],'state list modified')
        state=[5,7]
        self.assertEqual(fill(state,maxs,0),[5,7],'wrong output from fill')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[5,7],'state list modified')

    def testEmpty(self):
        maxs= [5,7]
        state=[1,1]
        self.assertEqual(empty(state,maxs,0),[0,1],'wrong output from empty')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[1,1],'state list modified')
        state=[1,1]
        self.assertEqual(empty(state,maxs,1),[1,0],'wrong output from empty')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[1,1],'state list modified')
        state=[1,7]
        self.assertEqual(empty(state,maxs,1),[1,0],'wrong output from empty')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[1,7],'state list modified')
        state=[5,7]
        self.assertEqual(empty(state,maxs,0),[0,7],'wrong output from empty')
        self.assertEqual(maxs,[5,7],'max list modified')
        self.assertEqual(state,[5,7],'state list modified')
    
    def testXfer(self):
        maxs=[21,25]
        state=[5,10]
        self.assertEqual(xfer(state,maxs,0,1),[0,15],"xfer output wrong")
        self.assertEqual(maxs,[21,25],'max list modified')
        self.assertEqual(state,[5,10],'state list modified')
        self.assertEqual(xfer(state,maxs,1,0),[15,0],"xfer output wrong")
        self.assertEqual(maxs,[21,25],'max list modified')
        self.assertEqual(state,[5,10],'state list modified')
        state=[10,20]
        self.assertEqual(xfer(state,maxs,0,1),[5,25],"xfer output wrong")
        self.assertEqual(maxs,[21,25],'max list modified')
        self.assertEqual(state,[10,20],'state list modified')
        self.assertEqual(xfer(state,maxs,1,0),[21,9],"xfer output wrong")
        self.assertEqual(maxs,[21,25],'max list modified')
        self.assertEqual(state,[10,20],'state list modified')
        maxs=[20,25]
        state=[20,25]
        self.assertEqual(xfer(state,maxs,0,1),[20,25],"xfer output wrong")
        self.assertEqual(maxs,[20,25],'max list modified')
        self.assertEqual(state,[20,25],'state list modified')
        self.assertEqual(xfer(state,maxs,1,0),[20,25],"xfer output wrong")
        self.assertEqual(maxs,[20,25],'max list modified')
        self.assertEqual(state,[20,25],'state list modified')

    


if __name__ == '__main__':
    unittest.main()

