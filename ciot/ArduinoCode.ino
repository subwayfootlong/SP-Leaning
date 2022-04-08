#include <ESP8266WiFi.h>
#include <PubSubClient.h>
const char* ssid = "Lais 12 (2)"; // Enter your WiFi name
const char* password =  "deeznuts"; // Enter WiFi password
const char* mqttServer = "172.20.10.7";
const int mqttPort = 1883;
const char* mqttUser = "admin";
const char* mqttPassword = "admin";
int BUTTONstate = 0;
int ledyellow =D6;
int ledred =D4;
int buzzer=D7;


String msg[10];
WiFiClient espClient;
PubSubClient client(espClient);
void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
      Serial.println("connected");  
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
    }
  }
  client.publish("esp/test", "hello"); //Topic name
  client.subscribe("esp/test");
  pinMode(D8, INPUT);//button
  pinMode(D2, INPUT);//pir
  pinMode(ledyellow, OUTPUT);//ledyellow
  pinMode(ledred, OUTPUT);//ledred
  pinMode(buzzer, OUTPUT);//buzzer
  
}
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    msg[i]=payload[i];
  }
  Serial.println();
  Serial.println("-----------------------");
}
void loop() {
  client.loop();
  //Serial.print(msg[0]);
  BUTTONstate = digitalRead(D8);
  if(digitalRead(D2)== HIGH){
    digitalWrite(ledred, LOW);
    digitalWrite(buzzer, LOW);
    client.publish("Reject Tray","Empty");
    }
    else if (digitalRead(D2)==LOW){
    digitalWrite(buzzer, HIGH);
    digitalWrite(ledred, HIGH);
    Serial.println("Reject tray is full");
    client.publish("Reject Tray","Full");
    }
  if(BUTTONstate ==HIGH) {
    digitalWrite(ledyellow, HIGH);
    client.publish("button","1");
  } else {
    digitalWrite(ledyellow, LOW);
    client.publish("button","0");
  }
  delay(1000); 
}
