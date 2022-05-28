import ctypes

class Config(object):
    myappid = 'Presto Change-O'



def init_app_id():
    # Tell Windows that this is its own application and not just pythonw.exe
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(Config.myappid)