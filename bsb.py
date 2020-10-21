import sys
import bs
import platform
import os


def execute_file(file):
    with open(file, "r") as fh:
        exec(fh.read(), {})
    fh.close()


def execute(cmd):
    """
    Build .bs files using bsbuilder
    """
    i = 1
    args = []
    while i < len(sys.argv):
        args.append(cmd[i])
        i += 1
    tasks = []
    i = 0
    while i < len(args):
        task = args[i]
        if task == "build":
            tasks.append({"id": "build", "file": str(args[i+1])})
            i += 1
        elif task == "start":
            tasks.append({"id": "start"})
            i += 1
        else:
            print(f"Unknown task \"{task}\"")
        i += 1
    used_file = ""
    for task in tasks:
        _id = task["id"]
        if _id == "build":
            file = task["file"]
            bs.compile_file(file, file + "-compiled")
            used_file = file+"-compiled.py"
        elif _id == "start":
            print(platform.system())
            if platform.system() == "Windows":
                os.startfile(used_file)
            else:
                os.system(f"python3 {used_file}")
        else:
            print(f"Failed to execute task \"{_id}\"")
            break


execute(sys.argv)
