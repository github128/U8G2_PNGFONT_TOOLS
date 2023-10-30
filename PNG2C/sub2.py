import subprocess
import sys


cmd =  "tools\png2bdf.exe -o myfont.bdf -f myfont -e 65  tst\*.png"
args = cmd.split()
p = subprocess.Popen(args,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
out ,err = p.communicate()
print(str(out).replace("\\r\\n","\r\n"))


cmd2 = r"tools\bdfconv.exe -v -f 1 -m 64-511 myfont.bdf -o myfont.c -n myfont -d myfont.bdf"
arg2 = cmd2.split()
p2 = subprocess.Popen(arg2,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
out2,err2 = p2.communicate()
print(str(out2).replace("\\r\\n","\r\n"))

a =  open("myfont.c","r+")
d = a.read()
a.seek(0)
a.write("#include \"u8g2.h\"\n")
a.write(d)
a.close()
print(d)

print(sys.argv[1])

input("wait")
