
class Stack(object):
    stack = []
    def __init__ (self):
        menu = {'a':self.pushstack, 'b':self.isemptystack,'c':self.popstack, 'd':self.peekstack}
        print'==========================='
        print'         STACK        '
        print'a压入堆栈'
        print'b判断堆栈是否为空'
        print'c弹出堆栈'
        print'd查看最顶数据' 
        print'e退出'
        print'============================'
        while True:
            choice = raw_input(('请选择:').strip())
            if choice not in 'abcd':
                if choice == 'e':
                    break
                else:
                    print'输入有误,请从新输入'
            else :
                menu[choice]()
    
        
    def pushstack(self):
        self.stack.append(raw_input('请输入字符（一次只能输入一个字符）：').strip())
    def isemptystack(self):
        if len(self.stack)==0:
            print('栈空')
        else:
            print('栈不空')
    def popstack(self):
        if len(self.stack)==0:
            print '栈已空 不能再弹出'
        else:
            print '弹出（', self.stack.pop(), '）'

    def peekstack(self):
        if len(self.stack)==0:
            print '栈空，不能查看'
        else:
            print '最顶元素为', self.stack[len(self.stack)-1]

    def quits(self):
        while True:
            if choice == 'e':
                break


print'=============================='          
print'              STACK'
print'          学号：09212109       '
print'          班级：3'
print'          姓名：石博莹'
print'=============================='

def createstack():
    stack = Stack()

createstack()

