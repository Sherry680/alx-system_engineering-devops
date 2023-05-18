# sky is the limit, let's bring that limit higher

exec { 'increase the limit'
  command => '/usr/bin/env sed -i s/15/6000/ /etc/default/nginx'
}
-> exec { '/usr/bin/env service nginx restart':
}
