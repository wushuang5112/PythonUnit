from Tkinter import Widget
import unittest
# ִ�в��Ե���
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
    def testResize(self):
        self.widget.resize(100, 100)        
        self.assertEqual(self.widget.getSize(), (100, 100))        
# ����
if __name__ == "__main__":
    # ������Լ�
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    
    # ִ�в���
    runner = unittest.TextTestRunner()
    runner.run(suite)