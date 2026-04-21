FROM n8nio/n8n:latest
USER root

# Copy assets with correct ownership in one layer (avoids chown doubling disk usage)
COPY --chown=node:node books/       /home/node/nets/books/
COPY --chown=node:node frameworks/  /home/node/nets/frameworks/

USER node
