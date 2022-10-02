

//Motor 1
int mpin1=A1;
int mpin2=A2;

//Motor 2
int mpin3=A3;
int mpin4=A4;
int sp = 255;//assigns the speed of the motors




void setup() 
{

  //Setting up the motors pins, trigger pin as output and echo pin as input
  pinMode(mpin1,OUTPUT);
  pinMode(mpin2,OUTPUT);
  pinMode(mpin3,OUTPUT);
  pinMode(mpin4,OUTPUT);
}

void loop() 
{ 
  analogWrite(mpin1,sp);
  analogWrite(mpin2,0);
  analogWrite(mpin3,sp);
  analogWrite(mpin4,0);
}
