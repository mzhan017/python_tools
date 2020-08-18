#!/usr/bin/python
#usage, python convert.py <file-name>, generate one new file with postfix <file-name>.out
#author, Mark Zhang(420075746@qq.com)
#Any question, it's ok to sent email
#Attention, if there is special char, that cannot be resolved, then error log print:
#Attention!!!!! please there is one line that with decode error


import sys
import json
import io 

file=sys.argv[1]
file_output=file+".out"

f_trace = io.open(file, 'r',errors="ignore")
f_message = open(file_output, 'w')


i=0
version = ""

for line in f_trace:
 try:
  if len(line)!=1: ###if the line is empty
    geek_dict = json.loads(line.replace(",,",","), strict=False)

    if i == 0:
      if line.find("build_version")>-1:
        version = "".join(geek_dict['extension']['build_version']+"\n\n")
        i=2
    if geek_dict['type'] == "alarm":   # if the log type is alarm
        f_message.write(geek_dict['time']+":"+geek_dict['host']+":"+geek_dict['process']+":"+geek_dict['level']+":"+geek_dict['systemid']+":"+geek_dict['version']+"\n") 

        line2="".join(geek_dict['alarm']['data'])
        f_message.write("Alarm: "+line2+"\n\n") 
    else:
        f_message.write(geek_dict['time']+":"+geek_dict['host']+":"+geek_dict['process']+":"+geek_dict['level']+":"+geek_dict['systemid']+":"+geek_dict['version']+":"+"Seq="+geek_dict['extension']['log_attempts']+":"+geek_dict['extension']['file_name']+":"+geek_dict['extension']['line']+"\n") 

        line2="".join(geek_dict['log']['message'])
        line2=line2.replace("^M^M","\n").replace("^M","\n")
        f_message.write(line2+"\n\n") 
 except:
  f_message.write("Attention!!!!! please there is one line that with decode error!!!\n\n")
f_message.write("version: "+version) 
