# fix apache returning 500 error


exec{ 'fix-wordpress':
    command => 'sed -i "s/phpp/php" /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
    }
