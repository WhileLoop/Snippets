#!/bin/bash
# Configure Xvfb as a service.

sudo tee /etc/init.d/xvfb > /dev/null <<EOL
### BEGIN INIT INFO
# Provides: Xvfb
# Required-Start: $local_fs $remote_fs
# Required-Stop:
# X-Start-Before:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Loads X Virtual Frame Buffer
### END INIT INFO

XVFB=/usr/bin/Xvfb
XVFBARGS=":99 -screen 0 1920x1080x24"
PIDFILE=/var/run/xvfb.pid
case "\$1" in
  start)
    echo -n "Starting virtual X frame buffer: Xvfb"
    start-stop-daemon --start --quiet --pidfile \$PIDFILE --make-pidfile --background --exec \$XVFB -- \$XVFBARGS
    echo "."
    ;;
  stop)
    echo -n "Stopping virtual X frame buffer: Xvfb"
    start-stop-daemon --stop --quiet --pidfile \$PIDFILE
    echo "."
    ;;
  restart)
    \$0 stop
    \$0 start
    ;;
  *)
  echo "Usage: /etc/init.d/xvfb {start|stop|restart}"
  exit 1
esac
exit 0
EOL

sudo chmod +x /etc/init.d/xvfb
sudo update-rc.d xvfb defaults
sudo sh -c "echo DISPLAY=:99 >> /etc/environment"
source /etc/environment
sudo /etc/init.d/xvfb start
