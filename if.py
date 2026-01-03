def a_or_b(value):
    if value == "A":
        print("A")
    elif value == "B":
        print("B")
    else:
        print("Other")

a_or_b("A") # Should print "A"
a_or_b("B") # Should print "B"
a_or_b("C") # Should print "Other"
