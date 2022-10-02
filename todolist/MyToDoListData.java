package todolist;

import java.util.ArrayList;
import java.util.List;

public class MyToDoListData {
    static MyToDoListData obj = new MyToDoListData();

    private MyToDoListData() {
    }

    public static MyToDoListData getInstance() {
        return obj;
    }

    List<String> to_do = new ArrayList<>();
}
