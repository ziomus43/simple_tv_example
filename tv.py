import keyboard
import switch

class tv:
    kanaly=[1, 2, 3, 4, 5]
    def __init__(self):
        self.kanal=None
        self.volume=None
        self.status=False


    def tv_on(self):
        self.kanal=tv.kanaly[1]
        self.volume=30
        self.status=True
        print("tv is on...")

    def tv_off(self):
        self.kanal = None
        self.volume = None
        self.status==False
        print("...tv is off")
        exit()


    def zmiana_kanalu(self):

            while (1):
                print("wybierz kanal sposrod kanalow od 1 do 5: ")
                k=input()
                if(k.isdigit()):
                    k = int(k)
                    if (k >= 1 and k <= 5 and k % 1 == 0):

                        for el in tv.kanaly:
                            if(el==int(k)):
                                self.kanal=el
                                print("przelaczono na kanal "+str(k))
                                return k
                    else:
                        print("*nie ma takiego kanalu!*")

    def k_next(self):

            for el in tv.kanaly:
                if(el==self.kanal):
                    inx=tv.kanaly.index(el)
                    if(inx==4):
                        self.kanal=tv.kanaly[0]
                        print("przelaczono na kanal " + str(self.kanal))
                        return self.kanal
                    self.kanal=tv.kanaly[inx+1]
                    print("przelaczono na kanal " + str(self.kanal))
                    return self.kanal

    def k_previous(self):

            for el in tv.kanaly:
                if(el==self.kanal):
                    inx=tv.kanaly.index(el)
                    if(inx==0):
                        self.kanal=tv.kanaly[4]
                        print("przelaczono na kanal " + str(self.kanal))
                        return self.kanal
                    self.kanal=tv.kanaly[inx-1]
                    print("przelaczono na kanal " + str(self.kanal))
                    return self.kanal


    def volume_up(self):

        if(self.volume==100):
            print("volume: " + str(self.volume)+" (100=max)")

        if(self.volume<100):
            self.volume+=5
            print("volume: "+str(self.volume))


    def volume_down(self):

        if (self.volume == 0):
            print("volume: " + str(self.volume)+" (0 - dzwiek wylaczony)")

        if (self.volume > 0):
            self.volume -= 5
            print("volume: " + str(self.volume))


    def mute(self):
        self.volume=0
        print("glosnosc=0 - dzwiek wylaczony")

    def menu(self):
        print("\n\n     *** Lista przyciskow na pilocie ***")
        print("\n**| podglosnij + |**")
        print("**| przycisz - |**")
        print("**| mute u |**")
        print("**| kanal poprzedni p |**")
        print("**| kanal nastepny n |**")
        print("**| zmiana kanalu z |**")
        print("**| wylacz w |**")
        print("**| wyswietl menu dzialania przyciskow m |**")


if(__name__=="__main__"):
    t1=tv()
    while(1):
        print("Aby wlaczyc tv nacisnij 1")
        on=input()
        if(on=="1"):
            t1.tv_on()
            t1.menu()
            break
        else:
            print("tym przyciskiem nie wlaczamy telewizora ;<")


    while(1):
        print("wcisnij przycisk na pilocie ('m' aby wyswietlic pomoc)")
        i = input()
        if(i=="z" and t1.status == True):
            t1.zmiana_kanalu()

        elif (i == "n" and t1.status == True):
            t1.k_next()

        elif (i == "p" and t1.status == True):
            t1.k_previous()

        elif(i=="+" and t1.status == True):
            t1.volume_up()

        elif (i == "-" and t1.status == True):
            t1.volume_down()

        elif(i=="u" and t1.status==True):
            t1.mute()

        elif(i=="w" and t1.status == True):
            t1.tv_off()

        elif(i=="m" and t1.status==True):
            t1.menu()

        else:
            print("nie ma takiego przycisku na pilocie!\n")


