# Personal Reflection - Member 5 (Amr Hatem Gaber Zidan, A21EC0251)
Role: Integration, Documentation & Testing

## My Contribution
As Member 5 my job was integration, documentation, and testing. I did not write
the network or Docker code myself; my teammates did that. My job was to make sure
everything fits together and the repository is clean and clear.

I cleaned the repo (removed a stray .ted.swp file, expanded .gitignore), added my
details to the README and fixed the clone URL, created the README checklist
(README_TEMPLATE.md), and wrote the project running log and bug log in notes.md.
For testing, I ran the Linux system_info playbook (all tasks passed, output saved
in sample_output_linux.txt), built the Docker environment, and ran the network
playbook against the DevNet sandbox.

## Challenges
I struggled at the start with the Git workflow (clone, pull, commit, push, tokens)
until I understood why each step matters. The hardest part was a Docker build error
about clone3; I traced it to an old libseccomp2 library on the VM, upgraded it, and
the build then worked. When I ran the network playbook it reached the Cisco sandbox
but the sandbox refused the connection, so that test could not finish due to the
sandbox being down/expired, not the code.

## What I Learned
I learned that this work is as much about communication and being organized as it
is about code: clear commits, honest notes, and flagging issues to the right person.
I also learned to read errors carefully instead of giving up, and I saw the value of
the integration role in catching small mistakes early.
