import sys 

from pylint import lint  

from typing import TextIO

from pylint.lint import Run

THRESHOLD = 5

default_stdout = sys.stdout
sys.stdout = type("Dummy", (TextIO,), {"write": lambda self, data: ()})()
score = Run(["mapquest_parse-json_7.py"], exit=False).linter.stats.global_note
sys.stdout = default_stdout

if score < THRESHOLD: 
    print("Code Rating Based on Lint Testing:", score,"\n (((FAILED TEST)))") 
    sys.exit(1) 
else:
    print("Code Rating Based on Lint Testing:", score,"\n (((PASSED TEST)))")

sys.exit(0) 