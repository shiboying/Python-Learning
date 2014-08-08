class Queue(object):
    queue=[]
    def __init__(self):
        menu = {'a':self.enqueue, 'b':self.dequeue, 'c':self.putfile, 'd':self.getfile}
        print'============================'
        print'          QUEUE'
        print'a 入队'
        print'b 出队'
        print'c 写入文件'
        print'd 从文件读取'
        print'e 退出'
        print'============================'
        while True:
          choice = raw_input(('请选择:').strip())
          if choice not in 'abcd':
              if choice == 'e':
                  break
              else:
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



print'=============================='          
print'              QUEUE'
print'          学号：09212109       '
print'          班级：3'
print'          姓名：石博莹'
print'=============================='

def createqueue():
    queue = Queue()

createqueue()
