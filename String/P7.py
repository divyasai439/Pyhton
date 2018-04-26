#The method replace() returns a copy of the string in which the values of old string have been replaced with the new value.

oldstring ="I have some money"
newstring = oldstring.replace('have', 'had')
print newstring
print oldstring.replace('some', 'lot of')
print oldstring.replace(oldstring[0:50], 'Divya')