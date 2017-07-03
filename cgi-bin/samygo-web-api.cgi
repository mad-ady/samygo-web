#!/mnt/opt/privateer/usr/bin/php-cgi
<?php
$LIBSDIR='/mnt/opt/privateer/usr/libso';
$SAMYGOSO='/mnt/opt/privateer/usr/bin/samyGOso';
$SAMYGORC='/mnt/opt/privateer/usr/bin/samyGOrc';
$BIN='/mnt/bin';

$KEYS= array(
    KEY_MTS => 0,
    KEY_SOURCE => 1,
    BD_KEY_POWER => 2,
    KEY_SLEEP => 3,
    KEY_1 => 4,
    KEY_2 => 5,
    KEY_3 => 6,
    KEY_VOLUP => 7,
    KEY_4 => 8,
    KEY_5 => 9,
    KEY_6 => 10,
    KEY_VOLDOWN => 11,
    KEY_7 => 12,
    KEY_8 => 13,
    KEY_9 => 14,
    KEY_MUTE => 15,
    KEY_CHDOWN => 16,
    KEY_0 => 17,
    KEY_CHUP => 18,
    KEY_PRECH => 19,
    KEY_GREEN => 20,
    KEY_YELLOW => 21,
    KEY_CYAN => 22,
    KEY_VAL_23 => 23,
    KEY_VAL_24 => 24,
    KEY_ADDDEL => 25,
    KEY_MENU => 26,
    KEY_TV => 27,
    KEY_VAL_28 => 28,
    KEY_VAL_29 => 29,
    KEY_VAL_30 => 30,
    KEY_INFO => 31,
    KEY_PIP_ONOFF => 32,
    KEY_PIP_SWAP => 33,
    KEY_VAL_34 => 34,
    KEY_PLUS100 => 35,
    KEY_VAL_36 => 36,
    KEY_CAPTION => 37,
    KEY_VAL_38 => 38,
    KEY_AD => 39,
    KEY_PMODE => 40,
    KEY_VAL_41 => 41,
    KEY_VAL_42 => 42,
    KEY_VAL_43 => 43,
    KEY_TTX_MIX => 44,
    KEY_EXIT => 45,
    KEY_VAL_46 => 46,
    KEY_PIP_SIZE => 47,
    KEY_MAGIC_CHANNEL => 48,
    KEY_PIP_SCAN => 49,
    KEY_PIP_CHUP => 50,
    KEY_PIP_CHDOWN => 51,
    KEY_DEVICE_CONNECT => 52,
    KEY_HELP => 53,
    KEY_ANTENA => 54,
    KEY_CONVERGENCE => 55,
    KEY_11 => 56,
    KEY_12 => 57,
    KEY_AUTO_PROGRAM => 58,
    KEY_RSURF => 61,
    KEY_PICTURE_SIZE => 62,
    KEY_TOPMENU => 63,
    KEY_GAME => 64,
    KEY_QUICK_REPLAY => 65,
    KEY_STILL_PICTURE => 66,
    KEY_DTV => 67,
    KEY_FAVCH => 68,
    KEY_REWIND => 69,
    KEY_STOP => 70,
    KEY_PLAY => 71,
    KEY_FF => 72,
    KEY_REC => 73,
    KEY_PAUSE => 74,
    KEY_TOOLS => 75,
    KEY_INSTANT_REPLAY => 76,
    KEY_LINK => 77,
    KEY_FF_ => 78,
    KEY_GUIDE => 79,
    KEY_REWIND_ => 80,
    KEY_ANGLE => 81,
    KEY_RESERVED1 => 82,
    KEY_ZOOM1 => 83,
    KEY_PROGRAM => 84,
    KEY_BOOKMARK => 85,
    KEY_DISC_MENU => 86,
    KEY_PRINT => 87,
    KEY_RETURN => 88,
    KEY_SUB_TITLE => 89,
    KEY_CLEAR => 90,
    KEY_VCHIP => 91,
    KEY_REPEAT => 92,
    KEY_DOOR => 93,
    KEY_OPEN => 94,
    KEY_WHEEL_LEFT => 95,
    KEY_UP => 96,
    KEY_DOWN => 97,
    KEY_RIGHT => 98,
    KEY_DMA => 99,
    KEY_TURBO => 100,
    KEY_LEFT => 101,
    KEY_FM_RADIO => 102,
    KEY_DVR_MENU => 103,
    KEY_ENTER => 104,
    KEY_PCMODE => 105,
    KEY_TTX_SUBFACE => 106,
    KEY_CH_LIST => 107,
    KEY_RED => 108,
    KEY_DNIe => 109,
    KEY_SRS => 110,
    KEY_CONVERT_AUDIO_MAINSUB => 111,
    KEY_MDC => 112,
    KEY_SEFFECT => 113,
    KEY_DVR => 114,
    KEY_DTV_SIGNAL => 115,
    KEY_LIVE => 116,
    KEY_PERPECT_FOCUS => 117,
    KEY_HOME => 118,
    KEY_ESAVING => 119,
    KEY_WHEEL_RIGHT => 120,
    KEY_CONTENTS => 121,
    KEY_VCR_MODE => 122,
    KEY_CATV_MODE => 123,
    KEY_DSS_MODE => 124,
    KEY_TV_MODE => 125,
    KEY_DVD_MODE => 126,
    KEY_STB_MODE => 127,
    KEY_CALLER_ID => 128,
    KEY_SCALE => 129,
    KEY_ZOOM_MOVE => 130,
    KEY_CLOCK_DISPLAY => 131,
    KEY_AV1 => 132,
    KEY_SVIDEO1 => 133,
    KEY_COMPONENT1 => 134,
    KEY_SETUP_CLOCK_TIMER => 135,
    KEY_COMPONENT2 => 136,
    KEY_MAGIC_BRIGHT => 137,
    KEY_DVI => 138,
    KEY_HDMI => 139,
    KEY_W_LINK => 140,
    KEY_DTV_LINK => 141,
    KEY_VAL_142 => 142,
    KEY_APP_LIST => 143,
    KEY_BACK_MHP => 144,
    KEY_ALT_MHP => 145,
    KEY_DNSe => 146,
    KEY_RSS => 147,
    KEY_ENTERTAINMENT => 148,
    KEY_ID_INPUT => 149,
    KEY_ID_SETUP => 150,
    KEY_ANYNET => 151,
    KEY_POWEROFF => 152,
    KEY_POWERON => 153,
    KEY_ANYVIEW => 154,
    KEY_MS => 155,
    KEY_MORE => 156,
    KEY_PANNEL_POWER => 157,
    KEY_PANNEL_CHUP => 158,
    KEY_PANNEL_CHDOWN => 159,
    KEY_PANNEL_VOLUP => 160,
    KEY_PANNEL_VOLDOW => 161,
    KEY_PANNEL_ENTER => 162,
    KEY_PANNEL_MENU => 163,
    KEY_PANNEL_SOURCE => 164,
    KEY_AV2 => 165,
    KEY_AV3 => 166,
    KEY_SVIDEO2 => 167,
    KEY_SVIDEO3 => 168,
    KEY_ZOOM2 => 169,
    KEY_PANORAMA => 170,
    KEY_4_3 => 171,
    KEY_16_9 => 172,
    KEY_DYNAMIC => 173,
    KEY_STANDARD => 174,
    KEY_MOVIE1 => 175,
    KEY_CUSTOM => 176,
    KEY_AUTO_ARC_RESET => 177,
    KEY_AUTO_ARC_LNA_ON => 178,
    KEY_AUTO_ARC_LNA_OFF => 179,
    KEY_AUTO_ARC_ANYNET_MODE_OK => 180,
    KEY_AUTO_ARC_ANYNET_AUTO_START => 181,
    KEY_AUTO_FORMAT => 182,
    KEY_DNET => 183,
    KEY_HDMI1 => 184,
    KEY_AUTO_ARC_CAPTION_ON => 185,
    KEY_AUTO_ARC_CAPTION_OFF => 186,
    KEY_AUTO_ARC_PIP_DOUBLE => 187,
    KEY_AUTO_ARC_PIP_LARGE => 188,
    KEY_AUTO_ARC_PIP_SMALL => 189,
    KEY_AUTO_ARC_PIP_WIDE => 190,
    KEY_AUTO_ARC_PIP_LEFT_TOP => 191,
    KEY_AUTO_ARC_PIP_RIGHT_TOP => 192,
    KEY_AUTO_ARC_PIP_LEFT_BOTTOM => 193,
    KEY_AUTO_ARC_PIP_RIGHT_BOTTOM => 194,
    KEY_AUTO_ARC_PIP_CH_CHANGE => 195,
    KEY_AUTO_ARC_AUTOCOLOR_SUCCESS => 196,
    KEY_AUTO_ARC_AUTOCOLOR_FAIL => 197,
    KEY_AUTO_ARC_C_FORCE_AGING => 198,
    KEY_AUTO_ARC_USBJACK_INSPECT => 199,
    KEY_AUTO_ARC_JACK_IDENT => 200,
    KEY_NINE_SEPERATE => 201,
    KEY_ZOOM_IN => 202,
    KEY_ZOOM_OUT => 203,
    KEY_MIC => 204,
    KEY_HDMI2 => 205,
    KEY_HDMI3 => 206,
    KEY_AUTO_ARC_CAPTION_KOR => 207,
    KEY_AUTO_ARC_CAPTION_ENG => 208,
    KEY_AUTO_ARC_PIP_SOURCE_CHANGE => 209,
    KEY_HDMI4 => 210,
    KEY_AUTO_ARC_ANTENNA_AIR => 211,
    KEY_AUTO_ARC_ANTENNA_CABLE => 212,
    KEY_AUTO_ARC_ANTENNA_SATELLITE => 213,
    KEY_EXT1 => 214,
    KEY_EXT2 => 215,
    KEY_EXT3 => 216,
    KEY_EXT4 => 217,
    KEY_EXT5 => 218,
    KEY_EXT6 => 219,
    KEY_EXT7 => 220,
    KEY_EXT8 => 221,
    KEY_EXT9 => 222,
    KEY_EXT10 => 223,
    KEY_EXT11 => 224,
    KEY_EXT12 => 225,
    KEY_EXT13 => 226,
    KEY_EXT14 => 227,
    KEY_EXT15 => 228,
    KEY_EXT16 => 229,
    KEY_EXT17 => 230,
    KEY_EXT18 => 231,
    KEY_EXT19 => 232,
    KEY_EXT20 => 233,
    KEY_EXT21 => 234,
    KEY_EXT22 => 235,
    KEY_EXT23 => 236,
    KEY_EXT24 => 237,
    KEY_EXT25 => 238,
    KEY_EXT26 => 239,
    KEY_EXT27 => 240,
    KEY_EXT28 => 241,
    KEY_EXT29 => 242,
    KEY_EXT30 => 243,
    KEY_EXT31 => 244,
    KEY_EXT32 => 245,
    KEY_EXT33 => 246,
    KEY_EXT34 => 247,
    KEY_EXT35 => 248,
    KEY_EXT36 => 249,
    KEY_EXT37 => 250,
    KEY_EXT38 => 251,
    KEY_EXT39 => 252,
    KEY_EXT40 => 253,
    KEY_EXT41 => 254,
);

