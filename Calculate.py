from  stack import Stack

def get_expression(get_str):
    pro = dict(zip('#+-*/', '01122'))
    out = Stack()
    s = Stack()
    for x in get_str:
        if x == '(':
            s.push(x)
        elif x == ')':
            t = s.pop()
            while t != '(':
                out.push(t)
                t = s.pop()
        elif x in '+-*/':
            while 1==1:
                t = s.pop()
                if t == '(':
                    s.push(t)
                    break
                if pro[x] <= pro[t]:
                    out.push(t)
                else:
                    s.push(t)
                    break
            s.push(x)
        else:
            out.push(x)

    while len(s) != 0:
        out.push(s.pop())

    return out[:-1]


bds2 = '(a+b)*c-(d+e)/f'

print(get_expression(bds2))




# def computer_expression:



# if __name__ == "__main__":
