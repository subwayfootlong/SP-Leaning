# CIOT
This is a module I took in SP to create a CIOT project.

## Brief
  1. Camera is used to detect white and silver cubes; Ai is then used to classify between white and silver. 
  2. If the A.I (Artificial Intelligence) detects white cube, a motor will push the white cube into the reject tray.  
  3. The reject tray contains an Infared sensor that count the number of white cubes.  
  4. When there are too many white cubes, LED Red and Buzzer will turn on. It will also send a notification via Telegram. 
  5. A technician will then come by to remove the white cubes. He will also turn on a switch to show that the machine is being serviced. The servicing status will be sent via telegram. 
  6. The machine uptime/downtime and reject frequency will all be available via dashboard for anyone on the network. 
  
  ![image](https://user-images.githubusercontent.com/74981128/162348480-b1f164f2-31c0-4aac-8934-a3ac6f52529e.png)
  
## Explanation
This project was mainly done on a laptop acting as a server with the python script and backend running. We chose to use the Node-MCU v3 as our I/O as it had the number of I/O s we needed and most importantly was capable of WiFi as it had a built in ESP8266

## Technologies used 
Node-RED, InfluxDB, Arduino, MQTT, Telgram, TensorFlow 

## Remarks
The model was not included as it was too large

For a full project description, read the report provided
