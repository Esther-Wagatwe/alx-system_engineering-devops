# 0x0C. Web server

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" />
</p>

## Learning Objectives

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

## Requirements

- All files are created and compiled on Ubuntu 14.04.4 LTS
- All Bash scripts are linted with Shellcheck
- All Puppet scripts are linted with Puppet Lint 2.1.1

## Resource

<details>
<summary><a href="https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes">Child Process</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/bw6hYBS5/image.png' border='0' alt='image'/></a>
</details>

- [Background contenxt](https://www.youtube.com/watch?v=AZg4uJkEa-4)
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
- [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

## Tasks

### [0. Transfer a file to your server](./0-transfer_file)

- Write a Bash script that transfers a file from our client to a server:
  - Accepts 4 parameters
    - The path to the file to be transferred
    - The IP of the server we want to transfer the file to
    - The username scp connects with
    - The path to the SSH private key that scp uses
  - Display Requirements: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
  - scp must transfer the file to the user home directory ~/
  - Strict host key checking must be disabled when using scp

### [1. Install nginx web server](./1-install_nginx_web_server)

- Web servers are the piece of software generating and serving HTML pages, let’s install one!

  - Install nginx on your web-01 server
  - Nginx should be listening on port 80
  - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
  - As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

### [2. Setup a domain name](./2-setup_a_domain_name)

- .TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.
  - Provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
  - Configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
  - Go to your profile and enter your domain in the Project website url field

### [3. Redirection](./3-redirection)

- Configure your Nginx server so that /redirect_me is redirecting to another page.
  - The redirection must be a “301 Moved Permanently”
  - You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
  - Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

### [4. Not found page 404](./4-not_found_page_404)

- Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

  - The page must return an HTTP 404 error code
  - The page must contain the string Ceci n'est pas une page
  - Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task

### [5. Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp)

- Install and configure an Nginx server using Puppet instead of Bash.
    - Nginx should be listening on port 80
    - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
    - The redirection must be a “301 Moved Permanently”
    - Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements

