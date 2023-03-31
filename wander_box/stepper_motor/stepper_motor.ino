const int buttonPin = 7;

void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  digitalWrite(2, LOW);  

  // Button Code
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("Hello!");
}

void loop() {
   

  // Button Code
  if (digitalRead(buttonPin) == LOW) {

    Serial.println("DOWN");
    for(int i=0; i<=32500; i++){
      digitalWrite(2, LOW);
      digitalWrite(3, HIGH);
      delayMicroseconds(60); 
      digitalWrite(3, LOW);   
    }

    delay(1000);
    
    Serial.println("UP"); 
    for(int i=0; i<=32500; i++){
     digitalWrite(2, HIGH); 
     digitalWrite(3, HIGH);
     delayMicroseconds(60);
     digitalWrite(3, LOW);
    }
    
    Serial.println("FINISHED");
  }
}
