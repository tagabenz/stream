#! /bin/sh
docker exec stream-db-1 pg_dumpall > /$PWD/../DATABASE/stream.sql