// Parse arguments
parse_str($_SERVER["QUERY_STRING"], $params);

//read the local challenge
$challenge = trim(file_get_contents("/mnt/etc/samygo-web-api.challenge"));

if($params['challenge'] == $challenge){
	switch($params['action']){
		case 'CHANNELINFO':
			header("Content-Type: application/json; charset=UTF-8");
			error_log("Processing CHANNELINFO");
			if(getLock()){
				$exec=`$SAMYGOSO -d -A -B -l "$LIBSDIR/libLogChannel.so" 2>/dev/null 1>&2`;
				releaseLock();
				sleep(1);
				
				
				#process the log
				$channel_info=file_get_contents("/dtv/LogChannel.log");
				
				#$channel_info=`$BIN/cat /dtv/LogChannel.log | $BIN/grep "Source:" -A 8 | $BIN/sed -e "s/[^ ]* \(.*\)/\1/g"`;
				error_log("Received output: $channel_info");
				//Split the output into tokens:
				/*
	Source: TV (0)
	PVR Status: NONE
	PowerState: Normal
	TV mode: Cable (1)
	Volume: 6 (mute)
	Channel number: 44
	Channel name: Nat Geo
	Program name: Geniul: Einstein
	Resolution: 720x576
				 */
				 $channel_lines=explode("\n", $channel_info);
				 $output = array();
				 foreach ($channel_lines as $line){
					 error_log("Looking at $line");
					 if(preg_match('/\[[^\]]+\]\s+([^:]+):(.*)/', $line, $tokens)){
						 
						 #$tokens = explode(":", $line);
						 
						 #process the first token to remove spaces, lowercase
						 $tokens[1]=preg_replace('/\s+/', '_', $tokens[1]);
						 $tokens[1]=strtolower($tokens[1]);
						 $tokens[2]=trim($tokens[2]);
						 
						 #save it into the output
						 $output[$tokens[1]]=$tokens[2];
						 
						 #if power_state == Soft-Off don't record the program name
						 if($tokens[1] == 'program_name' && $output['power_state'] == 'Soft-Off'){
							 error_log("The TV is off. Ignoring program name");
							 $output[$tokens[1]] = 'Off';
						 }
						 
						 if($tokens[1] == 'program_name' && preg_match('/HDMI|Undefined/', $output['source'])){
							 error_log("The TV is tuned to a different source.");
							 $output[$tokens[1]] = 'Non-TV';
						 }
						 error_log("Saving $tokens[1] = $tokens[2]");
					}
					 
				 }
				 $output['error']=false;
				 echo json_encode($output);
			 }
			 else{
				 echo json_encode( array('error' => true, 'message' => "Unable to get an injection lock. Try again later"));
			 }
			 break;
	    case 'KEY':
			header("Content-Type: application/json; charset=UTF-8");
			error_log("Processing KEY");
			if(array_key_exists( 'key', $params)){
				$key=null;
				if(! is_numeric($params['key'])){
					error_log("Resolving key ".$params['key']);
					#convert the key string to its value
					if(array_key_exists($params['key'], $KEYS)){
						$key = $KEYS[$params['key']];
					}
					else{
						echo json_encode( array('error' => true, 'message' => "Key ".$params['key']." is not supported"));
						exit;
					}
				}
				else{
					$key = $params['key'];
				}
				
				#do the injection
				if(getLock()){
					
					$exec=`$SAMYGORC -d -p $($BIN/pidof exeTV || $BIN/pidof exeDSP) $key 2>/dtv/keys.txt 1>&2`;
					releaseLock();
					sleep(1);
					echo json_encode( array('error' => false, 'message' => "Sent key $key"));
				}
				else{
					echo json_encode( array('error' => true, 'message' => "Unable to get an injection lock. Try again later"));
				}
				
			}
			else{
				echo json_encode( array('error' => true, 'message' => "Key parameter missing"));
			}
			break;
		case 'REBOOT':
			header("Content-Type: application/json; charset=UTF-8");
			error_log("Processing REBOOT");
			echo json_encode( array('error' => false, 'message' => "Rebooting TV"));
			#the TV reboots immediately and the socket might time out
			$exec=`/sbin/micom reboot`;
			break;
		case 'SNAPSHOT':
			error_log("Processing SNAPSHOT");
			//see if TV is on or off by checking /dtv/tvIsSleeping
			$file="";
			if(! file_exists("/dtv/tvIsSleeping")){
				#TV is on. Get a list of existing screenshots
				$initialFiles = glob("/dtv/*.bmp");
				#take the screenshot
				if(getLock()){
					$exec=`$SAMYGOSO -d -T -B -l $LIBSDIR/libScreenShot.so PATH:/dtv  UPSIDE`;
					sleep(1);
					releaseLock();
					#We need to find out  the filename
					$currentFiles = glob("/dtv/*.bmp");
					foreach ($currentFiles as $filename){
						if(! array_key_exists($filename, $initialFiles)){
							#this looks like a new file. Convert it to jpeg
							$exec=`$BIN/cjpeg -q 95 $filename > /dtv/screenshot.jpg`;
							#remove the bmp file
							unlink("$filename");
							$file="/dtv/screenshot.jpg";
							break;
						}
					}
				}
				else{
					#couldn't get a lock. Return a generic image
					$file="/mnt/var/www/samygo-web-api/colorbars.jpg";
				}
			}
			else{
				#TV is off. No need to query it, just return a static image
				$file="/mnt/var/www/samygo-web-api/colorbars.jpg";
			}
			
			header("Content-Type: image/jpeg");
			header("Content-Length: " . filesize($file));
			$fp = fopen($file, 'rb');
			fpassthru($fp);
			exit;			
			break;
		default:
			header("Content-Type: application/json; charset=UTF-8");
			echo json_encode( array('error' => true, 'message' => "Bad action ".$params['action']));
		
	}
}
else{
	header("Content-Type: application/json; charset=UTF-8");
	#challenge doesn't match
	echo json_encode( array('error' => true, 'message' => 'Bad request (challenge)') );
}

//get a lock to do an injection
function getLock(){
	$count = 0;
	$available = false;
	while($count < 20){
		if(file_exists("/dtv/injection.lock")){
			#a lock is active. Wait until it finishes and is released
			sleep(0.5);
		}
		else{
			#we can get the lock
			if(touch("/dtv/injection.lock")){
				$available = true;
				break;
			}
			else{
				#couldn't get the lock
				error_log("Couldn't get the injection lock");
			}
		}
	}
	return $available;
}

//release the lock
function releaseLock(){
	$success=false;
	if(file_exists("/dtv/injection.lock")){
		if(unlink("/dtv/injection.lock")){
			$sucess=true;
		}
		else{
			error_log("Unable to release injection lock");
		}
	}
	else{
		$success=true;
	}
	return $success;
}
?>
