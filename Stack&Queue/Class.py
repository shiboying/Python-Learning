




class Stack(object):
    stack = []
    def __init__ (self):
        menu = {'a':self.pushstack, 'b':self.isemptystack,'c':self.popstack, 'd':self.peekstack,'e':self.quits}
        print'======================'
        print'         STACK        '
        print'aѹ���ջ'
        print'b�ж϶�ջ�Ƿ�Ϊ��'
        print'c������ջ'
        print'd�鿴�����' 
        print'e�˳�'
        print'======================='
        while True:
            choice = raw_input(('��ѡ��:').strip())
            if choice not in 'abcde':
                    print'��������,���������'
            else :
                menu[choice]()
    
        
    def pushstack(self):
        self.stack.append(raw_input('�������ַ���һ��ֻ������һ���ַ�����').strip())
    def isemptystack(self):
        if len(self.stack)==0:
            print('ջ��')
        else:
            print('ջ����')
    def popstack(self):
        if len(self.stack)==0:
            print 'ջ�ѿ� �����ٵ���'
        else:
            print '������', self.stack.pop(), '��'

    def peekstack(self):
        if len(self.stack)==0:
            print 'ջ�գ����ܲ鿴'
        else:
            print '�Ԫ��Ϊ', self.stack[len(self.stack)-1]

    def quits(self):
        while True:
            if choice == 'e':
                break
print'=============================='          
print'��ѡ������Ҫ���еĲ���'
print'1. ջ����'
print'2. ���в���'
print'3. �˳�'
print'=============================='

def createstack():
    stack = Stack()
def createqueue():
    queue = Queue()
menu = {'1':createstack, '2':createqueue}
while True:
    while True:
          choice = raw_input(('��ѡ��:').strip())
          if choice not in '12':
                if choice == '3':
                    break 
                else:
                    print'���������������������'
          else :
                menu[choice]()




class Queue(object):
    queue=[]
    def __init__(self):
        menu = {'a':self.enqueue, 'b':self.dequeue, 'c':self.putfile, 'd':self.getfile,'e':self.quits}
        print'========================='
        print'a ���'
        print'b ����'
        print'c д���ļ�'
        print'd ���ļ���ȡ'
        print'e �˳�'
        print'========================='
        while True:
          choice = raw_input(('��ѡ��:').strip())
          if choice not in 'abcde':
                    print'���������������������'
          else :
                menu[choice]()
                
    def enqueue(self):
        self.queue.append(raw_input('�������ַ�(һ��ֻ������һ���ַ�):').strip())
    def dequeue(self):
        if len (self.queue)==0:
            print'�����ѿղ��ܳ���'
        else:
             print '���ӣ�', self.queue.pop(0), '��'
    def putfile(self):
        if len(self.queue)==0:
            print'������'
        else:
            filename = raw_input('�������ļ�����')
            file = open(filename,'w')
            for i in range(len(self.queue)):
                file.write(self.queue[i])
            print'�����'
    def getfile(self):
        filename = raw_input('����������Ҫ���ļ�����'
                             )
        if open(filename)==False:
            print'�޴��ļ�'
        else:
            files = open(filename,'r')
            self.queue = files.readline()
            print'����Ϊ��',self.queue

    def quits(self):
        while True:
            if choice == 'e':
                break


print'=============================='          
print'��ѡ������Ҫ���еĲ���'
print'1. ջ����'
print'2. ���в���'
print'3. �˳�'
print'=============================='

def createstack():
    stack = Stack()
def createqueue():
    queue = Queue()
menu = {'1':createstack, '2':createqueue}
while True:
    while True:
          choice = raw_input(('��ѡ��:').strip())
          if choice not in '12':
                if choice == '3':
                    break 
                else:
                    print'���������������������'
          else :
                menu[choice]()


    

