#! /bin/sh
docker run --rm -v stream_PGDATA:/PGDATA -v /$PWD/../DATABASE:/backup ubuntu bash -c "cd /PGDATA && tar cvfz /backup/backup.tgz *"