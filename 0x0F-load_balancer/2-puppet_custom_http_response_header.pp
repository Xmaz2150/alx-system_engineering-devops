# configure nginx with puppet

exec { 'update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}

