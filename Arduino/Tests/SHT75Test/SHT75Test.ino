/*
 * Query a SHT10 temperature and humidity sensor
 *
 * A simple example that queries the sensor every 5 seconds
 * and communicates the result over a serial connection.
 * Error handling is omitted in this example.
 */

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

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" C, Humidity: ");
  Serial.print(humidity);
  Serial.print(" %, Dewpoint: ");
  Serial.print(dewpoint);
  Serial.println(" C");
  
  delay(1000);  
}
