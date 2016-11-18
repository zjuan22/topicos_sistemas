
// this version work with door ok 17nov
char dataString[30] = {0};
char dataLuz[50] = {0};

int a =0; 
int b =0; 
int sensorPin = 0; //A0 ?
int sensorPinFoto=1; //A1 fotoresitor
int LDR = 0;



// interface motor
int motor_1 = 6; // pin D6  
int motor_2 = 7; // pin D7
// switch puerta
int sw_left = 4; // pin D4  
int sw_right = 5; // pin D5

int sw_boton = 8; // pin D8

String switch_d;
int swl;
int swr;
int swb;
int sw;

void setup() {
  Serial.begin(9600);              //Starting serial communication
  pinMode(motor_1, OUTPUT);
  pinMode(motor_2, OUTPUT);
  pinMode(sw_left, INPUT);
  pinMode(sw_right, INPUT);
  pinMode(sw_boton, INPUT);
  pinMode(A1, INPUT);
  pinMode(A3, INPUT);
  pinMode(A2, INPUT);

}

  
void loop() {
  //Serial.print("Valor: ");
  
  //swl=digitalRead(A2);
  //swr=digitalRead(A3);
  
  swl=digitalRead(sw_left);
  swr=digitalRead(sw_right);
  //swb=digitalRead(sw_boton);
  swb=digitalRead(A1);
  delay(50);
  switch_d = String(swb) + String(swl) + String(swr);
  sw = switch_d.toInt();
  switch(sw){
        case 0:
            
            digitalWrite(motor_2,LOW);
            digitalWrite(motor_1,LOW);
            delay(50);  
            digitalWrite(motor_1,HIGH);
            Serial.println("derec1a..abierto");
            break;
        case 001:
            digitalWrite(motor_1,LOW);
            digitalWrite(motor_2,LOW);
            delay(50);  
            Serial.println("quieto_abierto");  
            break;
        case 10:
            digitalWrite(motor_2,LOW);
            digitalWrite(motor_1,LOW);
            delay(50);  
            digitalWrite(motor_1,HIGH);
            Serial.println("abriendo");
            break;
        case 100:
            digitalWrite(motor_2,LOW);
            digitalWrite(motor_1,LOW);
            delay(50);  
            digitalWrite(motor_2,HIGH);
            Serial.println("abriendo");
            break;
        case 101:
            digitalWrite(motor_2,LOW);
            digitalWrite(motor_1,LOW);
            delay(50);   
            digitalWrite(motor_2,HIGH);
            Serial.println("abriendo");
            break;
        case 110:
            delay(50);    
            digitalWrite(motor_1,LOW);
            digitalWrite(motor_2,LOW);
            Serial.println("quieto_cerrado");

            break;
            
         default:
            delay(50);    
            digitalWrite(motor_1,LOW);
            digitalWrite(motor_2,LOW);
            Serial.println("default");        
            break;
         }  
  
  Serial.println("res= "+ String(sw));
  
  LDR = analogRead(sensorPinFoto);
  


   if (LDR > 280){
    b=1;
    }
   else {
     b=0;}
  Serial.println(LDR);   // send the data  
  //Serial.println(b);   // send the data
  
  int reading = analogRead(sensorPin); 
  float voltage = reading * 5.0;
  voltage /= 1024.0;
  float temperatureC = (voltage - 0.5) * 100 ; 
  a=temperatureC;                          // a value increase every loop
/* a = prob1;
 b =  prob2;*/
  //sprintf(dataString,"%02X",a); // convert a value to hexa 
  //sprintf(dataLuz,"%02X",b); // convert a value to hexa */
  //Serial.println(dataLuz);   // send the data
  //Serial.println(dataString);   // send the data
  delay(1000);                  // give the loop some break

}
