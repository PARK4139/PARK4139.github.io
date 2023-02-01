# __________________________ ( encoding = utf-8 ) _______________________ 


# __________________________ ( read temp.txt) _______________________ 
f_path = r'C:\Users\ë°?????Desktop\alpha\categories\RPA\src\categories\.bat\01 ( high frequency using commands )/temp.txt'
new_content = ''
with open(f_path,'r',encoding='utf-8') as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        new_string = l.strip()
        new_content += 'cd "' + new_string + '"' + '\nmkdir #\ncd ..' 


# __________________________ ( writie temp.txt) _________________________ 
with open(f_path,'w') as f:
    f.write(new_content)


# __________________________ ( rename temp.txt to temp.py ) _________________________  
import os 
os.rename('temp.txt','temp.bat')


