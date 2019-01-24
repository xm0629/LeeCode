# python3.6 实现顺序表

class SeqList(object):
    def __init__(self,size=50):
        self.max = size
        self.num = 0
        self.data = [None]*self.max

    def is_empty(self):
        return self.num is 0

    def is_full(self):
        return self.num is self.max
    
    def __getitem__(self, index):
        if not isinstance(index,int):
            raise TypeError
        if 0 <= index < self.max:
            return self.data[index]
        else:
            raise IndexError

    def __setitem__(self,index,value):
        if not isinstance(index,int):
            raise TypeError
        if 0 <= index < self.max:
            self.data[index] = value
        else:
            IndexError

    def local_item(self,value):
        for i in range(self.num):
            if self.data[i] == value:
                return i
        return -1
    
    
    def cout(self):
        return self.num


    def append_last(self,value):
        if self.num > self.max:
            print('list is full')
        else:
            self.data[self.num] = value
            self.num += 1
    def insert(self,index,value):
        if self.num > self.max:
            print('list is full')
        if not isinstance(index,int):
            raise TypeError
        if index<0 or index>self.num:
            raise IndexError
        for i in range(self.num,index,-1):
            self.data[i]=self.data[i-1]
        self.data[index]=value
        self.num += 1


    def remove(self,index):
        if isinstance(index,int):
            raise TypeError
        if index < 0 or index >= self.num:
            raise IndexError
        for i in range(index,self.num):
            self.data[i]=self.data[i+1]
        self.num -= 1

    def print_list(self):
        for i in range(0,self.num):
            print(self.data[i])

    def destroy(self):
        self.__init__()


if __name__ == "__main__":
    seqList = SeqList()
    print(seqList.is_empty())
    print(seqList.append_last(18))
    print(seqList.__getitem__(0))
