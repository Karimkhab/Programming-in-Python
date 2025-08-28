# Karim Khabibrakhmanov
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO


class IndexException(Exception):
    '''
    Exception class for incorrect indexes
    '''
    def __init__(self, index: int):
        self.index = index


    def exception(self):
        '''
        Method for error output
        '''
        print(f"Invalid index: {self.index}.")


class CodeCell:
    '''
    Сlass that implements interface of a Python Notebook Cell
    '''
    def __init__(self, code : str, global_vars):
        self.code = code
        self.output = []

        if global_vars is not None:
            self.global_vars = global_vars
        else:
            self.global_vars = {}


    def execute(self):
        '''
        Method that executes the code Cell
        At the same time, it uses global variables created before
        '''

        # For StringIO Сlass from io library, I used this link:
        # https://www.geeksforgeeks.org/python/stringio-module-in-python/
        executionPy = StringIO()
        errorPy = StringIO()

        try:

            # For redirect_stdout and redirect_stderr Сlasses from contextlib library, I used this link:
            # https://docs.python.org/3/library/contextlib.html
            with redirect_stdout(executionPy), redirect_stderr(errorPy):

                # For built-in exec() function from the standard library, I used this link:
                # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-exec/
                exec(self.code, {}, self.global_vars)

        except Exception as e:
            self.output.append(str(e))

        # Adding output to the sheet if there is output
        # if not then error output
        stdout = executionPy.getvalue()
        stderr = errorPy.getvalue()
        if stdout:
            self.output.append(stdout)
        if stderr:
            self.output.append(stderr)

    def clear_output(self):
        '''
        Method that cleans the output
        '''
        self.output = []

    def disp_output(self):
        '''
        Method that displays the output if there is one
        '''
        if self.output:
            # More beautiful output display
            for line in self.output[-1].split("\n"):
                print('\t',line)
        else:
            pass


class PythonNotebook:
    '''
    Сlass that implements interface of a Python Notebook Cell
    '''
    def __init__(self):
        self.cells = []
        self.global_vars = {}

    def check_index(self, index):
        '''
        Method for checking Index whether cell exists
        '''
        if not (0 <= index < len(self.cells)):
            raise IndexException(index).exception()

    def add_cell(self, code : str):
        '''
        Method that adds new Cell
        '''
        if self.cells:
            global_vars = self.cells[-1].global_vars
        else:
            global_vars = self.global_vars

        self.cells.append(CodeCell(code, global_vars))

    def execute_cell(self, index : int):
        '''
        Method that executes new Cell
        '''
        self.check_index(index) # Checking validity of index

        self.cells[index].execute()

        self.global_vars.update(self.cells[index].global_vars) # Update global variables

    def clear_output_cell(self, index : int):
        '''
        Method that clears output Cell
        '''
        self.check_index(index) # Checking validity of index

        self.cells[index].clear_output()

    def clear_all_output(self):
        '''
        Method that clears all output Cell
        '''
        for cell in self.cells:
            cell.clear_output()
        self.global_vars = {}

    def show_output(self, index : int):
        '''
        Method that displays the output Cell
        '''
        self.check_index(index) # Checking validity of index

        print(f'Output ({index}): ')
        self.cells[index].disp_output()

    def show_all_output(self):
        '''
        Method that displays all output Cell
        '''
        for index in range(len(self.cells)):
            self.show_output(index)


notebook = PythonNotebook()
notebook.add_cell("x = 2\ny = 3\nprint(x+y)")
notebook.add_cell("print(x+y)")
notebook.execute_cell(0)
notebook.show_output(0)
