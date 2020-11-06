# ARTH-Task-PythonMenu
A menu with Python is created to do  multiple tasks.


1. Hadoop
Installation

2. Docker
Installation

3. Linux Commands

4. AWS 
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



