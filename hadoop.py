import os

p=20*'*'
print("\n\n\t\t{}Automation{}\n\n".format(p,p))
print("Welcome to my program...")

#configure hadoop namenode
def bigdata():
    inp= input("\nWhat do you want\n")
    if inp in "configure hadoop namenode" or inp in "master node":
        print("\nconfiguration of Master node\n")	       
        ing=input("enter machine IP")
        os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ing))	    
        os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ing))
        os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ing))
        os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ing))
        os.system("ssh {} jps".format(ing))
        os.system("mkdir {} /nam".format(ing))
        os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ing))
       	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ing))
        os.system("ssh {} hadoop namenode -format".format(ing))
        os.system("ssh {} hadoop-daemon.sh start namenode".format(ing))
        os.system("ssh {} jps".format(ing))
		
    elif inp in "configure hadoop datanode" or inp in "slave node":
		
       	print("\nconfiguration of Slave node\n")
       	ing=input("enter machine IP")
       	os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ing))
		
       	os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ing))
		
       	os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ing))
       	os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ing))
       	os.system("ssh {} jps".format(ing))
       	os.system("mkdir {} /data".format(ing))
       	os.system("scp /home/Ganesh/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ing))
       	os.system("scp /home/Ganesh/core-site.xml {}:/etc/hadoop/core-site.xml".format(ing))
	    
        os.system("ssh {} hadoop-daemon.sh start datanode".format(ing))        	
        os.system("ssh {} jps".format(ing))
                
    else:
            print("Please correct requirement")
if __name__=="__main__":
    bigdata() 
      
        
