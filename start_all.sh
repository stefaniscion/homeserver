docker compose -f services/duckdns/duckdns.yml up -d
docker compose -f services/swag/swag.yml up -d
docker compose -f services/nextcloud/nextcloud.yml up -d
docker compose -f services/jellyfin/jellyfin.yml up -d
docker compose -f services/homeassistant/homeassistant.yml up -d