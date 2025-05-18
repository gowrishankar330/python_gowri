# variable scope = where a variable is visible & acccessible
#scope resolution = (LEGB) local->enclosed->global->built.in

#local
#def func1():
#   x=2
#    print(x)
#def func2():
#    x=3
#    print(x)
#func1()
#func2()

#enclosed
#def func1():
#    x=2
#    def func2():
#        print(x)
#    func2()
#func1()

#global
#def func1():
#    print(x)
#def func2():
#    print(x)
#x = 5

#func1()
#func2()


#built-in

from modules import pi

def func1():
    print(pi)
#pi = 3.234
func1()