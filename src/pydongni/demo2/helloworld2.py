from ..demo.helloworld import hello_world as h2

def hello_world():
    print("hello world from module demo2")

def hello_world3():
    print("import from demo-helloworld")
    h2()
    print("complete import from demo-helloworld")

