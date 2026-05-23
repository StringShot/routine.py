print("I wake up in the morning and 6:00")
print("I go for a Morning Devotion")
borb = (input("Do I brush or bath first today? "))
if borb == "brush":
    print("I brush my teeth before taking a bath")
elif borb == "bath":
    print("I take a bath before brushing my teeth")
else:
    print("I don't", borb, "first, I'll bath first before brushing my teeth")
    print("I get dressed")
    eorp = (input("Do I eat breakfast or pack my bag first? "))
    if eorp == "eat":
        print("I eat breakfast before packing my bag")
    elif eorp == "pack":
        print("I pack my bag before eating breakfast")
    else:
        print("I don't", eorp, "first, I'll pack my bag before eating breakfast")
print("I leave for school at 7:40")
