'''
The case of relative import problem 1

if we run...
    (case1) python main.py
    >> from .classDir.classB import B
       ModuleNotFoundError: No module named '__main__.classDir'; '__main__' is not a package

    (case1) python -m main
    >> from .classDir.classB import B
       ImportError: attempted relative import with no known parent package

    (import_trap) python -m case1.main
    >> sucess

explain:
    The relative import will be sucessful only in the subdirectory of current directory.
    if we execute code in case1 directory, the import in case1 directory level (main.py import .classDir) will not work.
    (but the import within classDir work).

    Thus the code with relative import should be executed in module way (python -m <module>).

'''
from .classDir.classB import B

b = B('Same', 178, 'blue')
b.printNameNSize()
b.printColor()







