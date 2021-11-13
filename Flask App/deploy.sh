echo "Removing previous docker containers if any..."
docker-compose down --rmi all -v
echo "Pulling new changes and building new images..."
docker-compose pull
docker-compose build --no-cache
docker-compose up -d
echo "Server is up!"