#kills a process
exec {'killmenow':
    path => ['usr/bin', '/usr/sbin',],
    command => 'pkill killmenow',
    }
