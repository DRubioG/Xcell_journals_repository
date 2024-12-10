import requests
import numpy as np
import threading

base_url = 'https://www.xilinx.com/publications/archives/xcell/Xcell'
# base_url = 'https://www.xilinx.com/publications/archives/xcell-software/xcell-software'

def download(i):
    response = requests.get(base_url+str(i)+".pdf")
    file_Path = 'Xcell_software'+str(i)+'.pdf'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully #' + str(i))
    else:
        print('Failed to download file #' + str(i))

threads = list()
numbers = np.arange(1,94)
for i in numbers:
    x = threading.Thread(target=download, args=(i,))
    threads.append(x)
    x.start()
