# Use rsync through cygwin on Windows only. Everyone else gets standard vboxfs.

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  if Vagrant::Util::Platform.windows?
    # Hack to enable cygwin support.
    ENV["VAGRANT_DETECTED_OS"] = ENV["VAGRANT_DETECTED_OS"].to_s + " cygwin"
    config.vm.synced_folder ".", "/vagrant", type: "rsync",
  end
end
