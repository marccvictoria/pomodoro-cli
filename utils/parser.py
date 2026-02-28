# receive an input from the user
# read each line separated by spaces as delimeter


def session_inf():
    pass

def save_conf(work, brk):
    pass

class Task:
    def add():
        pass
    def remove():
        pass
    def list():
        pass


commands = {
    "pomo": {
        "-session": {
            "-infinite": session_inf,
        },
        "-save-config": save_conf,
        "-change-setting": "",
        "-change-default": "",
        "task": {
            "add": Task.add,
            "remove": Task.remove,
            "list": Task.list
        }
    }

}

def parse(usr_inp):
    usr_inp_parsed = usr_inp.split()
