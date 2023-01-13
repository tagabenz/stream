#! /bin/sh
docker exec stream-db-1 pg_dump stream_db > /$PWD/../DATABASE/stream.sql
