# SSH

In this project, I became familiar connecting to and working
with servers using the SSH protocol. I worked on a server
provided by ALX.

## Tasks :page_with_curl:

* **0. Use a private key**
  * [0-use_a_private_key](./0-use_a_private_key): Bash script that uses `ssh` to connect to my
ALX-provided server.

* **1. Create an SSH key pair**
  * [1-create_ssh_key_pair](./1-create_ssh_key_pair): Bash script that creates an RSA key pair.

* **2. Client configuration file**
  * [2-ssh_config](./2-ssh_config): SSH configuration file configured to use the private key
`~/.ssh/school` and to refuse authentication using a password.

* **3. Let me in!**
  * Now that you have successfully connected to your server, we would also like to join the party.

  * Add the SSH public key below to your server so that we can connect using the ubuntu user.

* **4. Client configuration file (w/ Puppet)**
  * [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp): setting up client SSH configuration file so that I can connect to a server without typing a password. 
