package todolist;

import java.util.*;

public class MyToDoListChoices {
    public static void main(String[] args) {

        int choice = 10;

        MyToDoListData data = MyToDoListData.getInstance();

        MyToDoList obj = new MyToDoListImpl();
        Scanner scn = new Scanner(System.in);

        System.out.print("Welcome to your to-do list\n\n" +
                "What would you like to do?\n\n" +
                "Available choices : \n");

        while (choice != 6) {
            System.out.print("\n1 - Create a new to-do \n" +
                    "2 - Read your to-do list \n" +
                    "3 - Update your to-do list\n" +
                    "4 - Delete your to-do list\n" +
                    "5 - Mark an item as complete\n" +
                    "6 - Exit!\n\n" +
                    "Enter choice : ");
            choice = scn.nextInt();
            switch (choice) {
                case 1:
                    obj.create(data.to_do);
                    break;
                case 2:
                    obj.read(data.to_do);
                    break;
                case 3:
                    obj.read(data.to_do);
                    obj.update(data.to_do);
                    break;
                case 4:
                    obj.read(data.to_do);
                    obj.delete(data.to_do);
                    break;
                case 5:
                    obj.read(data.to_do);
                    obj.markComplete(data.to_do);
                    break;
                case 6:
                    break;
                default:
                    System.out.println("\nInvalid Choice, enter again.\n");
            }
        }
        System.out.println("\nThank you for using the to-do");

    }
}
