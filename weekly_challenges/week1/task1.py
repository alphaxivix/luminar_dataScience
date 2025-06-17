#Check if a string is a valid identifier
#rules ==> 1. it should start with a letter (a-z,A-Z) or an underscore (-)
#          2. followed by zero or more letters,underscores or digits (0-9

string_id =input("Enter the string: ")

valid_f_letter = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_' ]
valid_i_body = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',0,1,2,3,4,5,6,7,8,9,'_' ]

if string_id[0] in valid_f_letter and all(c in valid_i_body for c in string_id[1:]):
    print("This is a valid identifier.....")
else:
    print("This is not a valid identifier!!")