import picamera
from timeit import default_timer as timer

path = 'picture/'

def picture_save(number, file_name):
    camera = picamera.PiCamera()
    start = timer()
    '''
    for i in range(1):
        camera.capture( path + str(i) + '.jpg')
        print (i)
    '''

    camera.capture( path + str(file_name) )
    
    end = timer()
    print (end - start) 
    camera.close()

if __name__=="__main__":
    import time
    for i in range(10):
        print(i)
        time.sleep(1)
        picture_save(1, "chou"+str(i)+".jpg")
