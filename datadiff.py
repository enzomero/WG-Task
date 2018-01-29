# -*- coding: utf-8 -*-
import copy

'''
Имеется предустановленный набор данных в виде вложенных словарей. Пример:
data = {
    'a' : {
        'a1' : 1,
        'a2' : 2,
    },
    'b' : {
        'b1' : {
            'b11' : 1,
            'b12' : 2,
            },
    }
}
Вложенность словарей может быть произвольной. Требуется предложить программное решение на языке
Python для получения разницы между начальным и конечным состояниями данных. Пример:
data['a']['a1'] = 3
data['b']['b1']['b11'] = 5
Результат представляет из себя компиляцию изменений:
res = {
'a' : {'a1' : 3},
'b' : {'b1' : {'b11' : 5}}
}
Программа должна быть покрыта юнит-тестами.
'''

# Alghoritm which finds and drops identical branches from struct.
# p_data        - struct of data which we set as the base
# p_dataEdited  - struct of data which was changed
def find(p_data, p_dataEdited):
    for i in p_data:
        if (p_data[i] != p_dataEdited[i]):
            if (type(p_data[i]) != type(10)) :
                find(p_data[i], p_dataEdited[i])
        else:
            p_dataEdited.pop(i)
    return p_dataEdited;

def getChanges(p_data, p_dataEdited):
    try:
        return find(p_data, p_dataEdited)
    except KeyError as err:
        return 'Can\'t find the key'


