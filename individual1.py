def sum_between_negatives(*args):
    # Если список аргументов пуст, возвращаем None
    if not args:
        return None
    
    # Ищем индексы первого и последнего отрицательных аргументов
    first_negative_index = None
    last_negative_index = None
    for i, arg in enumerate(args):
        if arg < 0:
            if first_negative_index is None:
                first_negative_index = i
            last_negative_index = i
    
    # Если нет отрицательных аргументов, возвращаем None
    if first_negative_index is None:
        return None
    
    # Вычисляем сумму аргументов между первым и последним отрицательными
    result_sum = sum(args[first_negative_index + 1:last_negative_index])
    return result_sum

# Пример использования:
arguments = [1, -2, 3, 4, -5, 6, 7, -8]
result = sum_between_negatives(*arguments)
print(result)
