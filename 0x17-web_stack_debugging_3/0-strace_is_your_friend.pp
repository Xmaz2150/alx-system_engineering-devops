# Fix apache 500 internal caused by typo in the wordpress settings

exec { 'fix-apache':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin:/usr/bin', '/sbin:/bin'],
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}
