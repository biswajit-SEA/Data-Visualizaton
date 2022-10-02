/**
 * This is a simple Interface-based To-Do-List Application
 * It implements Java libraries and OOP concepts
 * Allows the user to perform CRUD operations on the to-do-list
 *
 * @author :- Biswajit Panda
 * @version :- 1.0.0
 */


package todolist;

import java.util.List;

public interface MyToDoList {
    void create(List<String> list);

    void read(List<String> list);

    void update(List<String> list);

    void delete(List<String> list);

    void markComplete(List<String> list);
}


/*
learn about factory pattern
builder pattern
thread-safe singleton pattern
 */
