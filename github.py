import os

try:
    msg = input("Enter a commit sessage: ")

    os.chdir("/home/student/mycode")
    cmds = ["git add .",
            "x",
            "git push"]
    cmds[1] = "git commit -m " + msg

    for x in cmds:
        os.system(x)

except Exception as err:
    print("Something went wrong: ", err)
