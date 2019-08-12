import os
# import shutil
import win_unicode_console
win_unicode_console.enable()

wantFileType = ['mp4', 'rmvb', 'avi', 'mkv', 'txt']


class findFileClass:
    def __init__(self, directer=""):
        self.dir = directer
        self.dirQueue = [self.dir]
        self.deal_process()

    # 1. cp file to self.dir
    # 2. make path to self.dirQueue
    def dealCurrentDir(self, currentDir):
        if not os.path.exists(currentDir):
            # print(currentDir, " is not exists.")
            return False
        contents = os.listdir(currentDir)
        # print(type(contents))  // list

        for content in contents:
            temppath = currentDir + "/" + content
            if os.path.isdir(temppath):
                self.enQueue(temppath)
            else:
                # print(content, " is a file.")
                if temppath[-3:] in wantFileType:
                    self.dealWantFile(currentDir, content)

    def dealWantFile(self, dirWant, fileWant):
        print(fileWant)
        # if not dirWant == self.dir:
        #     shutil.copyfile(dirWant + '/' + fileWant,
        #                     self.dir + "/" + fileWant)

    def enQueue(self, dir):
        self.dirQueue.append(dir)

    def popQueue(self):
        if not self.dirQueue:
            return None
        return self.dirQueue.pop()

    def deal_process(self):
        while True:
            # print("self.queue length is :", len(self.dirQueue))
            currentdir = self.popQueue()
            if not currentdir:
                print("Deal all content over.")
                return
            else:
                # print(currentdir)
                self.dealCurrentDir(currentdir)


if __name__ == "__main__":
    # print("hello")
    # findFileClass("E:/gg")

