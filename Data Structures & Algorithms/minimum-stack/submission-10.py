class MinStack:
    dat = []
    mini = []
    def __init__(self):
        self.dat = []
        self.mini = []

    def push(self, val: int) -> None:
        self.dat.append(val)
        if len(self.mini) == 0 or val <= self.mini[-1]:
            self.mini.append(val)

    def pop(self) -> None:
        tmp = self.dat.pop()
        if len(self.mini) == 0:
            return
        if self.mini[-1] == tmp:
            self.mini.pop()

    def top(self) -> int:
        return self.dat[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
