DEBUGGING = True

def DEBUG(*args):
    if DEBUGGING: 
        print("DEBUG: " + " ".join(map(str, args)))
