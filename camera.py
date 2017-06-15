import picamera
from timeit import default_timer as timer

def picture_save(number, file_name):
    camera = picamera.PiCamera()
    path = 'picture/'
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
