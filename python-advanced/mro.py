
class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):
    pass


c = C()
print(c.greet())  # Output: Hello from A
print(C.__mro__)
print(C.mro())

# Daimond problem

class D:
    def greet(self):
        return "Hello from D"

class E(D):
    pass

class F(D):
    def greet(self):
        return "Hello from F"

class G(E, F):
    pass

g = G()
print(g.greet())  # Output: Hello from F
print(G.__mro__)
print(G.mro())