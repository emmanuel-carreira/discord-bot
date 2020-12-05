# Build docker image
docker build -t bot_discord .

# Build container from image
docker run -itd --rm --name bot_discord -v ${pwd}:/usr/src/app bot_discord

# Access container bash
docker exec -it bot_discord bash

# Shutdown container
docker stop bot_discord