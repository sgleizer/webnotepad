FROM nginx:1.17.10
# Install apache2-utils to get htpasswd command
RUN apt-get update -y && apt-get install -y apache2-utils && rm -rf /var/lib/apt/lists/*
# auth credentials
RUN htpasswd -c -b /etc/nginx/htpasswd sam 1236

# Nginx config file
WORKDIR /etc/nginx/
COPY . .



