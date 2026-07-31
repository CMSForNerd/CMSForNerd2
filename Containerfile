# ==============================================================================
# Protocol    : Deep State of Mind (DSOM) For My AI
# Author      : Harisfazillah Jamel (LinuxMalaysia)
# Timestamp   : 2026-07-31
# License     : GNU General Public License v3.0
# Standard    : UK English | DBP-standard Bahasa Melayu Malaysia (Piawai)
# ==============================================================================
# =============================================================================
# CMSForNerd2 v2.0.0 - Containerfile for Render Production Deployments (NGINX/Astro 7.1)
# =============================================================================

# Stage 1: Build environment
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependency definitions
COPY package*.json ./

# Install dependencies with legacy peer dependency resolution
RUN npm install --legacy-peer-deps

# Copy workspace source files
COPY . .

# Compile static assets
RUN npm run build

# Stage 2: Production runtime environment (NGINX Alpine Slim)
FROM nginx:alpine-slim AS runtime

# Copy custom unprivileged NGINX configuration
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Copy compiled static assets from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Configure unprivileged execution directories and customise permissions
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html && \
    mkdir -p /var/cache/nginx/client_temp \
             /var/cache/nginx/proxy_temp \
             /var/cache/nginx/fastcgi_temp \
             /var/cache/nginx/uwsgi_temp \
             /var/cache/nginx/scgi_temp && \
    chown -R nginx:nginx /var/cache/nginx /var/run /var/log/nginx && \
    touch /var/run/nginx.pid && \
    chown nginx:nginx /var/run/nginx.pid

# Switch to unprivileged nginx runtime user
USER nginx

# Expose unprivileged web port
EXPOSE 8080

# Run NGINX in foreground
CMD ["nginx", "-g", "daemon off;"]
