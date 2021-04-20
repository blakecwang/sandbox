#!/usr/bin/env python

class ColumnList(list):

    def insert_after(self, new_columns, after_column):
        insert_index = self.index(after_column) + 1
        if isinstance(new_columns, list):
            tail = self[insert_index:]
            del self[insert_index:]
            self.extend(new_columns)
            self.extend(tail)
        else:
            self.insert(insert_index, new_columns)

list1 = ["a", "b", "c"]
col_list1 = ColumnList(list1)
print(col_list1)
col_list1.insert_after("z", "b")
print(col_list1)
col_list1.insert_after(["y", "y", "y"], "a")
print(col_list1)
