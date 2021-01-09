const int ECART=20;
const int TEMPO=2000;
int stop = 0;
void setup(){
  randomSeed(analogRead(1));
  for(int i=2;i<=7;i++){
    pinMode(i,OUTPUT);
  } 
}
void loop(){
  int luminosite1=analogRead(0);
  delay(100);
  int luminosite2=analogRead(0);  

  // tester si un capteur est passer pour lancer le jeux
  if((luminosite2-luminosite1==ECART) && stop ==0)
  {
    stop=1;
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
    digitalWrite(5,HIGH);
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
}*/
