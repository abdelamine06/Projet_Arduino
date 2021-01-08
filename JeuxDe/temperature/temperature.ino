#include <math.h>

const int TEMPO=300;

// Temperature
int val;
double temp;
 
int stop = 0;

void setup(){

  Serial.begin(9600);

  randomSeed(analogRead(1));
  for(int i=2;i<=7;i++){
    pinMode(i,OUTPUT);
  } 
}

double Thermistor(int v)
{
  double Temp;
  Temp = log (10000.0 * ((1024.0/v)-1));
  Temp = 1 / ( 0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp )) * Temp );
  Temp = Temp-273.15;
  Temp = ( Temp*9.0 )/5.0 + 32.0;
  return Temp;
  
}


void loop()
{
  
  val = analogRead(2);
  temp = Thermistor(val);
  
    //Serial.print("Temp : ");
    //Serial.println(temp);
    
  // si on touche le capteur
  if(temp > -40.57 && stop ==0){
    stop = 1;
    afficheDe(random(1,7));
   }
  
   
}
void afficheDe(int nombre){

  if(nombre==1){
    digitalWrite(2,HIGH);
  }
  
  if(nombre==2){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
  }

  if(nombre==3){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
  }

  if(nombre==4){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(5,HIGH);
  }
  if(nombre==5){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(6,HIGH);
  }

  if(nombre==6){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(7,HIGH);
  }

}
/*
void eteintDe(){
  
  for(int i=2;i<=7;i++){
    digitalWrite(i,LOW);
    
  }
  delay(TEMPO);
}*/
