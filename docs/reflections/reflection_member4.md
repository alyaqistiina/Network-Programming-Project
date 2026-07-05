## Personal Reflection - Member 4 (Ain Najiha Binti Junaidi, A23CS0038)
Role: Network Config Automation (Static route and device info retrieval)

## My Contribution
In this project, I was assigned to configure network automation for static route and device information retrieval. This task operates collaboratively alongside with my other member Zulaikha as she was responsible for the main component of the network automation suite. I worked closely with Member 3 to seamlessly inject my configuration blocks right before the core configuration commit sequence, ensuring the entire automation suite ran linearly without breaking the target state.

I designed and implemented the Ansible playbook for state and information retrieval located at ansible/network/retrieve_info.yml. Utilizing the ansible.netcommon.netconf_get module, I built precise XML filtering structures targeting the Cisco-IOS-XR-ifmgr-cfg YANG model to pull active operational states from the sandbox device. I paired this with custom Ansible debug loops to display structured data in an easily readable format for the team.

Other than that, I integrated the IPv4 static route configurations within the shared ansible/network/configure_device.yml playbook using the Cisco-IOS-XR-ip-static-cfg data model to mapping prefixes, subnet masks, and next-hop gateways safely to the default VRF.

## Challenges
Few challenges I faced during this project was file contention and branch management because Zulaikha and I were concurrently modifying the exact same playbook file (configure_device.yml), the risk of Git merge conflicts was high. Hence, I established a branch workflow before making local edits on the precise placement of code blocks and pulling the absolute latest master branch changes to resolve this issue. I also need to ensure the other member finish their part before pushing a new edit to avoid conflict.
Moreover, this configuration tasks relied heavily on the inventory credentials and target platform variables set up by other members where debugging required explicit coordination to ensure sandbox credentials were functional and securely handled through localized environment variables (.env). Lastly, transitioning between sandbox environments meant dealing with complex vendor namespaces. Mapping out the exact schema structures for Cisco-IOS-XR-ip-static-cfg required rigorous documentation verification to ensure the XML payloads matched the rigid structures mandated by the Cisco IOS-XR Always-On sandbox.

## My Lessons Learned
I learned that this project required an active communication with the members and organized distribution tasks to ensure an active participation between group members. A clear committed history is also helpful to ensure the task progress is clear throughout the project especially in implementing through GitHub. Other than that, I learned that Git is just as vital to modern network operations as a console cable. Managing branch checkouts, merging configurations via pull requests and conducting peer reviews are critical strategies for preventing team members from overwriting active configurations. 
Next, I learned technically how to write Ansible playbooks using NETCONF and YANG models to interact with a working IOS XR device. Lastly, separating the operational state retrieval from active state modifications taught me the importance of modularity. This architecture ensures that the operations team can safely query a network environment at any time without accidental configurations occurring.

