def main_func(some_function):
    def wrap_func():
        print("This line is within main_func function.")
        some_function()
        print("This line is within mail_func function.")
    return wrap_func

@main_func
def main_func_child():
    print("This line is winthin mail_func_child function")
main_func_child()
