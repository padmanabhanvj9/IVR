import phonenumbers
import json
def phonenumbers_country(request):
   phone = request.json['phone']
   tstl = phonenumbers.parse(phone,None)
   print(tstl.country_code)
   print(tstl.national_number)
   countrycode = tstl.country_code
   national_number = tstl.national_number
   return (json.dumps({'Status':'Success', 'Returnvalue_Conutry': countrycode, 'Returnvalue_Nationalnnumber': national_number}, indent =4))
