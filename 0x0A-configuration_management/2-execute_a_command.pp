# Kill the process named killmenow
exec { 'killmenow':
  # Use the pkill command
  command => 'pkill killmenow',
  # Only run the command if the process exists
  onlyif  => 'pgrep killmenow',
  # Set the path for the command to execute
  path    => '/bin:/usr/bin',
}
