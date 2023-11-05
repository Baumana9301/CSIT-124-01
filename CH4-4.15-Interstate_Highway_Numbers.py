# CSIT-124-01 LAB 4.15 - Interstate Highway Numbers

# Given a highway #, indicate whether it is primary or auxiliary.
# If aux., indicate what primary it serves.
# Also indicate if said primary runs north/south or east/west

# Input

hnum = int(input('Please type a highway number: '))

# Branching & Output

# test

if 0 < hnum < 100:
    if hnum % 2 == 0:
        print(f"I-{hnum} is primary, going east/west.")
    else:
        print(f"I-{hnum} is primary, going north/south.")
elif 100 <= hnum < 1000:
    if hnum % 100 == 0:
        print(f"{hnum} is not a valid interstate highway number.")
    elif ((hnum % 100) % 2) == 0:
        print(f"I-{hnum} is auxiliary, serving I-{hnum % 100}, going east/west.")
    else:
        print(f"I-{hnum} is auxiliary, serving I-{hnum % 100}, going north/south.")
else:
    print(f"{hnum} is not a valid interstate highway number.")
    
