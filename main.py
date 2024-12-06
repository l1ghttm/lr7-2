import json

def find_qualification(qualification_number):
    # Открываем файл и загружаем данные
    with open('dump.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    found_specialty = None
    found_qualification = None

    for item in data:
        if item.get('model') == 'data.skill':
            code = item['fields']['code']
            if code == qualification_number:
                found_qualification = item
            elif qualification_number.startswith(code) and len(code.split('-')) == 3:
                found_specialty = item


    if found_specialty or found_qualification:
        print("=============== Найдено ===============")
        if found_specialty:
            print(f"{found_specialty['fields']['code']} >> Специальность \"{found_specialty['fields']['title']}\", ПТО")
        if found_qualification:
            print(f"{found_qualification['fields']['code']} >> Квалификация \"{found_qualification['fields']['title']}\"")
    else:
        print("=============== Не найдено ===============")

if __name__ == "__main__":
    qualification_number = input("Введите номер квалификации: ")
    find_qualification(qualification_number)
