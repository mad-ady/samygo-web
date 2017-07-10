#/mnt/bin/sh
DIR=`dirname "$0"`
echo "Installing samygo-web-api cgi component from $DIR to /mnt/var/www/samygo-web-api/"
if [ ! -d "/mnt/var/www/samygo-web-api/" ]; then
    mkdir -p /mnt/var/www/samygo-web-api/
fi
cp -a "$DIR/colorbars.jpg" /mnt/var/www/samygo-web-api/
cp -a "$DIR/cgi-bin/samygo-web-api.cgi" /mnt/var/www/samygo-web-api/

echo "Installing cjpeg dependency to /mnt"
cp -a "$DIR/cjpeg/cjpeg" /mnt/bin/
cp -a "$DIR/cjpeg/libjpeg.so.62" /mnt/usr/lib/

echo "Installing startup script to /mnt/etc/init.d/"
cp -a "$DIR/init.d/99_99_samygo_web_api.init" /mnt/etc/init.d/

echo -n "Checking if apache is running... ";
out=`netstat -tpan | grep 1080 | grep httpd | grep LISTEN | wc -l`;
if [ "$out" -gt 0 ]; then
  echo " [  OK  ]"
else
  echo " [ FAIL ]"
fi

echo 
echo "Installation is complete. Remember, for the web api to function, it needs the following external dependencies:"
echo -n " * samyGOso: https://forum.samygo.tv/viewtopic.php?t=6186 "
if [ -x "/mnt/opt/privateer/usr/bin/samyGOso" ]; then
  echo "[ FOUND ]"
else
  echo "[MISSING]"
fi

echo -n " * samyGOrc: https://forum.samygo.tv/viewtopic.php?f=63&t=6395 "
if [ -x "/mnt/opt/privateer/usr/bin/samyGOrc" ]; then
  echo "[ FOUND ]"
else
  echo "[MISSING]"
fi

echo -n " * libLogChannel: https://forum.samygo.tv/viewtopic.php?f=63&t=8717 "
if [ -f "/mnt/opt/privateer/usr/libso/libLogChannel.so" ]; then
  echo "[ FOUND ]"
else
  echo "[MISSING]"
fi

echo -n " * libScreenShot: https://forum.samygo.tv/viewtopic.php?t=9201 "
if [ -f "/mnt/opt/privateer/usr/libso/libScreenShot.so" ]; then
  echo "[ FOUND ]"
else
  echo "[MISSING]"
fi

echo 
echo "To start the web API and generate your key please run:"
echo "  /mnt/etc/init.d/99_99_samygo_web_api.init start"
echo 
echo "The web api will be available at http://tv-ip:1080/cgi-bin/samygo-web-api.cgi"
echo "Consult the API documentation at https://github.com/mad-ady/samygo-web"
