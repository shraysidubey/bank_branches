import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_branches.settings')
from bank.models import Bank

django.setup()

bank_data = open("C:\\Users\\DeLL\\Documents\\bank.txt")
bank_data_lines = bank_data.readlines()    # ["STATE BANK OF INDIA	1", "PUNJAB NATIONAL BANK	2", "CANARA BANK	3"]

for data in bank_data_lines:
    row = data.decode("utf-8").split("\t")
    bank_name = row[0].encode("utf-8")
    bank_id = int(row[1].rstrip("\n"))
    #print "bank_name",bank_name
    #print "bank_id", bank_id
    bank = Bank()
    bank.name = bank_name
    bank.b_id = bank_id
    bank.save()

bank_data.close()


