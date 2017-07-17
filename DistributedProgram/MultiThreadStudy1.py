import threading
import queue
import time
def washer(dishes,dish_queue):
    for dish in dishes:
        print('washing ',dish)
        time.sleep(5)
        dish_queue.put(dish)
def dryer(dish_queue):
    while True:
        time.sleep(1)
        #get 方法会阻塞线程，washer不PUT dish进来之前，get会一直阻塞
        dish=dish_queue.get()
        #所以下面这段其实不需要
        #if dish==None:
        #   print('no dish to dry right now')
        #  continue
        print(threading.currentThread)
        print('drying ',dish)
        dish_queue.task_done()
dish_queue=queue.Queue()
for n in range(2):
    dryerThread=threading.Thread(target=dryer,args=(dish_queue,))
    dryerThread.start()
dishes=['salad','bread','entree','desert']
washer(dishes,dish_queue)
dish_queue.join()
