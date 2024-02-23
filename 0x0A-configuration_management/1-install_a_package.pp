# 1-install_a_package.pp

# Install the flask packages from pip3
package { 'flask' :
    ensure   => '2.1.0',
    provider => 'pip3',
}
# Install the werkzueg package
package { 'Werkzeug':
  ensure   => '2.2.2',
  provider => 'pip3',
}
