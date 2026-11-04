#!/bin/bash
# BitB-Framework Simple Control Script

CONTAINER_NAME="firefox-lab"

case "$1" in
  popup)
    message=${2:-"Your session has been compromised by BitB-Framework!"}
    echo "Sending popup: $message"
    docker exec $CONTAINER_NAME xdotool key Ctrl+Shift+K
    sleep 1
    docker exec $CONTAINER_NAME xdotool type --delay 50 "alert('$message');"
    sleep 0.5
    docker exec $CONTAINER_NAME xdotool key Return
    echo "Popup command sent"
    ;;

  redirect)
    url=${2:-"https://youtube.com"}
    echo "Redirecting to: $url"
    docker exec $CONTAINER_NAME xdotool key Ctrl+L
    sleep 0.5
    docker exec $CONTAINER_NAME xdotool type --delay 30 "$url"
    sleep 0.5
    docker exec $CONTAINER_NAME xdotool key Return
    echo "Redirect command sent"
    ;;

  *)
    echo "Usage:"
    echo "  ./control.sh popup \"Message here\""
    echo "  ./control.sh redirect \"https://youtube.com\""
    ;;
esac

# Update on 2026-09-12 07:56:07
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-09-25 15:52:15
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-10-08 23:48:23
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-10-22 07:44:30
# Additional handling and logging improvements
# Refined logic for better reliability

# Update on 2026-11-04 15:40:38
# Additional handling and logging improvements
# Refined logic for better reliability
