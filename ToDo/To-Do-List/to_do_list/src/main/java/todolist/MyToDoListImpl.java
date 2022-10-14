package todolist;

import java.util.List;
import java.util.Scanner;

public class MyToDoListImpl implements MyToDoList {
    Scanner scn;

    MyToDoListImpl() {
        scn = new Scanner(System.in);
    }


    @Override
    public void create(List<String> list) {
        System.out.print("\nEnter date of to-do in the format \"day-month-year\" : ");
        String date = scn.nextLine();
        System.out.print("\nEnter what you want complete : ");
        String to_do = scn.nextLine();
        list.add(date + " :- " + to_do);
    }

    @Override
    public void read(List<String> list) {
        if (list.isEmpty()) {
            System.out.println("\nYour to-do list is empty!");
        } else {
            System.out.println("\nYour to-do list is : \n");
            for (int i = 0; i < list.size(); i++) {
                System.out.println(i + 1 + ") " + list.get(i));
            }
        }
    }

    @Override
    public void update(List<String> list) {
        if (list.isEmpty()) {
            System.out.print("");
        } else {
            int choice = 10;
            String newDate, new_task;
            System.out.print("\nEnter serial number of the to-do you want to update : ");
            int update = scn.nextInt();
            if (update <= list.size()) {
                String str = list.get(update - 1);
                String[] split = str.split(" ", 3);
                String date_sub = split[0];
                String task_sub = split[2];
                System.out.println("\nWhat do you want to update? : \n");
                while (choice != 0) {
                    System.out.print("1 - Date only\n2 - Task only\n\nEnter choice : ");
                    choice = scn.nextInt();
                    switch (choice) {
                        case 1:
                            scn.nextLine();
                            System.out.print("Enter the new date : ");
                            newDate = scn.nextLine();
                            list.set(update - 1, newDate + " :- " + task_sub);
                            return;
                        case 2:
                            scn.nextLine();
                            System.out.print("Enter the new task : ");
                            new_task = scn.nextLine();
                            list.set(update - 1, date_sub + " :- " + new_task);
                            return;
                        default:
                            System.out.println("Invalid choice, enter again : ");
                    }
                }
            }
            else {
                System.out.println("\nInvalid choice\n");
            }
        }
    }

    @Override
    public void delete(List<String> list) {
        if (list.isEmpty()) {
            System.out.print("");
        } else {
            System.out.print("\nEnter serial number of the to-do you want to delete : ");
            int update = scn.nextInt();
            if (update <= list.size()) {
                list.remove(update - 1);
            }
            else {
                System.out.println("\nInvalid choice\n");
            }
        }
    }

    @Override
    public void markComplete(List<String> list) {
        if (list.isEmpty()) {
            System.out.print("");
        } else {
            System.out.print("\nEnter serial number of the to-do you want to mark as complete : ");
            int update = scn.nextInt();
            if (update <= list.size()) {
                String str = list.get(update - 1);
                list.set(update - 1, str + " (Completed)");
            }
            else {
                System.out.println("\nInvalid choice\n");
            }
        }
    }
}
