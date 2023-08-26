# Client SSH configuration update

file_line {'add-private-key':
path => '/etc/ssh/ssh_config',
line => '	IdentityFile ~/.ssh/school',
replace => true
}


file_line {'password-auth':
path => '/etc/ssh/ssh_config',
line => '	PasswordAuthentication no',
replace => true
}
