import os

p=20*'*'
print("\n\n\t\t{}Automation{}\n\n".format(p,p))

#linux commands
def linux():
    ip=input("enter target machine IP")
    com= input("\nEnter your query\n")

    if  "pwd" in com or " path" in com	or "directory" in com :
        os.system("ssh {} pwd".format(ip))

    elif "cal" in com	or "calendar" in com:
        os.system("ssh {} cal".format(ip))

    elif "date" in com	:
        os.system("ssh {} date".format(ip))

    elif " who am i" in com	or "whoami " in com :
        os.system("ssh {} whoami".format(ip))

    elif "make folder" in com	or " make a folder" in com or "create folder" in com or " make folder" in com:
        fname= input("\nFolder name : ")
        os.system("ssh {} mkdir /{} ".format(ip,fname))

    elif "delete folder" in com	or " delete a folder" in com or " delete" in com or " remove" in com:
        fname= input("\nFolder name : ")
        os.system("ssh {} rm /{} ".format(ip,fname))


    elif "empty file" in com	or "touch" in com:
        fname=input("\nFile name : ")
        os.system("ssh {} touch {}".format(ip,fname))

    elif "copy" in com	or "cp" in com:
        source=input("\nEnter the source address : ")
        dest= input("\nEnter the destination address : ")
        os.system("ssh {} cp {} {}".format(ip,source,dest))

    elif "move" in com	or "cut" in com or "mv" in com:
        source=input("\nEnter the source address : ")
        dest= input("\nEnter the destination address : ")
        os.system("ssh {} mv {} {} ".format(ip,source,dest))

    elif "remove folder" in com	or "delete folder" in com:
        fname=input("\n Enter the folder name : ")  
        os.system("ssh {} ".format(ip))

    elif "install" in com	or "yum install" in com:
        pckg=input("\nPackage name : ")
        os.system("ssh {} yum install {} ".format(ip,pckg))

    elif "update" in com	or "yum update " in com:
        pckg=input("\nPackage name : ")
        os.system("ssh {} yum update {} ".format(ip,pckg))

    elif com == ""	:
        print("query cannot be empty")

                
    else:
            print("not available")


      
        
