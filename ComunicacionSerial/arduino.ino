int led= 2; 
char dato;
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) 
  {
    dato = Serial.read();
    if (dato == '1') 
    {
      Serial.println("LED encendido");
      digitalWrite(2, HIGH);
    
    }
    if (dato == '0') 
    {
      Serial.println("LED apagado");
      digitalWrite(2, LOW);
     
    } 
    
  }
