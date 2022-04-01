def simple_decore(fn):
    def wrapper():
        print("Start function")

    fn()
    print("Stop function")
    return wrapper


@simple_decore
def first_test():
    print("Test function 1")
