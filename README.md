# aws-manage
Manage your AWS instances using python


Instructions:
- ensure you have following files in your home folder
  # ls -l ~/.aws/
  total 12
  -rw-r----- 1 root root  28 Mar 21 11:13 config
  -rw-r----- 1 root root 116 May  7 09:33 credentials

- ensure to have them updated with your AWS account details
  # cat ~/.aws/config
  [default]
  region=ap-south-1
  
  # cat ~/.aws/credentials
[default]
aws_access_key_id = <replace_with_your_id>
aws_secret_access_key = <replace_with_your_key>


