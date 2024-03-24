# setup client SSH config file so i can connect to server without passwd

file_line { 'private_key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'password_authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
