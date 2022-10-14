import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> a= new ArrayList<>();
        int n=2 ;
        for (int i=1;i<=n/2;i++) {
            if (n % i == 0) {
//                System.out.print(i + " ");
                a.add(i);
            }
        }
//        System.out.print(n);
        a.add(n);
        System.out.println(a);
        int even =0;
        int odd=0;
        for(int i : a){
            if(i%2==0){
                ++even;
            }
            else{
                ++odd;
            }
        }
        if(even>odd){
            System.out.println("EVEN>ODD");
        } else if (odd>even) {
            System.out.println("ODD>EVEN");
        }
        else{
            System.out.println("EVEN=ODD");
        }
    }
}
