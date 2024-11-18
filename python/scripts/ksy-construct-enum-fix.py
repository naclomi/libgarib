#!/usr/bin/env python3
import ast
import sys


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.funcs = []
        self.imports = []

    def last_import(self):
        return max(i[1] for i in self.imports)

    def visit_Import(self, n):
        self.imports.append((n.lineno-1, n.end_lineno))

    def visit_ImportFrom(self, n):
        self.imports.append((n.lineno-1, n.end_lineno))

    def visit_FunctionDef(self, n):
        if n is not None:
            self.funcs.append((n.name, n.lineno-1, n.end_lineno))

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        with open(filename, "r") as f:
            input_code = f.read()
        tree = ast.parse(input_code)
        input_lines = input_code.split("\n")
        analyzer = Analyzer()
        analyzer.visit(tree)
        output_lines = []

        for idx in range(0, analyzer.last_import()):
            output_lines.append(input_lines[idx])
            input_lines[idx] = None
        output_lines.append("")
        for func in analyzer.funcs:
            for idx in range(func[1], func[2]):
                output_lines.append(input_lines[idx])
                input_lines[idx] = None
            output_lines.append("")
        for line in input_lines:
            if line is not None:
                output_lines.append(line)
        with open(filename, "w") as f:
            f.write("\n".join(output_lines))
