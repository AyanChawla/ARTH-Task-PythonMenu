
import os

p=20*'*'
print("\n\n\t\t{}Automation{}\n\n".format(p,p))
print("Welcome to my program...")

def dock():
    
    inp= input("\nWhat do you want\n")
    ip=input("Enter ip address")
    if inp in "install docker" or inp in "docker":
        print("step 1 configuration of yum for docker")
        os.system("scp /etc/yum.repos.d/doc.repo {}:/etc/yum.repos.d/".format(ip))
        print("step 2 installation of docker")
        os.system("ssh {} yum install docker-ce --nobest".format(ip))
        print("step 3 starting service of docker")
        os.system("ssh {} systemctl start docker".format(ip))
      #  os.system("ssh {} systemctl status docker".format(ip))


if __name__=="__main__":
    dock()
