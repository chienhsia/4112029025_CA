#建立名為CS的目錄
import os
os.mkdir('CS')
file_HW = os.path.join('CS', "homework.txt")
#在txt檔寫入內容(內容為：自己的學號_名字)
with open(file_HW,'w') as file:
    file.write('4112029025_黃千夏\n')
#讀資料內容跟檔案資訊
file=open('CS\homework.txt','r')
file_content=file.read()
print(f'檔案內容:{file_content}')
import time
file_size=os.path.getsize('CS\homework.txt')
print(f'文件大小:{file_size}字節')
modification_time = os.path.getmtime('CS\homework.txt')
print(f'最後修改時間:{modification_time}')
formatted_time = time.ctime(modification_time)   
print(f'最後修改時間(人類可讀格式):{formatted_time}')
file.close()
#刪除檔案與目錄
if os.path.exists('CS\homework.txt'):
    os.remove('CS\homework.txt')
os.rmdir('CS')
print('目錄與檔案已刪除')
