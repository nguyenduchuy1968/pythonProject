"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
"""
# def get_gmail(string:str) -> str|None:
#     domain = string.split('@').pop(-1).rstrip('\n')
#
#     if domain == "gmail.com":
#         arr_from_str = string.split('\t')
#         arr_from_str.pop(0)
#         email = ''.join(arr_from_str)
#         return email
#     return None
#
# try:
#     with open('emails.txt', 'r') as file:
#         with open('output.txt', 'w') as output:
#             for line in file:
#                 if get_gmail(line):
#                     output.write(get_gmail(line))
# except Exception as err:
#     print(err)

###############################################
"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""


import json
from typing import TypedDict

Note = TypedDict('Note', {'id': int, 'name': str, 'price': int})


class PurchaseNote:
    notes_all_purchases: list[Note] = []
    notes_file = 'notes.txt'

    @staticmethod
    def add_note(idx, name, price) -> None:
        note: Note = {'id': idx, 'name': name, 'price': price}
        PurchaseNote.notes_all_purchases.append(note)

        try:
            with open(PurchaseNote.notes_file, 'w') as file:
                json.dump(PurchaseNote.notes_all_purchases, file)
        except FileNotFoundError as error:
            print(error)

    @classmethod
    def show_all_purchases(cls) -> None:
        for note in cls.notes_all_purchases:
            print(f'{note['id']}: - {note["name"]} -> {note["price"]}')
        print('--------------------')

    @classmethod
    def find_purchase_by_name(cls, finding_item):
        for item in PurchaseNote.notes_all_purchases:
            if item['name'] == finding_item:
                return 'finding_purchase is: ', item

    @classmethod
    def find_purchase_by_max_price(cls):
        notes_sorted_by_price = PurchaseNote.notes_all_purchases.copy()
        notes_sorted_by_price.sort(key=lambda x: x["price"], reverse=True)
        return 'Max price purchase was: ', notes_sorted_by_price[0]

    @classmethod
    def delete_purchase_by_id(cls, idx):
        for item in PurchaseNote.notes_all_purchases:
            if item["id"] == idx:
                PurchaseNote.notes_all_purchases.remove(item)


note = PurchaseNote()
note.add_note(1, 'fishes', 100)
note.add_note(2, 'meat', 200)
note.add_note(3, 'water', 50)
note.add_note(4, 'apples', 120)
note.add_note(5, 'bananas', 60)

PurchaseNote.show_all_purchases()

print(note.find_purchase_by_name('water'))
print(note.find_purchase_by_max_price())
note.delete_purchase_by_id(3)
PurchaseNote.show_all_purchases()
