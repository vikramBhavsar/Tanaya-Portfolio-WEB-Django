#!/bin/bash

cd /tanayaPortfolio/clientApp
echo "Installing node packages"
yarn install
echo "building the application"
npm run build-watch

chmod +x /tanayaPortfolio
chmod +x /tanayaPortfolio/staticfiles
cp -r /tanayaPortfolio/clientApp/dist/tanaya-artist-portfolio/* /usr/share/nginx/html
cp /tanayaPortfolio/clientApp/nginx.conf /etc/nginx/nginx.conf

nginx -s reload
nginx -g 'daemon off;';
