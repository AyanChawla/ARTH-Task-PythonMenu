# ARTH-Task-PythonMenu
A menu with Python is created to do  multiple tasks.


1. Hadoop

<b>REQUIRED - User must have files jdk-8u171-linux-x64.rpm, hadoop-1.2.1-1.x86_64.rpm, and files hdfs-site.xml and core-site.xml configured in the system</b>

User can import the module and import the function bigdata() Then enter the ip of the system where it want to configure Hadoop.

<i><b>from docker import bigdata</b></i>


2. Docker

<b>REQUIRED - User must have files /etc/yum.repos.d/doc.repo configured in the system</b>

User can import the module and import the function dock() Then enter the ip of the system where it want to configure Docker.

<i><b>from docker import dock</b></i>

3. Linux Commands

User can directly use the commands of linux and gives the ip of the system where it want to execute the commands then can tell its requirements there.

<i><b>
  from linux import linux
  
  <b>linux()
  
  <b>enter target machine IP ipaddr
  
  Enter your query make folder
</b></i>

4. Partitions and Storage in Hadooop

<a>https://www.linkedin.com/posts/aarnika-shringi-a671171b3_cloudcomputing-righteducation-rightmentor-activity-6730468729685082112-aTzY</a>

5. AWS <br>
<b>REQUIRED - User must have configured aws IAM account in the System to use AWS.py module</b>
Launching an Ec2 Instance

User has to use by importing the AWS.py file and

<i><b>
from AWS import AWS
obj = AWS()
obj.function()
</b></i>

Now,Multiple functions are included in it.
<ol>
<li>describe_AMIs(platform)</li> - Platfrom can be windows or linux
<li>set_AMI(AMI_id)</li> - Select the ami id by using describe_AMIs
<li>describe_regions()</li>
<li>set_region(region_name)</li>
<li>describe_instance_types()</li>
<li>set_instance_type(instance_type)</li>
<li>describe_key_pairs()</li>
<li>create_key_pair()</li>
<li>set_key_pair(keypair_name_without_extension)</li>
<li>describe_security_group()</li>
<li>create_security_group()</li>
<li>set_security_group(security_grp _name)</li>
<li>set_count(number)</li> - number of instances user want to launch
<li>launch_instance()</li>
<li>describe_instances()</li>
<li>terminate_instances(instance_id)</li>
<li>describe_ebs()</li>
<li>create_ebs()</li>
<li>describe_az()</li> - gives a list of availability zones
<li>set_az(avialabilty_zone)</li>
<li>attach_ebs(instnace_id,volume_id)</li>
</ol>



