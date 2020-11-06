import subprocess as sb 

class AWS_EC2():
	
	def __init__(self):
		self.cmd = ""
		self.region = ""

	

	def describe_AMIs(self,platform):
		print(sb.getoutput("aws ec2 describe-images --filters \"Name=platform, Values=windows\" --image-ids"))

	def set_AMI(self,image_id):
		self.image_id = image_id
	
	
	

	def describe_regions(self):
		print(sb.getoutput("aws ec2 describe-regions"))
		print("----------------------\n\n\n")
		print("Select the RegionName, store it in a string variable and use set_region to set the region")

	def set_region(self,region):
		self.region = region
		#print(self.region)


	def describe_instance_types(self):
		print(sb.getoutput("aws ec2 describe-instance-type-offerings --region {}".format(self.region)))
		print("----------------------\n\n\n")
		print("Select the InstanceType, store it in a string variable and use set_instance_type to set the type")

	def set_instance_type(self,instance_type):
		self.instance_type = instance_type


	def describe_key_pairs(self):
		print(sb.getoutput("aws ec2 describe-key-pairs"))


	def create_key_pair(self):
		x = sb.getoutput("aws ec2 create-key-pair --key-name keypair")
		file = open("keypair.pem","w")
		file.write(x)
		file.close()

	def set_key_pair(self,keypair):
		self.keypair = keypair

	def describe_security_group(self):
		print(sb.getoutput("aws ec2 describe-security-groups"))


	def create_security_group(self):
		sb.getoutput("aws ec2 create-security-group --group-name security_grp_name --description \"SeurituGroup\"")

	def set_security_group(self,security_grp_name):
		self.security_grp_name = security_grp_name

	def set_count(self,number):
		self.count = number

	def launch_instance(self):
		self.cmd = "aws ec2 run-instances --image-id "+self.image_id+" --count "+str(self.count)+" --instance-type "+self.instance_type+" --key-name "+self.keypair+" --security-groups "+self.security_grp_name
		print(self.cmd)
		print(sb.getoutput(self.cmd))

	def describe_instances(self):
		print(sb.getoutput("aws ec2 describe-instances"))

	def terminate_instances(self,instance_id):
		sb.getoutput("aws ec2 terminate-instances --instance-ids "+instance_id)

	def describe_ebs(self):
		print(sb.getoutput("aws ec2 describe-volumes"))

	def create_ebs(self):
		volume_type = input("Please Choose (gp2,standard,io2,io1,sc1,st1)")
		size = input("Please Choose size (Constraints:  1-16,384  for  gp2  ,  4-16,384  for  io1  and  io2  ,\
          500-16,384 for st1 , 500-16,384 for sc1 , and 1-1,024 for standard .\
          If  you  specify  a  snapshot,  the  volume size must be equal to or\
          larger than the snapshot size.)") 
		sb.getoutput("aws ec2 create-volume --volume-type "+volume_type+" --size "+size+" --availability-zone "+self.az)



	def describe_az(self):
		print(self.region)
		if self.region=="":
			return "No region name given"
		print(sb.getoutput("aws ec2 describe-availability-zones --filters \"Name=region-name\",\"Values="+self.region+"\""))
		print("CAUTION- Intance and ebs volume must be in same region")
		print("\n\n\nSelect ZoneID and give argument to set_az")

	def set_az(self,az):
		self.az = az

	def attach_ebs(self,instance_id,volume_id):
		sb.getoutput("aws ec2 attach-volume --volume-id "+volume_id+" --instance-id "+instance_id+"  --device /dev/sdc")

def main():
	#print(sb.getoutput("date"))
	#e = AWS_EC2()
	#e.describe_regions()
	#e.set_region("us-east-2")
	#e.describe_AMIs()
	#e.set_AMI("ami-03657b56516ab7912")
	#e.describe_instance_types()
	#e.set_instance_type("t2.micro")
	#e.create_key_pair()
	#e.describe_key_pairs()
	#e.set_key_pair("keypair")
	#e.create_security_group()
	#e.describe_security_group()
	#e.set_security_group("security_grp_name")
	#e.set_count(1)
	#e.launch_instance()
	#e.terminate_instances("i-07d7692932d90d8b0")
	#e.describe_az()
	#e.set_az("use2-az3")
	#e.create_ebs()
	#e.describe_ebs()
	#e.attach_ebs("i-07d7692932d90d8b0","i-07d7692932d90d8b0")





if __name__ == '__main__':
	main()
		