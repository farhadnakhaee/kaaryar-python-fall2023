class ExceptionProxy(Exception):
    msg = "ok!"
    def __init__(self, func, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.function = func
        self.run_func()

    def run_func(self):
        try:
            self.function()
        except Exception as e:
            self.msg = str(e)


def transform_exceptions(func_ls):
    ans =[ExceptionProxy(func=func) for func in func_ls]
    return ans

if __name__ == "__main__":
    def f():
        1/0

    def g():
        pass

    tr_ls = transform_exceptions([f, g])

    for tr in tr_ls:
        print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)