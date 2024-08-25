# testing the class functionality
import unittest
from class_parser import ClassInspector

class TestClassInspector(unittest.TestCase):
    
    def setUp(self):
        self.parser = ClassInspector("student_info.py")


    def test_class_name(self):
        """
        Testing class name.
        """
        classes = self.parser.find_classes()
        self.assertEqual(classes[0]['class_name'], "Student")


    def test_method_names(self):
        """
        Test method names.
        """
        classes = self.parser.find_classes()
        method_names = [method['name'] for method in classes[0]['methods']]
        self.assertIn("__init__", method_names)
        self.assertIn("get_student_info", method_names)

    
    def test_output_structure(self):
        """
        Testing report structure.
        """
        report = self.parser.generate_report()
        self.assertIn("filename", report)
        self.assertIn("classes", report)
        self.assertEqual(report['filename'], "student_info.py")

if __name__ == "__main__":
    unittest.main()
