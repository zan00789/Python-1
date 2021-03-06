# 定制一个计时器的类,让它能够统计一个函数运行若干次的时间
# 要求:函数调用次数可以设置(默认一百万次),实现珍上timing()方法用于启动计时器
import time as t


class MyTimer:
    def __init__(self):
        self.begin = self.end = 0
        self.prompt = 'Please call the start() method first'

    def start(self):
        if self.begin:
            print(self.prompt)
        else:
            self.begin = t.perf_counter()  # 记录开始时间
            print('Start timing')
        self.prompt = 'Please call the stop() method first'

    def stop(self):
        if not self.begin:
            print(self.prompt)
        else:
            self.end = t.perf_counter()  # 记录结束时间
            print('Timing ends')
            self._calc()
            self.prompt = 'Please call the start() method first'

    def _calc(self):  # 内部方法
        self.lasted = self.end - self.begin
        self.begin = self.end = 0

    def __repr__(self):
        if not self.begin or not self.end:
            return self.prompt
        else:
            return

    def __add__(self, other):
        return self.lasted + other.lasted


class MyFuncTimer(MyTimer):
    def __init__(self, func, cycles=1000000):
        super(MyFuncTimer, self).__init__()
        self.func = func
        self.cycles = cycles

    def timing(self):
        self.begin = t.process_time()
        for i in range(self.cycles):
            self.func()
        self.end = t.process_time()
        self._calc()
        return 'It runs for %.2fs' % self.lasted
