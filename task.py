import os
import sys

dt_contest = {"b": "beginner", "r": "regular", "g": "grand"}
url = sys.argv[1]

grouped = url.split("/")[-1]
if grouped[0:3] not in {"abc", "arc", "agc"}:
    contest = "other"
    contest_num = grouped[:-1]
    task = (grouped[-1]).upper()
else:
    contest = dt_contest[grouped[1]]
    contest_num = grouped[3:6]
    task = (grouped[-1]).upper()

path_to_file = contest + "/" + contest_num

if not os.path.exists(path_to_file):
    os.mkdir(contest + "/" + contest_num)
    f = open(path_to_file + "/test.py", "w+")
    f.close()

base_code = ""
with open("base_code/aaa_basic_template.py", "r") as f:
    base_code = f.read()

for term in ["_v1", "_v2", "_v3", "_v4", "_v5", "_v6", "_v7", "_v8", "_v9"]:
    file_name = path_to_file + "/" + task + term + ".py"
    if not os.path.exists(file_name):
        with open(file_name, "w+") as f:
            f.write(base_code)
            break
