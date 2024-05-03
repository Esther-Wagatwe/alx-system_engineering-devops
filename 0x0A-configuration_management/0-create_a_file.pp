#Defines a resource to manage the /tmp/school file

file { '/tmp/school':
    ensure  => file,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => "I love Puppet\n",
}
