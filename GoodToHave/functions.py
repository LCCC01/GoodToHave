def GetInputBetween(startval:int, endval:int) -> int:
    while True:
        try:
            val = int(input("Ange val: "))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt menyval. Endast mellan {startval} och {endval}!")
        except:
            print("Ange ett tal tack!")

if __name__ == "__main__":    #Dessa rader körs endast ifall det är den aktuella filen som man kör i.
    x = GetInputBetween(100, 200)       #Om filen importeras så och körs i en annan fil så körs inte dessa rader.
    print(x)