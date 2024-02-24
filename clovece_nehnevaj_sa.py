from random import randint

# Mojím cieľom je simulovať hru dvoch hráčov A a B pri hre 'Človeče, nehnevaj sa!' bez zásahu pozorovateľa
print("-=-=-=- Človeče, nehnevaj sa! -=-=-=-")


class Hrac:  # Class ktorý vytvára hodnoty pre hráčov
    def __init__(self, vzdialenost, domcek, por_dom, znak, hrac_dom, start_pos):
        self.vzdialenost = vzdialenost      # List vzdialeností, ktoré figúrka prešla
        self.domcek = domcek                # Počet zaplnených domčekov
        self.por_dom = por_dom              # List miest políčok ktoré sú domčeky
        self.znak = znak                    # Značenie hráča
        self.hrac_dom = hrac_dom            # List obsahujúci časť hracej dosky kde sú domčeky hráča
        self.start_pos = start_pos          # Index políčka, na ktorom hráč začína (posun od ŠTART)


def gen_sachovnicu(n):          # Funkcia vygeneruje šachovnicu ako list stringov
    pol = 4*n - 4                   # Počet políčok
    dom = int((n - 3) / 2)          # Počet domčekov
    doska_hrac = []                 # Hlavná hracia doska
    doska_dom_a = []                # Doska obsahujúca domčeky hráča A
    doska_dom_b = []                # Doska obsahujúca domčeky hráča B

    for i in range(pol):        # Generácia políčok
        doska_hrac.append("*")

    for i in range(dom):      # Generácia domčekov
        doska_dom_a.append("D")
        doska_dom_b.append("D")

    return [doska_hrac, doska_dom_a, doska_dom_b]


def nova_figurka(poc_pol, hrac, plocha):       # Táto funkcia je spustená pri postavení novej figurky na plochu
    if hrac:
        plocha[0] = "A"
    else:
        plocha[int(poc_pol/2)] = "B"
    return plocha


def hod_kockou():     # Rekurzívne vráti hodnotu hodu kocky
    kocka = randint(1, 6)
    if kocka == 6:      # Ak hráč hodí 6 tak ide znovu
        return kocka + hod_kockou()
    else:
        return kocka


def zaciatok():         # Zistí či hráč hodil 6 ak nemá figúrku na hracom poli
    print("Kocky sú hodené:", end=" ")
    for i in range(3):
        a = hod_kockou()
        if a > 5:       # Hráč hádže znovu ak hodí 6
            print(6)
            return True
        print(a, end=" ")
    print()
    return False


def tlac_sachovnicu(n, doska, dom_a, dom_b, pol, stred):    # Vytlačí na obrazovku šachovnicu po stringoch v liste
    print("  ", end="")
    for i in range(n):          # Generácia horizontálnej číselnej osi
        print(f"  {i % 10}", end="")    # Pre hodnotu 10 sa preklopíme do 0 a začíname od znovu
    print()

    for i in range(n):
        if i == 0:              # "Prvý" riadok
            print(f"{i % 10}" + pol * "   " + doska[-2] + "  " + doska[-1] + "  " + doska[0] + pol * "   ")
            doska.pop(-1)   # Položené políčka sú vyhodené z možných políčok, pre urýchlenie tlačenia
            doska.pop(-1)
            doska.pop(0)
        elif i == (n-1):        # Posledný riadok
            print(f"{i % 10}" + pol * "   " + doska[2] + "  " + doska[1] + "  " + doska[0] + pol * "   ")
        elif i == (stred-1):    # Stredný riadok
            d = pol - 1         # Počet domčekov
            print(f"{i % 10}   " + doska[-1] + "  " + d * "D  " + "X  " + d * "D  " + doska[0])
            doska.pop(0)
            doska.pop(-1)
        elif i == (stred-2) or i == stred:  # Riadky okolo stredu
            row1 = ""
            row2 = ""
            for j in range(pol):
                row1 += f" {doska[0]} "
                row2 += f" {doska[-1]} "
                doska.pop(0)
                doska.pop(-1)
            if i == stred:      # Vo vrchnejšom riadku ideme iným smerom ako v spodnejšom preto reversujeme riadky
                print(f"{i % 10}  " + row2 + f" {dom_b[-1]} " + row1[::-1])
                dom_b.pop(-1)
            else:
                print(f"{i % 10}  " + row2[::-1] + f" {dom_a[0]} " + row1)
                dom_a.pop(0)
        else:                   # Ostatné riadky (POLÍČKO DOMČEK POLÍČKO)
            if i < stred:
                print(f"{i % 10}" + pol * "   " + doska[-1] + "  " + dom_a[0] + "  " + doska[0] + pol * "   ")
                dom_a.pop(0)
            else:
                print(f"{i % 10}" + pol * "   " + doska[-1] + "  " + dom_b[-1] + "  " + doska[0] + pol * "   ")
                dom_b.pop(-1)
            doska.pop(0)
            doska.pop(-1)

    print()
    return


