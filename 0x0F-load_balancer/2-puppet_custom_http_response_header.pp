# Using Puppet| Install Nginx server, setup and configuration

#update software packages list
exec { 'update packages':
    command => 'apt-get update',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

#install nginx
package { 'nginx':
    ensure => 'installed'
}

# allow HTTP
#exec { 'allow HTTP':
#  command => "/usr/sbin/ufw allow 'Nginx HTTP'",
#  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
#  onlyif  =>'/usr/bin/dpkg -l nginx | grep ^ii', 
#}

# create index file
file { '/var/www/html/index.html':
    content => 'Hello World!\n'
}

# create index file
file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page\n"
}

# add redirection and error page
file { 'Default Nginx file':
    ensure  => file,
    path    => '/etc/nginx/sites-enabled/default',
    content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        add_header X-Served-By $hostname;
        location / {
                try_files \$uri \$uri/ =404;
        }

        error_page 404 /404.html;
        location /404.html {
            internal;
        }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=BXd62mMu1UY&list=RDBXd62mMu1UY&start_radio=1;
    }
    }",
}

# restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start service nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
