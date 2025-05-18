capitals = {"usa":"washington",
            "india":"newdelhi",
            "nepal":"kathmandu",
            "china":"beijing"}
#print(capitals.get("china"))
#if capitals.get("japan"):
#    print("the capitals exits")
#else:
#    print("poda punda")
#capitals.update({"japan":"tokyo"})
#capitals.pop("nepal")       #removes nepal
#capitals.popitem()          #removes last updated item on dictionary
#value = capitals.values()
for i, j in capitals.items():
    print(i,j)
print()
#value = capitals.values()
#for i in value:
#    print(i)
#for x , y in capitals.items():
#   print(f"{x}:{y}")
#key = capitals.get("usa")
#print(key)
#print(capitals)