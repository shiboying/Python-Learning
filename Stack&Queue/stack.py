
class Stack(object):
    stack = []
    def __init__ (self):
        menu = {'a':self.pushstack, 'b':self.isemptystack,'c':self.popstack, 'd':self.peekstack}
        print'==========================='
        print'         STACK        '
        print'aѹ���ջ'
        print'b�ж϶�ջ�Ƿ�Ϊ��'
        print'c������ջ'
        print'd�鿴�����' 
        print'e�˳�'
        print'============================'
        while True:
            choice = raw_input(('��ѡ��:').strip())
            if choice not in 'abcd':
                if choice == 'e':
                    break
                else:
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
print'              STACK'
print'          ѧ�ţ�09212109       '
print'          �༶��3'
print'          ������ʯ��Ө'
print'=============================='

def createstack():
    stack = Stack()

createstack()

