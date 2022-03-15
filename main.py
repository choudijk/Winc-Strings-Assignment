# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
name_goalscorer_0 = "Ruud Gullit"
name_goalscorer_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = name_goalscorer_0 +" "+ str(goal_0) + ", " + name_goalscorer_1 +" "+ str(goal_1)
report = f"{name_goalscorer_0} scored in the {goal_0}nd minute\n{name_goalscorer_1} scored in the {goal_1}th minute"

#part 2
player = "Wim Kieft"
space = player.find(" ")
length_name = len(player)

first_name = player[slice(0, space)]
last_name = player[slice((space+1),(length_name + 1))]

first_name_len = len(first_name)
last_name_len = len(last_name)
print(first_name)
print(last_name_len)

name_short = player[slice(0,1)] + ". " + last_name
print(name_short)

chant = (first_name + "! ")*(first_name_len-1) + (first_name +"!")
print(chant)
good_chant = (chant[slice(len(chant)-1,len(chant)+1)] != " ")
print(good_chant)