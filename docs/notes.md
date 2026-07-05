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
- Linux system info (ansible/linux/system_info.yml):
  PASS. Ran with `ansible-playbook -i localhost, -c local`.
  All 14 tasks ok, failed=0. Collected hostname, date/time, CPU, memory,
  disk, logged-in users, top 5 processes. Full output saved in
  docs/sample_output_linux.txt.
- Network playbooks (configure_device.yml, retrieve_info.yaml):
  NOT re-run locally. Building the Docker control node failed on this VM with
  an OCI seccomp error on syscall clone3 (VM's Docker version does not support
  clone3). Tried seccomp=unconfined flag, older bullseye base image, and direct
  docker build - all blocked by the same daemon-level issue. Would need a Docker
  upgrade on the VM to resolve.
  Verified instead via commit history: M3 commit "Configure banner, interface
  description and IP via NETCONF - tested successfully" confirms these ran
  against the sandbox on the author's environment.

## 6. Issues Found During Integration
- [OPEN] .env.example missing but README setup step 2 tells users to copy it.
  Owner: M1 (Tina) to add .env.example with placeholder sandbox variables.
- [OPEN] retrieve_info playbook saved as retrieve_info.yaml; all other playbooks
  use .yml. Owner: M4 (Ain) to confirm or rename for consistency.
- [OPEN] Reflection files: only reflection_member3.md present.
  Owner: M1, M2, M4, M5 each to add their own reflection.
- [ENV] Docker build blocked by clone3/seccomp on this VM's Docker version.
  Not a code bug; network playbooks verified via M3's tested commit instead.
