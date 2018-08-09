import asyncio
import time

@asyncio.coroutine
def sayHello():
    print('Hello World!')
    beforeTime = int(time.time())
    timeArray = time.localtime(beforeTime)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    r = yield from asyncio.sleep(2)
    print('Hello again!')
    nowTime = int(time.time())
    timeArray = time.localtime(nowTime)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    print(otherStyleTime)

loop = asyncio.get_event_loop()

loop.run_until_complete(sayHello())

loop.close()


