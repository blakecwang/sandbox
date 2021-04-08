# -*- mode: ruby -*-
# vi: set ft=ruby :

class VagrantPlugins::ProviderVirtualBox::Action::Network
  def dhcp_server_matches_config?(dhcp_server, config)
    true
  end
end

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.disksize.size = "10GB"

  config.ssh.username = "sandbox"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Configure virtualbox settings to use 4GB of memory. Tweak as necessary.
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
    config.vm.network "private_network", :type => 'dhcp', :name => 'vboxnet1', :adapter => 2

    # Share an additional folder to the guest VM. The first argument is
    # the path on the host to the actual folder. The second argument is
    # the path on the guest to mount the folder. And the optional third
    # argument is a set of non-required options.
    #
    # https://blog.theodo.com/2017/07/speed-vagrant-synced-folders/
    # https://stackoverflow.com/questions/42758577/how-to-improve-slow-shared-folders-in-vagrant

    config.vm.synced_folder "vmshare", "/home/sandbox/vmshare",
       mount_options: ["rw", "vers=3", "tcp"],
       linux__nfs_options: ["rw", "no_subtree_check", "all_squash", "async"],
       nfs: true
  end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
