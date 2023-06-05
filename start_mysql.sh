docker run -d -p 3306:3306 \
           --name mysql-docker-container \
           -e MYSQL_ROOT_PASSWORD=w8woord \
           -e MYSQL_DATABASE=codetest \
           -e MYSQL_USER=pieter \
           -e MYSQL_PASSWORD=w8woord \
           mysql/mysql-server:latest
