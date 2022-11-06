import sys 

from pylint import lint  

from typing import TextIO

from pylint.lint import Run

THRESHOLD = 1

default_stdout = sys.stdout
sys.stdout = type("Dummy", (TextIO,), {"write": lambda self, data: ()})()
score1 = Run(["mapquest_parse-json_7.py"], exit=False).linter.stats.global_note
sys.stdout = default_stdout

if score1 < THRESHOLD: 
    print("Linter failed: Score < threshold value") 
    sys.exit(1) 
else:
    print("Code Rating Based on Lint Testing:", score1,"/ 5 \n (((PASSED)))")

sys.exit(0) 