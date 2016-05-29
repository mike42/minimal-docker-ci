FROM debian
ADD . /usr/share/test-server
WORKDIR /usr/share/test-server
RUN apt-get update && apt-get install --assume-yes netcat-openbsd
CMD ./server.sh

