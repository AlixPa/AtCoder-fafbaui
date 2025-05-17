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

path_to_file = contest + "/" + contest_num + "/" + task.upper()
for vers in [f"_v{i}.py" for i in range(9, 0, -1)]:
    if os.path.exists(path_to_file + vers):
        os.rename(path_to_file + vers, path_to_file + ".py")
        break
