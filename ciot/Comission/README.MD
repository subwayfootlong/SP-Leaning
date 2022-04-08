# Commision
Was commisioned to do someones final project for this module.

This was all done on node-red with a Raspberry Pi

## Data Flow
### Storage
Sensor > Raspberry Pi GPIO Node > SQLite 
### AI
Client Laptop running python AI detection > Client MQTT  publish > Raspberry Pi MQTT Subscribe > Node-RED Dashboard
