




class Stack(object):
    stack = []
    def __init__ (self):
        menu = {'a':self.pushstack, 'b':self.isemptystack,'c':self.popstack, 'd':self.peekstack,'e':self.quits}
        print'======================'
        print'         STACK        '
        print'a压入堆栈'
        print'b判断堆栈是否为空'
        print'c弹出堆栈'
        print'd查看最顶数据' 
        print'e退出'
        print'======================='
        while True:
            choice = raw_input(('请选择:').strip())
            if choice not in 'abcde':
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
print'请选择您需要进行的操作'
print'1. 栈操作'
print'2. 队列操作'
print'3. 退出'
print'=============================='

def createstack():
    stack = Stack()
def createqueue():
    queue = Queue()
menu = {'1':createstack, '2':createqueue}
while True:
    while True:
          choice = raw_input(('请选择:').strip())
          if choice not in '12':
                if choice == '3':
                    break 
                else:
                    print'您输入的有误请重新输入'
          else :
                menu[choice]()




class Queue(object):
    queue=[]
    def __init__(self):
        menu = {'a':self.enqueue, 'b':self.dequeue, 'c':self.putfile, 'd':self.getfile,'e':self.quits}
        print'========================='
        print'a 入队'
        print'b 出队'
        print'c 写入文件'
        print'd 从文件读取'
        print'e 退出'
        print'========================='
        while True:
          choice = raw_input(('请选择:').strip())
          if choice not in 'abcde':
                    print'您输入的有误，请重新输入'
          else :
                menu[choice]()
                
    def enqueue(self):
        self.queue.append(raw_input('请输入字符(一次只能输入一个字符):').strip())
    def dequeue(self):
        if len (self.queue)==0:
            print'队列已空不能出队'
        else:
             print '出队（', self.queue.pop(0), '）'
    def putfile(self):
        if len(self.queue)==0:
            print'无内容'
        else:
            filename = raw_input('请输入文件名：')
            file = open(filename,'w')
            for i in range(len(self.queue)):
                file.write(self.queue[i])
            print'已完成'
    def getfile(self):
        filename = raw_input('请输入您需要的文件名：'
                             )
        if open(filename)==False:
            print'无此文件'
        else:
            files = open(filename,'r')
            self.queue = files.readline()
            print'内容为：',self.queue

    def quits(self):
        while True:
            if choice == 'e':
                break


print'=============================='          
print'请选择您需要进行的操作'
print'1. 栈操作'
print'2. 队列操作'
print'3. 退出'
print'=============================='

def createstack():
    stack = Stack()
def createqueue():
    queue = Queue()
menu = {'1':createstack, '2':createqueue}
while True:
    while True:
          choice = raw_input(('请选择:').strip())
          if choice not in '12':
                if choice == '3':
                    break 
                else:
                    print'您输入的有误请重新输入'
          else :
                menu[choice]()


    

