import gc
import inspect


class Name(object):
    def __init__(self):
        self.first_name = "John"
        self.second_name = "Abrams"
        self.rty = (1, 2)
        super(Name, self).__init__()


class Person(object):
    def __init__(self):
        self.married = True
        self.mail = None
        self.logic = False
        self.height = 180
        self.qwe = {1, 2, 3}
        self.name = Name()
        super(Person, self).__init__()


def to_json(obj):
    if not isinstance(obj, (set, tuple, dict, list,)):
        attributes_dictionary = obj.__dict__
        attributes_list = list(attributes_dictionary)
        json_string = "{"
        for item in attributes_dictionary:
            if not inspect.ismethod(item):
                json_string += " \""
                json_string += str(item)
                json_string += "\": "
                attribute = getattr(obj, item)
                if isinstance(attribute, (set, tuple, dict, list,)):
                    json_string += "["
                    json_string += get_values(attribute)
                    if item != attributes_list[attributes_list.__len__() - 1]:
                        json_string += "],"
                    else:
                        json_string += "]}"
                elif isinstance(attribute, str):
                    json_string += "\""
                    if item != attributes_list[attributes_list.__len__() - 1]:
                        json_string += str(attribute)
                        json_string += "\","
                    else:
                        json_string += str(attribute)
                        json_string += "\"}"
                else:
                    json_string += str(attribute)
                    json_string += ","
        json_string = json_string.replace("True", "true")
        json_string = json_string.replace("False", "false")
        json_string = json_string.replace("None", "null")
        if json_string.find("<") > -1:
            object_address = json_string[
                             json_string.find("at", json_string.find("<")) + 3:
                             json_string.find(">")]
            json_string = json_string[:json_string.find("<")]
            obj_id = int(object_address, 16)
            obj = objects_by_id(obj_id)
            json_string += to_json(obj)
            json_string += "}"
    else:
        json_string = "["
        for object in obj:
            json_string += to_json(object)
            if object is not obj[obj.__len__() - 1]:
                json_string += ","
        json_string += "\n]"
    return json_string


def get_values(obj):
    obj = list(obj)
    values = ""
    for item in obj:
        values += str(item)
        values += ", "
    values = values[:values.__len__() - 2]
    return values


def objects_by_id(id_):
    for obj in gc.get_objects():
        if id(obj) == id_:
            return obj


def main():
    person = Person()
    people = [Person() for i in range(2)]
    print("Standard object dict: ", person.__dict__)
    print("Custom json string  :   ", to_json(person))


if __name__ == "__main__":
    main()
