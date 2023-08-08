FROM nginx:alpine
  COPY default.conf /etc/nginx/conf.d/default.conf
  ENTRYPOINT ["psql -f /db/stream.sql -U postgres"]