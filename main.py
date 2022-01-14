from flat import Bill, Flatmate
from reports import PdfReport, FileSharer



#CLI
input_total_amount_user = float(input('Hey User, Please Enter the Total Bill Amount: '))
input_month_user = input('Please Enter the Period of Bill: ')
input_user1_name = input('Please Enter the name of Flatmate1: ')
input_user1_days = int(input('Please Enter no. of days '+ input_user1_name +' stayed in the House: '))
input_user2_name = input('Please Enter the name of Flatmate2: ')
input_user2_days = int(input('Please Enter no. of days '+ input_user2_name +' stayed in the House: '))

#Function calls
my_bill = Bill(input_total_amount_user, input_month_user)
person1 = Flatmate(input_user1_name, input_user1_days)
person2 = Flatmate(input_user2_name, input_user2_days)

print(input_user1_name +' pays: '+ str(person1.pays(my_bill, person2)))
print(input_user2_name +' pays: '+ str(person2.pays(my_bill, person1)))


pdf_report = PdfReport(f'{my_bill.period}.pdf')
pdf_report.generate(person1, person2, my_bill)

#share link to others
share=FileSharer(pdf_report.filename)
print(share.upload())

