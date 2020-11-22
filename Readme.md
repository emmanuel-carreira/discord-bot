docker build -t bot_discord .
docker run -itd --rm --name bot_discord bot_discord
docker exec -it bot_discord bash