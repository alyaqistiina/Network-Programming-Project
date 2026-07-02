FROM python:3.11-slim

# Install system dependencies needed for Ansible + SSH + NETCONF
RUN apt-get update && apt-get install -y \
    openssh-client \
    sshpass \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages: Ansible, NETCONF client, SSH library
RUN pip install --no-cache-dir \
    ansible \
    ncclient \
    paramiko

# Install Ansible collections needed for NETCONF and Linux automation
RUN ansible-galaxy collection install ansible.netcommon ansible.utils

# Set working directory inside the container
WORKDIR /ansible

# Keep the container running so you can exec into it and run playbooks manually
CMD ["sleep", "infinity"]
