const int ECART=100;
const int TEMPO=2000;
int tour;
void setup(){
  Serial.begin(9600);
  randomSeed(analogRead(1));
  for(int i=2;i<=8;i++){
    pinMode(i,OUTPUT);    
  } 

  eteintDe();

  tour = 0;
}
void loop(){

  delay(100);

  if(tour == 0){

    Serial.print(2);
  
    // afficheDe(random(1,7));
    afficheDe(2);
    tour = 1;
  }
  
}

void afficheDe(int nombre){

  if(nombre==1){
    digitalWrite(5,LOW);
  }
  
  if(nombre==2){
    digitalWrite(3,LOW);
    digitalWrite(5,LOW);
  }

  if(nombre==3){
    digitalWrite(2,LOW);
    digitalWrite(5,LOW);
    digitalWrite(7,LOW);
  }

  if(nombre==4){
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(7,LOW);
  }
  if(nombre==5){
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(7,LOW);
    digitalWrite(5,LOW);
  }

  if(nombre==6){
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
    digitalWrite(7,LOW);
    digitalWrite(5,LOW);
  }
}
void eteintDe(){
  for(int i=2;i<=8;i++){
    digitalWrite(i,HIGH);
  }
}
