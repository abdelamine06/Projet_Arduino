const int TEMPO=1000;

//Ultrason 
const int butonOut = 8;
const int butonIn = 9;
int distance; // en cm
long temps;

int stop = 0;

void setup(){

  Serial.begin(9600);
  //Ultrason
  pinMode(butonOut, OUTPUT); 
  pinMode(butonIn, INPUT);
  
  randomSeed(analogRead(1));
  for(int i=2;i<=7;i++){
    pinMode(i,OUTPUT);
  } 
}
void loop()
{
    
  digitalWrite(butonOut, LOW);
  delayMicroseconds(3);
  digitalWrite(butonOut, HIGH);
  delayMicroseconds(10);
  digitalWrite(butonOut, LOW);
  temps = pulseIn(butonIn, HIGH);
  distance= temps*0.034/2;

  
    //Serial.print("Distance : ");
    //Serial.println(distance);
    
  // tester si la distance est inférieure à 5cm pour lancer le jeux
  if(distance<5 && stop == 0){
    stop = 1;
    afficheDe(random(1,7));
   }

  delay(500);
  temps=0;
  distance=0;
  delay(500);
  
   
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
