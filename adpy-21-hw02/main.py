from pprint import pprint
import csv
import re

def make_phonebook(contacts_list, titles):
    contacts = {}
    for contact in contacts_list:
        name =' '.join(contact[0:2]).split(' ')[:3]
        if (name[0], name[1]) in contacts:
            for i, _ in enumerate(name):
                if titles[i] not in contacts[(name[0], name[1])]:
                    contacts[(name[0], name[1])][titles[i]] = _
        else:
            contacts[(name[0], name[1])] = {}
            for i, _ in enumerate(name):
                contacts[(name[0], name[1])][titles[i]] = _
        for i, _ in enumerate(contact[3:7]):
            if titles[i + 3] not in contacts[(name[0], name[1])]:
                contacts[(name[0], name[1])][titles[i + 3]] = _
            elif contacts[(name[0], name[1])][titles[i + 3]] == '':
                contacts[(name[0], name[1])][titles[i + 3]] = _
    return contacts

def make_phone_num(phone):
    pattern = r'(.*)[Д|д]об\.?\s*(\d+)'
    result = re.findall(pattern, phone)
    ext_no = None
    if len(result):
        ext_no = result[0][-1]
    pattern = r'[\+7|8]+[\s\-\(\)]*(\d*)[\s\-\(\)]*(\d*)[\s\-\(\)]*(\d*)[\s\-\(\)]*(\d*)'
    result = re.findall(pattern, phone)
    phone_no = '+7' + ''.join(result[0])
    if ext_no:
        phone_no += f' доб.{ext_no}'
    phone_no = phone_no[:2] + '(' + phone_no[2:5] + ')' + phone_no[5:8] + '-' + phone_no[8:10] + '-' + phone_no[10:]
    return phone_no

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код

    titles = contacts_list.pop(0)
    phonebook = make_phonebook(contacts_list, titles)

    for contact, contact_data in phonebook.items():
        contact_data['phone'] = make_phone_num(contact_data['phone'])
    new_contacts_list = [titles]
    for contact_data in phonebook.values():
        tmp_listed_contact = []
        for title in titles:
               tmp_listed_contact.append(contact_data[title])
        new_contacts_list.append(tmp_listed_contact)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
      datawriter = csv.writer(f, delimiter=',',)
      datawriter.writerows(new_contacts_list)