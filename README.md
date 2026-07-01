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
| Alya Qistina binti Awaluddin | | | Docker environment |
| Member 2 | | | Linux system info automation |
| Member 3 | | | Network config automation (IP, user, banner, interface) |
| Member 4 | | | Network config automation (static route, device info retrieval) |
| Member 5 | | | Integration, documentation, testing |

## Architecture

```
                     ┌─────────────────────────┐
                     │   Ansible Control Node    │
                     │   (Docker container)      │
                     └───────────┬───────────────┘
                                 │
                 ┌───────────────┴────────────────┐
                 │                                  │
      NETCONF over SSH                    Ansible over SSH
                 │                                  │
                 ▼                                  ▼
   ┌───────────────────────────┐      ┌─────────────────────────┐
   │  Cisco DevNet IOS-XE       │      │  Linux Target Container  │
   │  Always-On Sandbox         │      │  (Docker container)      │
   └───────────────────────────┘      └─────────────────────────┘
```

- The **Ansible control node** runs inside a Docker container with Ansible, `ncclient`, and the `ansible.netcommon` collection installed.
- **Network configuration tasks** are pushed to a Cisco DevNet Always-On IOS-XE sandbox via NETCONF.
- **Linux system info tasks** run against one or more Linux target containers over SSH.

## Repository Structure

```
netops-automation-suite/
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
- Access credentials for the Cisco DevNet IOS-XE Always-On Sandbox
  ([https://developer.cisco.com/site/sandbox/](https://developer.cisco.com/site/sandbox/))

## Setup & Usage

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd netops-automation-suite
   ```

2. **Configure sandbox credentials**
   Copy the example environment file and fill in your DevNet sandbox details:
   ```bash
   cp .env.example .env
   ```

3. **Build and start the containers**
   ```bash
   cd docker
   docker-compose up --build -d
   ```

4. **Run the network configuration playbook**
   ```bash
   docker exec -it ansible-control ansible-playbook ansible/network/configure_device.yml
   ```

5. **Retrieve device information**
   ```bash
   docker exec -it ansible-control ansible-playbook ansible/network/retrieve_info.yml
   ```

6. **Collect Linux system information**
   ```bash
   docker exec -it ansible-control ansible-playbook ansible/linux/system_info.yml
   ```

## Sample Output


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
- [ ] Personal Reflection Reports (2 pages per member, in `docs/reflections/`)
