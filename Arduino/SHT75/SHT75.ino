#include <Sensirion.h>

const uint8_t dataPin  =  2;
const uint8_t clockPin =  3;

float temperature;
float humidity;
float dewpoint;

Sensirion tempSensor = Sensirion(A5, A2);

void setup()
{
  Serial.begin(9600);

  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);

  digitalWrite(A3, HIGH);
  digitalWrite(A4, LOW);
}

void loop()
{
  tempSensor.measure(&temperature, &humidity, &dewpoint);


  Serial.print(temperature);
  Serial.print(" ");
  Serial.print(humidity);
  Serial.print(" ");
  Serial.print(dewpoint);
  Serial.print(" ");
  Serial.println();
  delay(300);  
}
