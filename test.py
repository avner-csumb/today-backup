# snake_case
fave_number = 4

# lists in Python
my_list = [4, '4', True]

# for cur_val in my_list:
#     print('value is: ' + str(cur_val))

my_list.append('guacamole')

# print(my_list[3][::-1])

fave_color = 'green'

# print(fave_color[1:3])

list_of_numbers = range(101,57,-1)

# print(list_of_numbers)

# fave_genre = raw_input('What\'s your favorite style of music? ')
# fave_musician = raw_input('Who is your favorite musician? ')
#
# print('Your favorite style of music is ' + fave_genre + ' and your favorite musician is ' + fave_musician + '.')
#
#
# print('Again, the genre is {0} and the musician is {1}.'.format(fave_genre, fave_musician))
#
# print('Yet again, your favorite musician is %s.' %(fave_musician))

def helloMachine(user_name, zip_code):
    divided_zip = zip_code/5

    hello_string = 'Hello ' + str(user_name) + ', by the way your zip code divided by 5 is ' +  str(divided_zip) + '. ' + str(user_name) + ' is a nice name.'

    other_string = 'Hello {0}, by the way your zip code divided by 5 is {1}. {0} is a nice name.'.format(str(user_name),str(divided_zip))

    return other_string

print(helloMachine('Helga', 90210) + ' I don\'t like balloons.')
