# Project Running Log & Integration Report - NetOps Automation Suite
SECR3253 Network Programming - Group Assignment
Maintained by M5 (Amr Hatem) - Integration and Documentation

## 1. Key Decisions
- Automation stack: Docker + Ansible with NETCONF.
- Network target: Cisco DevNet IOS XR Always-On sandbox (port 830).
  Chosen because it is free, always available, supports NETCONF, and needs no hardware.
- Version control: one shared GitHub repo. Each member commits to their own
  folder so participation shows in the history from day one.

## 2. Member Responsibilities
- M1 Alya Qistina (alyaqistiina) - Docker: Dockerfile, docker-compose, networking
- M2 Tang Jasmine (tjasmiine)    - Linux system info playbook (system_info.yml)
- M3 Adriana Zulaikha (zlaikhaa) - NETCONF: IP, user, banner, interface (configure_device.yml)
- M4 Ain Najiha (ainjhaa)        - NETCONF: static route + device info (retrieve_info)
- M5 Amr Hatem (amr432)          - Integration, README/docs, testing, bug log, reflections

## 3. Timeline
| Date  | Milestone                                              |
|-------|--------------------------------------------------------|
| 1 Jul | Repo setup, folder structure, DevNet access confirmed  |
| 2 Jul | First drafts of Docker env and all playbooks           |
| 3 Jul | Core playbook logic completed, individually tested     |
| 4 Jul | Full integration of components                         |
| 5 Jul | End-to-end testing, cleanup, documentation, reflections|
| 6 Jul | Submission (9 AM)                                      |

## 4. Prior Blockers (Member 3 - NETCONF)
- Sandbox IOS XR Always-On, port 830 reachable via nc test.
- SSH handshake failure (Python 3.8 / paramiko vs IOS XR SSH algorithms on labvm).
- Resolution: tested inside Docker container; configure_device.yml confirmed working.

## 5. Integration Test Log (M5) - 5 Jul
- Docker environment: built with `docker-compose up --build -d`. Both containers
  (ansible-control, linux-target) built and running, confirmed via `docker ps`.
- Linux system info (ansible/linux/system_info.yml):
  PASS. All 14 tasks ok, failed=0. Collected hostname, date/time, CPU, memory,
  disk usage, logged-in users, and top 5 processes. Full output saved in
  docs/sample_output_linux.txt.
- Network playbooks (configure_device.yml, retrieve_info.yaml):
  Ran retrieve_info.yaml from the ansible-control container against the DevNet
  sandbox. Result: connection to the sandbox was refused
  ("Connection reset by peer", sandbox IP 131.226.217.150 port 830).
  A plain SSH test to the same host returned the same reset, so the sandbox
  itself was unreachable at test time (public sandbox down/busy or credentials
  expired) - the playbook code is unaffected.
  Network configuration was previously confirmed working via M3's commit
  "Configure banner, interface description and IP via NETCONF - tested successfully".

## 6. Issues Found During Integration
- [OPEN] .env.example missing but README setup step 2 tells users to copy it.
  Owner: M1 (Tina) to add .env.example with placeholder sandbox variables.
- [OPEN] retrieve_info playbook saved as retrieve_info.yaml; all other playbooks
  use .yml. Owner: M4 (Ain) to confirm or rename for consistency.
- [OPEN] Reflection files: only reflection_member3.md present.
  Owner: M1, M2, M4, M5 each to add their own reflection.
- [OPEN] DevNet sandbox refused connections during testing; re-check sandbox
  status and refresh credentials before the final demo.
