class Queue(object):
    queue=[]
    def __init__(self):
        menu = {'a':self.enqueue, 'b':self.dequeue, 'c':self.putfile, 'd':self.getfile}
        print'============================'
        print'          QUEUE'
        print'a ���'
        print'b ����'
        print'c д���ļ�'
        print'd ���ļ���ȡ'
        print'e �˳�'
        print'============================'
        while True:
          choice = raw_input(('��ѡ��:').strip())
          if choice not in 'abcd':
              if choice == 'e':
                  break
              else:
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



print'=============================='          
print'              QUEUE'
print'          ѧ�ţ�09212109       '
print'          �༶��3'
print'          ������ʯ��Ө'
print'=============================='

def createqueue():
    queue = Queue()

createqueue()
