char dataString[30] = {0};
char dataLuz[50] = {0};

const int LM35 = A0; // Define o pino que lera a saída do LM35
float Temperatura; // Variável que armazenará a temperatura medida
const int PinSensorAgua= 0;// Define pino que lera a saida do sensor de nivel de agua
int liquid_level=0; // variável nivel de agua

int sensorFotoPatio=A2;
int sensorFotoSala=A3;
int sensorFotoDormitorio=A4;
int sensorFotoGarage=A5; // estado da porta garagem

//digitais
int carPin=3;
int sw_open_door=4;
int sw_close_door=5;


int sw_open = 0;
int sw_close = 0;
int car_aval = 0;
int LDR_garage = 0;
int LDR_patio = 0;
int LDR_sala = 0;
int LDR_dormitorio = 0;
int label_door=0;
String msg ="";
String open_door ="0";



void setup() {
Serial.begin(9600);              //Starting serial communication
pinMode(carPin, INPUT);
pinMode(sw_open_door, INPUT);
pinMode(sw_close_door, INPUT);
pinMode(PinSensorAgua, INPUT);//the liquid level sensor will be an input to the arduino
}
  
void loop() {
 // Programação da porta----------------------
 sw_open = digitalRead(sw_open_door);
 sw_close = digitalRead(sw_close_door);

  if (sw_open == 1){
    label_door=0;
    }
   else if (sw_close == 1) {
    label_door=1;
    }
   else {
    label_door=0;
    } 
 // Sinal do carro
 car_aval = digitalRead(carPin);
 
 // Sinal garagem
 LDR_garage = analogRead(sensorFotoGarage);
 
 // Temperatura
 Temperatura = (float(analogRead(LM35))*5/(1023))/0.01; 
 
 // Sensores de luz patio, sala, dormitorio
 LDR_patio = analogRead(sensorFotoPatio);
 LDR_sala = analogRead(sensorFotoSala);
 LDR_dormitorio = analogRead(sensorFotoDormitorio);
 // Sensor nível de agua
 liquid_level= analogRead(PinSensorAgua); //arduino reads the value from the liquid level sensor
   
 msg="{'temperature':"+ String(Temperatura) + ", 'luz_sala':" + String(LDR_sala) + ", 'luz_patio':" + String(LDR_patio) + ", 'car_ava':" + String(car_aval)+ ", 'luz_dormitorio':" + String(LDR_dormitorio)+ ", 'label_door':" + String(label_door)+ ", 'label_garage':" + String(LDR_garage)+ ", 'liquid_level':" + String(liquid_level)+ "}";
 Serial.println(msg);   // send the data,   

 delay(1000);                  // give the loop some break
}
