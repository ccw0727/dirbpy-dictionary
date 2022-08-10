import subprocess
import dirbpy
import wpscan_out_parse


###run in Kali
#wpscan


#dirb

result = subprocess.Popen("dirb http://testfire.net/ -o result.txt",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
print(result)