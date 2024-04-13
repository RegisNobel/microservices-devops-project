#!/bin/bash

INSTANCE_IP=$(terraform output -raw instance_ip)

cat > inventory.ini <<EOF
[webserver]
$INSTANCE_IP ansible_user=ec2-user ansible_ssh_private_key_file=keys/ec2-user.pem
EOF
