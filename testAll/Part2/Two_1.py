import unittest


class ClassOneInPart2(unittest.TestCase):
    def setUp(self):
        print "init class One in Part 2."
    def tearDown(self):
        print "finish class One in Part 2."
    def testclassOneStepOne(self):
        print "do jobs in Part2Class1Step1"
    def testclassOneStepTwo(self):
        print "Do jobs in Part2Class1Step2"

class ClassTwoInPart2(unittest.TestCase):
    def setUp(self):
        print "init class Two in Part 2."
    def tearDown(self):
        print "finish class Two in Part 2."
    def testclassOneStepOne(self):
        print "do jobs in Part2Class2Step1"
    def testclassOneStepTwo(self):
        print "Do jobs in Part2Class2Step2"

if __name__ == "__main__":
    unittest.main()
