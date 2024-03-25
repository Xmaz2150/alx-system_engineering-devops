#!/usr/bin/env bash
# transfers a file to remote server using scp
if [ "$#" -lt 4 ]; then
  echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
  scp -i "${4}" -o StrictHostKeyChecking=no "${1}" "${3}@${2}:~/"
fi
