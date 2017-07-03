SamyGO web API

* Requires that apache is enabled (/mnt/etc/init.d/06_05_apache.init) on port 1080
* Installs in /mnt/var/www/samygo-web


API Usage:
* to get the current information, request for action=CHANNELINFO: http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=CHANNELINFO
The response is in JSON format and looks like:
```
{"source":"TV (0)","pvr_status":"NONE","powerstate":"Normal","tv_mode":"Cable (1)","volume":"9","channel_number":"45","channel_name":"Nat Geo HD","program_name":"Planeta dezastrelor","resolution":"1920x1080","error":false}
```

* to reboot TV request for action=REBOOT: http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=REBOOT

* to send key events request for action=KEY and key=KEY_1: http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=KEY&key=KEY_1
The response is in JSON format:
```
{"error":false,"message":"Sent key 4"}
```

* to get a snapshot from the TV request for action=SNAPSHOT: http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=SNAPSHOT
The result is an image/jpg