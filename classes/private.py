class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # __update是私有方法，外部禁止访问
    update_a = update


class MappingSubClass(Mapping):
    def update(self, keys, values):
        # update重载,__update,update_a没有重载
        for item in zip(keys, values):
            self.items_list.append(item)


mapping = Mapping({'name': 'lai'})
mapping.update_a({'lover': 'xiao'})
print(mapping.items_list)
mappingSub = MappingSubClass({'name': 'lai'})
print(mappingSub.items_list)
