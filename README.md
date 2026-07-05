# NetOps Automation Suite

**SECR3253 Network Programming — Group Assignment (5%)**
Semester 2025/2026-2

## Objective

This project is an automation solution that uses **Docker** and **Ansible (with NETCONF)** to:
1. Configure a network device — IP address, user account, banner message, interface description, and a static route — and retrieve device information.
2. Automatically collect and display Linux system information — hostname, current date/time, CPU info, memory usage, disk usage, logged-in users, and the top 5 running processes by CPU usage.

## Team Members

| Name | Student ID | GitHub Username | Role |
|---|---|---|---|
| Alya Qistina binti Awaluddin | A23CS0041 | alyaqistiina | Docker environment |
| Tang Jasmine | A23CS0277 | tjasmiine | Linux system info automation |
| Adriana Zulaikha binti Zulkarman | A23CS0035 | zlaikhaa | Network config automation (IP, user, banner, interface) |
| Ain Najiha Binti Junaidi | A23CS0038 | ainjhaa | Network config automation (static route, device info retrieval) |
| AMR HATEM GABER ZIDAN |A21EC0251 |amr432 | Integration, documentation, testing |

## Architecture

```
                     ┌───────────────────────────┐
                     │   Ansible Control Node    │
                     │   (Docker container)      │
                     └───────────┬───────────────┘
                                 │
                 ┌───────────────┴──────────────────┐
                 │                                  │
	  NETCONF over SSH                    Ansible over SSH
                 │                                  │
                 ▼                                  ▼
   ┌───────────────────────────┐      ┌─────────────────────────┐
   │  Cisco DevNet IOS-XR      │      │  Linux Target Container │
   │  Always-On Sandbox        │      │  (Docker container)     │
   └───────────────────────────┘      └─────────────────────────┘
```

- The **Ansible control node** runs inside a Docker container with Ansible, `ncclient`, and the `ansible.netcommon` collection installed.
- **Network configuration tasks** are pushed to a Cisco DevNet Always-On IOS-XR sandbox via NETCONF.
- **Linux system info tasks** run against one or more Linux target containers over SSH.

## Repository Structure

```
Network-Programming-Project/
├── README.md
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── ansible/
│   ├── linux/
│   │   └── system_info.yml
│   └── network/
│       ├── inventory.yml
│       ├── configure_device.yml
│       └── retrieve_info.yml
├── docs/
│   ├── notes.md
│   └── reflections/
│       ├── reflection_member1.md
│       ├── reflection_member2.md
│       ├── reflection_member3.md
│       ├── reflection_member4.md
│       └── reflection_member5.md
└── .gitignore
```

## Prerequisites

- Docker & Docker Compose installed
- Git
- Access credentials for the Cisco DevNet IOS-XR Always-On Sandbox
  ([https://developer.cisco.com/site/sandbox/](https://developer.cisco.com/site/sandbox/))

## Setup & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/alyaqistiina/Network-Programming-Project.git
   cd Network-Programming-Project
   ```

2. **Configure sandbox credentials**
   Update `ansible/network/inventory.yml` with your DevNet sandbox host, port, username, and password.

3. **Build and start the containers**
   ```bash
   cd docker
   docker-compose up --build -d
   ```

4. **Run the network configuration playbook**
   ```bash
   docker exec -it ansible-control ansible-playbook -i /ansible/network/inventory.yml /ansible/network/configure_device.yml
   ```

5. **Retrieve device information**
   ```bash
   docker exec -it ansible-control ansible-playbook -i /ansible/network/inventory.yml /ansible/network/retrieve_info.yml
   ```

6. **Collect Linux system information**
   ```bash
   docker exec -it ansible-control ansible-playbook -i /ansible/linux/inventory.yml /ansible/linux/system_info.yml
   ```

## Sample Output

```
$ docker exec -it ansible-control ansible-playbook -i /ansible/linux/inventory.yml /ansible/linux/system_info.yml
...
TASK [Display hostname] ***********************************************
ok: [linux-target] => {
    "msg": "afac01e8ec3e"
}

TASK [Display memory usage] *******************************************
ok: [linux-target] => {
    "msg": [
        "               total        used        free      shared  buff/cache   available",
        "Mem:           3.8Gi       689Mi       1.8Gi       9.0Mi       1.4Gi       2.9Gi"
    ]
}
...
PLAY RECAP **************************************************************
linux-target               : ok=16   changed=0    unreachable=0    failed=0
```

## Development Timeline

| Date | Milestone |
|---|---|
| 1 Jul | Repo setup, DevNet sandbox access confirmed |
| 2 Jul | First draft of Docker environment and all playbooks |
| 3 Jul | Core playbook logic completed and individually tested |
| 4 Jul | Full integration of all components |
| 5 Jul | End-to-end testing, polish, documentation, reflections |
| 6 Jul | Submission (9 AM) |

## Deliverables

- [x] GitHub Repository
- [x] Personal Reflection Reports (2 pages per member, in `docs/reflections/`)
