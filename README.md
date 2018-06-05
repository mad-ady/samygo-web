SamyGO web API

The Web API exposes some of SamyGO's plugins to external clients. The API tries to return data in json format where possible, but uses image/jpg for screenshots.

Features:
* Get TV State and current program details via libLogChannel
* Control the TV via samyGOrc with remote actions
* Reboot the TV
* Get a screenshot of what is on the screen via libScreenShot
* Start a widget via libRunWidget
* Display an onscreen message via libAlert
* Compatibility with libSoftPowerOff (https://forum.samygo.tv/viewtopic.php?t=8987&start=230)

Dependencies:
* Apache (/mnt/etc/init.d/06_05_apache.init)
* samyGOso: https://forum.samygo.tv/viewtopic.php?t=6186
* samyGOrc: https://forum.samygo.tv/viewtopic.php?f=63&t=6395
* libLogChannel: https://forum.samygo.tv/viewtopic.php?f=63&t=8717 
* libScreenShot: https://forum.samygo.tv/viewtopic.php?t=9201 
* libRunWidget: https://forum.samygo.tv/viewtopic.php?f=63&t=9306
* libAlert: https://forum.samygo.tv/viewtopic.php?f=63&t=9099

Installation:
* Download to your rooted SamyGO TV:
```
cd /tmp
curl -k https://codeload.github.com/mad-ady/samygo-web/zip/master > samygo-web-api.zip
```
* Unzip
```
unzip samygo-web-api.zip
```
* Run the installation script:
```
./samygo-web-master/installer.sh
```

LibSoftPowerOff coexistence:
If you have libSoftPowerOff enabled in your TV and you use the screenshot functionality, in order not to inject the screenshot command when the display is off you can signal that the TV is in soft-off mode by configuring libSoftPowerOff.so to run two scripts on power on/off. When you load the libSoftPowerOff library, use the following options:
```CMD_ON:/mnt/scripts/onPowerOn.sh CMD_OFF:/mnt/scripts/onPowerOff.sh```
The onPowerOn.sh/onPowerOff.sh scripts (among other functionality) should set a flag by creating a file called ```/dtv/tvIsSleeping```:
* onPowerOn.sh: rm -f /dtv/tvIsSleeping
* onPowerOff.sh: touch /dtv/tvIsSleeping

If you don't use libSoftPowerOff, the TV powers off and the web API is no longer accessible.

Startup:
```
/mnt/etc/init.d/99_99_samygo_web_api.init start
```
* On first run the startup script will generate a unique challenge which will be printed by the startup screen. This challenge is generated in /mnt/etc/samygo-web-api.challenge. You will need to supply this challenge string on all requests. The security is equivalent to HTTP Simple Auth and should protect you against somebody scanning your system, but will not protect you from a man-in-the middle attack! Also, don't use over unencrypted internet!


API Usage:
* to get the current information, request for action=CHANNELINFO: 

```
$ wget -O - "http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=CHANNELINFO"

{"source":"TV (0)","pvr_status":"NONE","powerstate":"Normal","tv_mode":"Cable (1)","volume":"9","channel_number":"45","channel_name":"Nat Geo HD","program_name":"Planeta dezastrelor","resolution":"1920x1080","error":false}
```

* to reboot TV request for action=REBOOT: 
```
$ wget -O - http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=REBOOT
```

* to send key events request for action=KEY and key=KEY_1:
```
$ wget -O - http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=KEY&key=KEY_1

{"error":false,"message":"Sent key 4"}
```
The list and codes of supported keys are available inside the script in the $KEYS array: https://github.com/mad-ady/samygo-web/blob/master/cgi-bin/samygo-web-api.cgi

* to get a snapshot from the TV request for action=SNAPSHOT:
```
$ wget -O /tmp/image.jpg http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=SNAPSHOT
```

* to run a widget on your TV request for action=WIDGET&name=YouTube (name is case-sensitive):

```
$ wget -O - http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=WIDGET&name=YouTube
```
* to display an onscreen message use action=ALERT&message=This+is+a+test&type=CENTER. You can also use blinks=4&delay=1000 to blink for 4 seconds:
```
$ wget -O - http://tv-ip:1080/cgi-bin/samygo-web-api.cgi?challenge=oyd4uIz5WWAkWPo5MzfxBFraI05C3FDorSPE7xiMLCVAQ40a&action=ALERT&type=CENTER&message=This+is+a+test
```
