/**
 * This is a simple To-Do List Application program written in java
 * The Application allows user to perform CRUD {Create, Read, Update, Delete} operations
 *
 * @author Gulshan Kumar Nayak
 * @version 1.0
 */
package ToDoPackage;    //smallcase
import java.util.List;
public interface ToDoInterface {
    void showList(List<String> list, int number);
    void addItem(List<String> list);
    void delete(List<String> list);
    void markAsComplete(List<String> list, List<String> completed_list);
    void update(List<String> list);
}
