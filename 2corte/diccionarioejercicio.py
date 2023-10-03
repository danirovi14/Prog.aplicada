sensors={"living room":21,"kitchen":23,"bedroom":20,"pantry":22}
num_cameras={"backyard":6,"garage":2,"driveway":1}
print(sensors)

traslations= {"mountain":"orod","bread":"bass","friend":"mellon","horse":"roch"}
print(traslations)

children={"von trapp":["Johannes","rosmarie","eleonrore"],"carleone":["sonny","fredo","michael"],"1000719793":20}
print(children)

my_empty_dictionary= {}
print(my_empty_dictionary)

animals_in_zoo={"zebras":8,"monkeys":12}
animals_in_zoo["dinosaurs"]=0
print(animals_in_zoo)

menu={"oatmeal":3,"avocado":6,"carrot":5,"muffin":2}
print(menu)
animals_in_zoo={"dinosaurs":0}
animals_in_zoo={"dinosaurs":0}
print(animals_in_zoo)

user_ids={"teraCoder":9018293,"proProgammer":119238}
print(user_ids)
user_ids.update({"theLopper":1348446,"sringqueen":85739})
print(user_ids)

oscar_winners={"Best picture":"La La Land","Best Actor":"Caswy Affleck","Best Actress":"Emma Stone","Animated Featured":"Zootopia"}
print(oscar_winners)
oscar_winners.update({"Supporting Actress":"Viola Davis"})
oscar_winners["Best picture"]="Moonlight"
print (oscar_winners)
oscar_winners["Animated Featured"]="Sherk"
print(oscar_winners)

drink=["expresso","chai","deacaf","drip"]
caffeine=[60,40,0,120]
zipped_drinks=zip(drink,caffeine)
drink_to_caffeine={key: value for key, value in zipped_drinks}
print(drink_to_caffeine) 
