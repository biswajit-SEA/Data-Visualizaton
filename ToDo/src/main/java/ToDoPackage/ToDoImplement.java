package ToDoPackage;

import java.util.List;
import java.util.Scanner;

import java.time.LocalDate;
import java.time.LocalTime;

public class ToDoImplement implements ToDoInterface{
    Scanner scn = new Scanner(System.in);

    @Override
    public void addItem(List<String> list) {
        LocalDate myObj = LocalDate.now(); // Create a date object
        LocalTime myObj1 = LocalTime.now();
        System.out.print("Enter date in the format \"day-month-year\" : ");
        String date = scn.nextLine();
        System.out.print("Enter your task : ");
        String task = scn.nextLine();
        String temp;
        temp = "Creation Date:- " + myObj + "\nCreation Time:- " + myObj1;
        list.add(temp + "\n" + "Task:- " +task + "\nDeadline:- " + date);
    }

    @Override
    public void showList(List<String> list, int number) {
        System.out.println("---------------------------------------------------");
        switch (number){
            case 1 -> System.out.println("[ To-Do List ]\n");
            case 6 -> System.out.println("[ Completed List ]\n");
        }

        if(list.isEmpty()){
            System.out.println("The List is Empty !!!");
        }
        else {
            for(int i=0;i<list.size();i++){
                System.out.println(i+1 + ") "+list.get(i));
                System.out.println();
            }
        }
        System.out.println("---------------------------------------------------");
    }

    @Override
    public void delete(List<String> list) {
        if(list.isEmpty()){
            System.out.println("The list is Empty !!!");
        }
        else{
            System.out.println("Enter the index number you want to delete: ");
            int index=scn.nextInt();
            if(index > list.size()){
                System.out.println("WARNING!!! ->Index out of range !!!");
            }
            else {
                list.remove(index-1);
            }
        }
    }

    @Override
    public void markAsComplete(List<String> list, List<String> completed_list) {
        if(list.isEmpty()){
            System.out.println("List is Empty !!!");
        }
        else{
            System.out.println("Enter the index you wish to mark as complete?");
            int index= scn.nextInt();
            int list_size= list.size();
            if(index > list_size){
                System.out.println("WARNING!!! ->Index out of range !!!");
            }
            else {
                String second = list.get(index-1);
                System.out.println("Enter Finish Date: ");
                scn.nextLine();
                String date = scn.nextLine();
                System.out.println("** Task moved to Completed To-Do List **");
                completed_list.add(completed_list.size(), second + "\nTask completed on: " + date);
                list.remove(index-1);
            }
        }
    }

    @Override
    public void update(List<String> list) {
        int index, choice;
        String newDate, newTask, temp, concat;
        if(list.isEmpty()){
            System.out.println("The list is Empty !!!");
        }
        else{
            System.out.println("Enter the index where you want to update: ");
            index = scn.nextInt();
            if(index > list.size()){
                System.out.println("WARNING!!! ->Index out of range !!!");
            }
            else{
                temp = list.get(index-1);
                String[] upd = temp.split("\n");
                System.out.println("1.Update Date\n2.Update Task");
                choice = scn.nextInt();

                switch(choice){
                    case 1 -> {
                        scn.nextLine();
                        System.out.println("Enter new date: ");
                        newDate = scn.nextLine();
                        concat = upd[0] + "\n" + upd[1] + "\n" + upd[2] + "\n" + "Deadline:- " + newDate;
                        list.set(index-1, concat);
                    }
                    case 2 -> {
                        scn.nextLine();
                        System.out.println("Enter new Task: ");
                        newTask = scn.nextLine();
                        concat = upd[0] + "\n" + upd[1] + "\n" + "Task:- " + newTask + "\n" + upd[3];
                        list.set(index-1, concat);
                    }
                    default -> System.out.println("WARNING!!! ->Enter valid choice");
                }
            }
        }
    }
}
