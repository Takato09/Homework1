names = ('Alex', 'Carl', 'Hannah')
names_list = []


class Student:
    def __init__(self, names_tuple):
        self.names_tuple = names_tuple

    @property
    def list_by(self):
        for name in self.names_tuple:
            names_list.append(name)

        return names_list


student_list = Student(names)

print(student_list.list_by)

