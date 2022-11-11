// A0, etc just store actual pin numbers, so 'int' works
int lightSensorPin = A0;
int tempSensorPin = A1;

void setup() {
  // don't actually need to set analog pinmode
  Serial.begin(9600);
}

void loop() {
  // need a pause between analog pin reads
  // apparently the easiest way is to "double read"
    // to let ADC settle -- tosses first read

  // get light value first -- arbitrary units
  int light = analogRead(lightSensorPin);
  light = analogRead(lightSensorPin);

  // get temp and convert to C and F
  int raw_temp = analogRead(tempSensorPin);
  float temp_calc = raw_temp * 5.0;
  temp_calc /= 1024.0;
  float tempC = (temp_calc - 0.5) * 100 ;
  float tempF = (tempC * 9.0 / 5.0) + 32.0;

  // print data
  Serial.print(light);
  Serial.print(",");
  Serial.print(tempC);
  Serial.print(",");
  Serial.print(tempF);
  Serial.println();

  // collect data every 5 minutes
  delay(300000);
}
