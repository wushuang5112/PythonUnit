import unittest


class ClassOneInPart1(unittest.TestCase):
    def setUp(self):
        print "init class One in Part 1."
    def tearDown(self):
        print "finish class One in Part 1."
    def testclassOneStepOne(self):
        print "do jobs in Part1Class1Step1"
    def testclassOneStepTwo(self):
        print "Do jobs in Part1Class1Step2"

class ClassTwoInPart1(unittest.TestCase):
    def setUp(self):
        print "init class Two in Part 1."
    def tearDown(self):
        print "finish class Two in Part 1."
    def testclassOneStepOne(self):
        print "do jobs in Part1Class2Step1"
    def testclassOneStepTwo(self):
        print "Do jobs in Part1Class2Step2"

if __name__ == "__main__":
    unittest.main()


