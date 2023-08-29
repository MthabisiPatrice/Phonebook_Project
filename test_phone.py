import pytest
import csv

from contact_book_final import (
    get_write_contacts,
    get_read_contacts,
    do_add_contact,
    get_edit_contact,
    do_delete_contact,
    get_view_contacts,
)


def test_get_write_contacts():
    contacts = [['Mthabisi Munyariri', '141 S 1st Main', '208-821-8996', 'munyariri94@gmail.com']]
    get_write_contacts(contacts)

    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        actual_contacts = list(reader)

    assert actual_contacts == contacts


def test_get_read_contacts():
    contacts = [['Mthabisi Munyariri', '141 S 1st Main', '208-821-8996', 'munyariri94@gmail.com']]
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

    expected_contacts = get_read_contacts()

    assert expected_contacts == contacts


def test_do_add_contact():
    contacts = []
    do_add_contact('Denzel Bheka', '125 Plumer Street', '456-789-0123', 'denzel@gmail.com')

    expected_contacts = ['Denzel Bheka', '125 Plumer Street', '456-789-0123', 'denzel@gmail.com']
    contacts = get_read_contacts()

    assert expected_contacts in contacts


def test_get_edit_contact():
    contacts = [['Mthabisi Munyariri', '141 S 1st Main', '208-821-8996', 'munyariri94@gmail.com']]
    get_edit_contact(0, 'Denzel Bheka', '125 Plumer Street', '456-789-0123', 'denzel@gmail.com')

    expected_contacts = [['Denzel Bheka', '125 Plumer Street', '456-789-0123', 'denzel@gmail.com']]

    assert contacts == expected_contacts


def test_get_delete_contact():
    deleted_contacts = ['Mthabisi Munyariri', '141 S 1st Main', '208-821-8996', 'munyariri94@gmail.com']
    contacts = get_read_contacts()
    index = contacts.index(deleted_contacts)
    do_delete_contact(index)
    contacts = get_read_contacts()

    assert deleted_contacts not in contacts


def test_get_view_contacts():
    contacts = [['Mthabisi Munyariri', '141 S 1st Main', '208-821-8996', 'munyariri94@gmail.com']]
    get_view_contacts()


pytest.main(["-v", "--tb=line", "-rN", __file__])
