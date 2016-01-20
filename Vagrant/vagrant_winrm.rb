# vagrant rdp
Vagrant.configure("2") do |config|
    config.vm.box = "opentable/win-2012r2-standard-amd64-nocm" # vagrant/vagrant
    config.vm.communicator = "winrm"
    config.vm.network :forwarded_port, guest: 5985, host: 5985, id: "winrm", auto_correct: true
    config.vm.network :forwarded_port, guest: 3389, host: 33389
    config.vm.guest = :windows
    config.winrm.username = "vagrant"
    config.vm.provision "shell", inline: "Write-Output $env:username"
end
