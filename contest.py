import os
import sys

type_dt = {"b": "beginner", "r": "regular", "g": "grand"}
url = sys.argv[1]
contest_type = type_dt[url.split("/")[-1][1]]
contest_numb = url.split("/")[-1][3:]
contest_path = contest_type + "/" + contest_numb
os.mkdir(contest_path)

with open("base_code/aaa_basic_template.py", "r") as f:
    base_template = f.read()

for letter in ["A", "B", "C", "D", "E", "F", "test"]:
    with open(contest_path + f"/{letter}_v1.py", "w+") as f:
        f.write(base_template)
