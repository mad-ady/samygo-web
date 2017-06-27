#!/mnt/opt/privateer/usr/bin/php-cgi
<?php
$LIBSDIR='/mnt/opt/privateer/usr/libso';
$SAMYGOSO='/mnt/opt/privateer/usr/bin/samyGOso';
$BIN='/mnt/bin';

header("Content-Type: application/json; charset=UTF-8");

// Parse arguments
//var_dump($_SERVER);

parse_str($_SERVER["QUERY_STRING"], $params);

//read the local challenge
$challenge = trim(file_get_contents("/mnt/etc/samygo-web-api.challenge"));

if($params['challenge'] == $challenge){
	switch($params['action']){
		case 'CHANNELINFO':
			error_log("Processing CHANNELINFO");
			if(getLock()){
				$exec=`$SAMYGOSO -d -A -B -l "$LIBSDIR/libLogChannel.so" 2>/dev/null 1>&2`;
				sleep(1);
				releaseLock();
				
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
			 break;
		default:
			 echo json_encode( array('error' => true, 'message' => "Bad action ".$params['action']));
		
	}
}
else{
	#challenge doesn't match
	echo json_encode( array('error' => true, 'message' => 'Bad request (challenge)') );
}

//get a lock to do an injection
function getLock(){
	$count = 0;
	$available = false;
	while($count < 5){
		if(file_exists("/dtv/injection.lock")){
			#a lock is active. Wait until it finishes and is released
			sleep(1);
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
