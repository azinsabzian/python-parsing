# class_parser.py

import ast
import json

class PythonClassParser:
  """
    Define class.
    """
    def __init__(self, filename):
        self.filename = filename
        self.tree = self._parse_file()

    def _parse_file(self):
      """
        Reads the Python file and parses its contents into an AST.
        """
        
        with open(self.filename, "r") as file:
            file_content = file.read()
        return ast.parse(file_content)

    def extract_classes(self):
       """
        Extracts information.
        """
        classes = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        methods.append({
                            "name": item.name,
                            "params": [arg.arg for arg in item.args.args],
                            "docstring": ast.get_docstring(item),
                        })
                class_info = {
                    "name": node.name,
                    "inherits": [base.id for base in node.bases] if node.bases else [],
                    "docstring": ast.get_docstring(node),
                    "methods": methods,
                }
                classes.append(class_info)
        return classes

    def parse(self):
        return {
            "file": self.filename,
            "classes": self.extract_classes(),
        }

if __name__ == "__main__":
  # Instance
    parser = PythonClassParser("student_info.py")
    parsed_data = parser.parse()

    print(json.dumps(parsed_data, indent=4))
