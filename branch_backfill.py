import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_branches.settings')
from bank.models import Branch, Bank

django.setup()

def save_bank_branch_table():

    c_file= open("C:\\Users\DeLL\\Documents\\final_branch.txt")
    bank_details = c_file.readlines()


    for data in range(1, len(bank_details)):
        row = bank_details[data].decode("utf-8").split('"')
        try:
            split_zero_index = row[0].split(',')
            split_last_index = row[2].split(',')
            #print "split_last_index", split_last_index
            ifsc = split_zero_index[0]
            bank_id = split_zero_index[1]
            branch_name = split_zero_index[2]
            address = row[1]
            city = split_last_index[1]
            district = split_last_index[2]
            state = split_last_index[3]

            branch_obj = Branch()
            bank = Bank.objects.get(b_id=bank_id)
            branch_obj.ifsc = ifsc
            branch_obj.bank_id = bank
            branch_obj.branch = branch_name
            branch_obj.address = address
            branch_obj.city = city
            branch_obj.district = district
            branch_obj.state = state
            branch_obj.save()

        except:

            "exception string: " + bank_details[data].decode("utf-8")
            pass


save_bank_branch_table()


