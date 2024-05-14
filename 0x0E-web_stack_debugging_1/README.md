# 0x0E. Web stack debugging #1

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   Your Puppet manifests must pass `Shellcheck` version 0.3.7 without any errors.
*   All your Bash script files must be executable.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.
*   You can’t use `systemctl` for restarting a process.
*   You are not allowed to use `wget`.

## Project Description.
Learn what is the main role of a web server.
What is a child process.
Why web servers usually have a parent process and child processes.
What are the main HTTP requests.
What DNS stands for and its main role.


### [0. Nginx likes port 80](0-nginx_likes_port_80)
* Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix. - `0-nginx_likes_port_80`.

  Requirements:

  * Nginx must be running, and listening on port `80` of all the server’s active IPv4 IPs.
  * Write a Bash script that configures a server to the above requirements.

---

### [1. Make it sweet and short](1-debugging_made_short)
* Using what you did for task #0, make your fix short and sweet. - `1-debugging_made_short`.

  Requirements:

  * Your Bash script must be 5 lines long or less.
  * There must be a new line at the end of the file.
  * You must respect usual Bash script requirements.
  * You cannot use `;`.
	* You cannot use `&&`.
	* You cannot execute your previous answer file (Do not include the name of the previous script in this one).
	* `service` (init) must say that `nginx` is not running ← for real.
