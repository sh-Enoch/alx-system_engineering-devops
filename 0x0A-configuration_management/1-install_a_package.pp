#install puppet-lint
class { 'python': }
python::pip { 'flask':
    version => '2.1.0'
    provider => 'pip3'
}
