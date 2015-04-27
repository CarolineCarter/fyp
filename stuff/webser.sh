IMAGE=$(docker build -t webservices . | tail -1 | awk '{ print $NF }')
MNT="$WORKSPACE/.."
docker rm websers
CONTAINER=$(docker run -d -p 8000:8000 -name websers webservices)
