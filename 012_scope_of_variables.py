a = 10  # global variables, available in module scope
b = 20


def test_function_for_scope_demonstration():
    a = 30  # function scope, available only in function body (local variables)
    b = 40
    print("Local variables, available inner function:", a, b)


test_function_for_scope_demonstration()

print("Global variables, available outer function: ", a, b)

print("...........................................")


def override_local_variables():
    global a, b  # will a OVERRIDE the local var
    a = 30  # function scope, available only in function body (local variables)
    b = 40
    print("Global variables has been override to local:", a, b)


override_local_variables()
print("...........................................")


def hack_global_variables():
    for i in range(5):
        c = 50  # loops and conditional statements has only global variables (module scope)
        pass
        print(" For loop and if statements has only global var:", i)
        # print(c)


hack_global_variables()

print("...........................................")


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

