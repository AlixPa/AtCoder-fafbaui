import os
import shutil

type_dt = {"b": "beginner", "r": "regular", "g": "grand"}
contest_type_i = input("Type of contest (b/r/g): ")
contest_type = type_dt[contest_type_i]
contest_numb = input("Contest number: ")
contest_path = contest_type + "/" + contest_numb
os.mkdir(contest_path)

with open("base_code/aaa_basic_template.py", "r") as f:
  base_template = f.read()

for letter in ["A", "B", "C", "D", "E", "F", "test"]:
  with open(contest_path + f"/{letter}_v1.py", "w+") as f:
    f.write(base_template)