
# 演算子が来たら、スタックから2個とって、計算結果を、積む。


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


