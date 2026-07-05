## Personal Reflection - Member 1 (Alya Qistina binti Awaluddin, A23CS0041)
Role: Docker environment — Dockerfile(s), docker-compose.yml, network setup between containers

## My Contribution to the Project
My personal contribution and responsibility in this project was to design a Docker-based environment which served as the basis for the entire automation solution. I set up the Ansible control node as a Docker container. I also wrote the Dockerfile to install Ansible, ncclient and paramiko that are needed for NETCONF communication. Additionally, I also wrote the docker-compose.yml file to define the services, which includes the control node and a Linux target container used for testing the system information playbook.

Other than that, I was also responsible for establishing network connectivity between the components. This includes:

1. Sharing Docker bridge network so the control node could reach both Linux target container
2. Verified connectivity using tools such as ping and nc to confirm that the NETCONF port (830)
3. Tested SSH access between containers to ensure the automation could be executed


## Challenges Encountered
My first personal challenge was a technical one. When I first started and created the folders and files needed, I couldn’t push my process in the GitHub. My attempts to push commits to GitHub were met with failure because my password was not accepted during the authentication process. After doing some research, I found out that I needed to use personal tokens to authenticate, instead of using my password. Later, I learned how to generate and use a Personal Access Token. Additionally, I also made sure to share this fix with the rest of my teammates so nobody else lost time on the same issue. 

Another major challenge that I encountered was learning to coordinate five people working on interdependent parts of the same system. For example, my networking setup depended on knowing which Linux image my teammate was responsible for. By using the docs/notes.md and always pushing commits helped overcome this challenge.


## What I Learned From the Project
This project gave me hands-on experience with automation. I learned how Docker networking works between multiple containers and an external host and how to test connectivity on specific ports. I also learned and gained much understanding of how Ansible interacts with network devices through NETCONF. I also understood why environmental consistency can break automation.

Other than technical skills, I also learned how to navigate in a collaborative environment. I learned that it is not easy to work with Git across five other people. I understood the importance of pulling before pushing and committing in small increments. I also learned that infrastructure work like mine often becomes a dependency for the rest of the team later in a project. 

Overall, this project has strengthened both my technical skills in network automation and my collaborative skills.
