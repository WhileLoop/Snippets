case "$1" in
  start)
        # Start

        ;;
  stop)
        # Stop daemons.

        ;;
  restart)
        $0 stop
        $0 start
        ;;
  *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
esac
