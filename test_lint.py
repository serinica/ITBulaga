import sys 

from pylint import lint  

from typing import TextIO

from pylint.lint import Run

THRESHOLD = 9  

run = lint.Run(["mapquest_parse-json_7.py"], do_exit=False) 

score = run

default_stdout = sys.stdout
sys.stdout = type("Dummy", (TextIO,), {"write": lambda self, data: ()})()
score1 = Run(["mapquest_parse-json_7.py"], exit=False).linter.stats.global_note
sys.stdout = default_stdout

if score1 < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 