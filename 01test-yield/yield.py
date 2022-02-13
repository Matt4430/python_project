

def yeld_id(a=5):
    for i in range(a):
        print("yeld start...")
        yield i


def start(b):
    for i in b:
        print('第 ', i ,' 个')



if __name__ == '__main__':

    start(yeld_id(100))
