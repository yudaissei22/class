def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, b, c)
        print("move %s: %s --> %s" %(n,a,c))
        hanoi(n-1, b, a, c)

hanoi(4,"A","B","C")


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, d):
        self.stack = self.stack + [ d ]

    def pop(self):
        d = self.stack[-1]
        self.stack = self.stack[:-1]
        return d

    def get(self, idx):
        return self.stack[-1-idx]
    
    
while True:
    line = input('>').split()
    print(line)
    
    st = Stack()
    for i in line:
        if i == "+":
            a = st.pop()
            b = st.pop()
            st.push(a + b)
        elif i == "-":
            a = st.pop()
            b = st.pop()
            st.push(b - a)
        elif i == "/":
            a = st.pop()
            b = st.pop()
            st.push(b / a)
        elif i == "*":
            a = st.pop()
            b = st.pop()
            st.push(a * b)
        else:
            st.push(int(i))

    print(st.stack)

