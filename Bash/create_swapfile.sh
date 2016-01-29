# Create a swapfile and configure it as swap space.
sudo dd if=/dev/zero of=/mnt/swapfile bs=1M count=2048
sudo chown root:root /mnt/swapfile
sudo chmod 600 /mnt/swapfile
sudo mkswap /mnt/swapfile
sudo swapon /mnt/swapfile
echo '/mnt/swapfile swap swap defaults 0 0' | sudo tee --append /etc/fstab
sudo swapon -a
