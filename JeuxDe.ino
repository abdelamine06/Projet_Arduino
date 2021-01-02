const int ECART=0;
const int TEMPO=2000;
void setup(){
  randomSeed(analogRead(1));
  for(int i=2;i<=9;i++){
    pinMode(i,OUTPUT);
  } 
}
void loop(){
  int luminosite1=analogRead(0);
  int luminosite2=analogRead(0);  

  // tester si un capteur est passer pour lancer le jeux
  if(luminosite2-luminosite1==ECART){
    afficheDe(random(1,8));
    delay(TEMPO);
    eteintDe();
   }
}
void afficheDe(int nombre){

  if(nombre==1){
    digitalWrite(5,HIGH);
  }
  
  if(nombre==2){
    digitalWrite(2,HIGH);
    digitalWrite(8,HIGH);
  }

  if(nombre==3){
    digitalWrite(2,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(8,HIGH);
  }

  if(nombre==4){
    digitalWrite(2,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(8,HIGH);
  }
  if(nombre==5){
    digitalWrite(2,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(8,HIGH);
    digitalWrite(5,HIGH);
  }

  if(nombre==6){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
  }
   if(nombre==7){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(6,HIGH);
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
  }
}

void eteintDe(){
  for(int i=2;i<=8;i++){
    digitalWrite(i,LOW);
  }
}