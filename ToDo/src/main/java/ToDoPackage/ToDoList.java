package ToDoPackage;
import java.util.Scanner;
public class ToDoList {
        public static void main(String[] args) {
//            List<String> list = new ArrayList<>();
//            List<String> completed_list = new ArrayList<>();
            ToDoSingleton singletonObject = ToDoSingleton.getInstance();
            ToDoInterface object = new ToDoImplement();
            int menuItem;
            while(true) {
                menuItem = menu();
                switch (menuItem) {
                    case 0 -> {
                            System.out.println("Thank you for using the application");
                            System.exit(0);
                    }
                    case 1 -> object.showList(singletonObject.list, 1);
                    case 2 -> object.addItem(singletonObject.list);
                    case 3 -> object.delete(singletonObject.list);
                    case 4 -> object.markAsComplete(singletonObject.list, singletonObject.completed_list);
                    case 5 -> object.update(singletonObject.list);
                    case 6 -> object.showList(singletonObject.completed_list, 6);
                    default -> System.out.println("Enter a valid option");
                }
            }
        }
        public static int menu() {

            int choice;

            Scanner input = new Scanner(System.in);
            System.out.println();
            System.out.println("Main Menu");
            System.out.println();
            System.out.println("0. Exit the program");
            System.out.println("1. Display to-do list");
            System.out.println("2. Add item to list");
            System.out.println("3. Remove item from list");
            System.out.println("4. Mark as complete");
            System.out.println("5. Update the List");
            System.out.println("6. View Completed ToDo list");
            System.out.println();
            System.out.print("Enter choice: ");
            choice = input.nextInt();

            return choice;
        }
}
