package ToDoPackage;
import java.util.ArrayList;
import java.util.List;
public class ToDoSingleton {
    static ToDoSingleton object = new ToDoSingleton();
    private ToDoSingleton(){
    }
    public static ToDoSingleton getInstance(){
        return object;
    }
    List<String> list = new ArrayList<>();
    List<String> completed_list = new ArrayList<>();
}
