docker compose -f services/duckdns.yml up -d --remove-orphans
docker compose -f services/nextcloud.yml up -d --remove-orphans
docker compose -f services/jellyfin.yml up -d --remove-orphans