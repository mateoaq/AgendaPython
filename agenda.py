import csv


class Contacto:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class Agenda:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contacto = Contacto(name, phone, email)
        self._contacts.append(contacto)
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))
        self._save()

    def show_all(self):
        for contacto in self._contacts:
            self._print_contact(contacto)

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')

    def delete(self, name):
        for idx, contacto in enumerate(self._contacts):
            if contacto.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def update(self, name):
        self.delete(name)

        name = str(input("Ingrese el nombre del contacto:"))
        phone = int(input("Ingrese el telefono:"))
        email = str(input("Ingrese el email:"))

        self.add(name, phone, email)

    def search(self, name):
        for contacto in self._contacts:
            if contacto.name.lower() == name.lower():
                self._print_contact(contacto)
                break
        else:
            self._not_found()

    def _not_found(self):
        print("*********")
        print("No encontramos el contacto!!")
        print("*********")

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contacto in self._contacts:
                writer.writerow(
                    (contacto.name, contacto.phone, contacto.email))


def run():

    agenda = Agenda()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            agenda.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input("Ingrese el nombre del contacto:"))
            phone = int(input("Ingrese el telefono:"))
            email = str(input("Ingrese el email:"))

            agenda.add(name, phone, email)

        elif command == 'ac':
            name = str(input("Ingrese el nombre del contacto:"))

            agenda.update(name)

        elif command == 'b':
            name = str(input("Ingrese el nombre del contacto:"))

            agenda.search(name)

        elif command == 'e':
            name = str(input("Ingrese el nombre del contacto:"))

            agenda.delete(name)

        elif command == 'l':

            agenda.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
