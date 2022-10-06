#include<Servo.h> //Inlcuding the servo library to operate servo motor

Servo servo;//naming the servo to use it in the pogram

//Motor 1
int mpin1=A1;
int mpin2=A2;

//Motor 2
int mpin3=A3;
int mpin4=A4;

int trig=6;
int echo=7;
int duration = 0;
int distance = 0;
int sp = 255;//assigns the speed of the motors

//function to drive the robot straight
void straight()
{
    analogWrite(mpin1,sp);
    analogWrite(mpin2,0);
    analogWrite(mpin3,sp);
    analogWrite(mpin4,0);
}

//function to drive the robot backward
void back()
{
  for(int i=1;i<=5;i++)
  {
    analogWrite(mpin1,0);
    analogWrite(mpin2,sp);
    analogWrite(mpin3,0);
    analogWrite(mpin4,sp);
  }
}
    

int look_right()
{
    servo.write(0); 
    delay(500);
    int distance = dist();
    delay(100);
    servo.write(90); 
    return distance;
    delay(100);
}

int look_left()
{
    servo.write(180); 
    delay(500);
    int distance = dist();
    delay(100);
    servo.write(90); 
    return distance;
    delay(100);
}

//function to turn the robot left
void turn_left()
{
    analogWrite(mpin1,sp);
    analogWrite(mpin2,0);
    analogWrite(mpin3,0);
    analogWrite(mpin4,sp);
    delay(500);
    analogWrite(mpin1,sp);
    analogWrite(mpin2,0);
    analogWrite(mpin3,sp);
    analogWrite(mpin4,0);
}

//function to turn the robot right
void turn_right()
{
    analogWrite(mpin1,0);
    analogWrite(mpin2,sp);
    analogWrite(mpin3,sp);
    analogWrite(mpin4,0);
    delay(500);
    analogWrite(mpin1,sp);
    analogWrite(mpin2,0);
    analogWrite(mpin3,sp);
    analogWrite(mpin4,0);
}

int dist()
{
  digitalWrite(trig , HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig , LOW);


  duration = pulseIn(echo , HIGH);//calculates time taken for the ultrasonic wave to received by the sensor form the obstacle
  
  distance = (duration/2) / 28.5 ;//calculates the distance between the obstacle and the sensor

  return distance;
}

//function to halt the robot 
void halt()
{
  analogWrite(mpin1,0);
  analogWrite(mpin2,0);
  analogWrite(mpin3,0);
  analogWrite(mpin4,0);
}

void setup() 
{
  servo.attach(8);//Assigning a pin number to the Servo to which it is to be connected
  servo.write(90);//set the servo intially to 90 degrees.
  delay(2000);

  //Setting up the motors pins, trigger pin as output and echo pin as input
  pinMode(mpin1,OUTPUT);
  pinMode(mpin2,OUTPUT);
  pinMode(mpin3,OUTPUT);
  pinMode(mpin4,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);

  Serial.begin(9600);
}

void loop() 
{ 
  int dist_r=0;
  int dist_l=0;
  delay(50);
  Serial.println(dist());//prints the distance between ultrasonic sensor and the obstacle on the serial monitor

  if(distance<=20)
  {
    halt();
    delay(300);
    back();
    delay(300);
    halt();
    delay(300);
    dist_r=look_right();
    delay(400);
    dist_l=look_left();
    delay(50);

    if(dist_r>=dist_l)
    {
      turn_right();
      halt();
    }
    else if(dist_l>=dist_r)
    {
      turn_left();
      halt();
    }
    else
    {
      back();
    }
  }
  else
  {
    straight();
  }
  distance=dist();
}
