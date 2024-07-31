int ledPin = 13;
int incomingNumber = 0;
int outgoingNumber = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingNumber = Serial.parseInt();
    for (int i = 0; i < incomingNumber; i++) {
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
      delay(1000);
    }
    outgoingNumber = random(1, 10);
    Serial.println(outgoingNumber);
  }
}
