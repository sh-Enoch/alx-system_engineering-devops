#install puppet-lint
package { 'flask':
    version => '2.1.0',
    provider => 'pip3',
}

#install wekzeug package
package { 'Werkzeug':
    version => '2.1.1',
    provider => 'pip3',
}

