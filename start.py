import os
import threading

def electron():
    os.system('npm run electron:serve')

def local_backend():
    os.system('python electron_chat/backend/server.py')
    
thread1 = threading.Thread(target=electron)
thread2 = threading.Thread(target=local_backend)

thread1.start()
thread2.start()