def pohyb(hr, prt_hr, poc_policok, doska):
    h = hod_kockou()    # Hráč hádže kockou
    print(f"Hráč {hr.znak} je na ťahu.")    # Výpis ťahu a hodu
    print("Kocky sú hodené:", h)
    # Ak hráč hodil 6, nemá na prvom políčku figúrku a má ešte možnosť novej figúrky
    m = hr.vzdialenost[0] + h   # Konečná vzdialenosť hráča
    if h > 6:
        if 0 not in hr.vzdialenost and len(hr.vzdialenost) < len(hr.por_dom):
            x = hr.znak == "A"      # Podľa pravdivosti sa vypočíta ktorému hráčovi sa pridá figúrka
            nova_figurka(poc_policok, x, doska)
            hr.vzdialenost.append(0)
            m -= 6      # Pohne sa figúrkou, ktorá je ďalej, ale o 6 políčok menej

    if m < poc_policok:     # Ak jeho pohybom neskončí v domčeku
        koniec = doska[(m+hr.start_pos) % poc_policok]  # Charakter na konečnej pozícii
        if koniec != hr.znak:   # V prípade že to nie je vlastná figúrka (NO FRIENDLY FIRE)
            if koniec == prt_hr.znak:   # Ak to je nepriateľ
                if m - hr.start_pos == prt_hr.start_pos:    # Ak vyhadzujeme "čestvú" figúrku na ŠTARTe
                    prt_hr.vzdialenost.pop(-1)
                else:                                       # Všetky ostatné situácie
                    prt_hr.vzdialenost.pop(0)
                print(f"BOOM! Hráč {prt_hr.znak} stráca figúrku")

            doska[(hr.vzdialenost[0]+hr.start_pos) % poc_policok], doska[(m+hr.start_pos) % poc_policok] = "*", hr.znak
            hr.vzdialenost[0] = m       # Posunieme figúrku na správne miesto a zapíšeme novú vzdialenosť

    elif m in hr.por_dom:       # Ak ideme do domčeka
        doska[(hr.vzdialenost[0]+hr.start_pos) % poc_policok], hr.hrac_dom[m-poc_policok] = "*", hr.znak
        hr.vzdialenost.pop(0)   # Posunieme figúrku na správne miesto
        hr.domcek += 1
        hr.por_dom.remove(m)    # Pripočítame si domček a odstránime možnú koncovú hodnotu domčeka

    elif poc_policok+5 == hr.por_dom[0] and h > 6:  # Špeciálny prípad ak máme domček vo vzdialenosti 6
        doska[(hr.vzdialenost[0] + hr.start_pos) % poc_policok], hr.hrac_dom[5] = "*", hr.znak
        hr.vzdialenost.pop(0)   # V tomto prípade by sme v skutočnosti nehádzali druhý krát kockou ak by nám padla 6tka
        hr.domcek += 1
        hr.por_dom.remove(poc_policok+5)

    return


def clovece(n):       # Hlavná funkcia ktorá volá ostatné
    tah = True          # Kto je (a nie je) na ťahu; True = A, False = B
    dom_n = int((n - 3) / 2)            # Počet domčekov na hráča
    pol = n*4 - 4                       # Počet políčok
    stred = int((n+1)/2)                # Stredný riadok
    hvz_n = dom_n + 1                   # Počet hviezdičiek (políčok na jednej strane ramena)

    rng = []        # Možné konečné hdnoty v domčekoch
    for i in range(pol, pol+dom_n):
        rng.append(i)

    dosky = gen_sachovnicu(n)              # Hracie pole pred prvým hodom kocky
    doska = dosky[0]

    a = Hrac([], 0, rng[:], "A", dosky[1], 0)  # Hráč A
    b = Hrac([], 0, rng[:], "B", dosky[2], (n*2)-2)  # Hráč B

    tlac_sachovnicu(n, doska[:], a.hrac_dom[:], b.hrac_dom[:], hvz_n, stred)

    while a.domcek < dom_n and b.domcek < dom_n:  # Sledujem či obidvaja hráči nemajú max hodnotu domčekov
        if (len(a.vzdialenost) == 0 and tah) or (len(b.vzdialenost) == 0 and not tah):  # Ak hráč má 0 figúrok
            if tah:
                print(f"Hráč A je na ťahu.")
            else:
                print(f"Hráč B je na ťahu.")
            if zaciatok():      # Funkcia hodí kockou 3-krát a vyhodnotí či hráč dostal 6
                if tah:
                    a.vzdialenost.append(0)
                else:
                    b.vzdialenost.append(0)
                doska = nova_figurka(pol, tah, doska)   # Položí príslušnú figúrku na hraciu plochu
            else:
                tah = not tah       # Výmena ťahov v prípade že hráč nedal 6
            tlac_sachovnicu(n, doska[:], a.hrac_dom[:], b.hrac_dom[:], hvz_n, stred)

        if (len(a.vzdialenost) != 0 and tah) or (len(b.vzdialenost) != 0 and not tah):  # Ak sa vie hráč hýbať má ťah
            if tah:
                pohyb(a, b, pol, doska)     # Hráč podľa jeho situácia vykonná pohyb
            else:
                pohyb(b, a, pol, doska)
            tah = not tah
            tlac_sachovnicu(n, doska[:], a.hrac_dom[:], b.hrac_dom[:], hvz_n, stred)

    if a.domcek == dom_n:       # Podľa toho ktorá hodnota je vyššia na konci hry sa vybere víťaz (opak golfu)
        vitaz = "Hráč A vyhral!"
    else:
        vitaz = "Hráč B vyhral!"

    return vitaz


v = int(input("Zadajte prosím veľkosť plochy: "))       # Zistí od používateľa veľkosť šachovnice v x v
while v < 5 or v % 2 == 0:                              # Skontroluje či číslo vyhovuje
    print("Hodnota musí byť vačšia ako 4 a nepárna")
    v = int(input("Zadajte prosím veľkosť plochy: "))

print(clovece(v))
