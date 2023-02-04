import time

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
def fast_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def ana_giris():
    slow_print("ÇEVİRİCİYE HOŞGELDİNİZ!\n")
    slow_print("Lütfen hangi çeviriciye gitmek istediğini seç.\n 1-Basınç Çevirici\n 2-Hacim Çevirici\n")
    user_choise = input()
    if user_choise == "Basınç Çevirici" or user_choise == "1" or user_choise == "Basınç":
        slow_print("Basınç Çeviriciye Gönderiliyorsunuz...\n")
        basinc_kismi()
    elif user_choise == "Hacim Çevirici" or user_choise == "2" or user_choise == "Hacim":
        slow_print("Hacim Çeviriciye Gönderiliyorsunuz...\n")
        hacim_kismi()
    else:
        fast_print("Böyle Bir Çeviricimiz Yok!")
        ana_giris()

def basinc_kismi():
    global basinc_birimi
    global atm_cevirici
    global cmHG_cevirici
    global mmHG_cevirici
    global torr_cevirici
    
    slow_print("BASINÇ ÇEVİRİCİ\n")
    fast_print("Lütfen çevirmek istediğin basınç birimini seç.(1-atm, 2-cmHG, 3-mmHG, 4-Torr)\n")
    basinc_birimi = input()
    if basinc_birimi == "atm" or basinc_birimi == "1":
        atm_cevirici()
    elif basinc_birimi == "cmHG" or basinc_birimi == "2":
        cmHG_cevirici()
    elif basinc_birimi == "mmHG" or basinc_birimi == "3":
        mmHG_cevirici()
    elif basinc_birimi == "Torr" or basinc_birimi == "4":
        torr_cevirici()
    else:
        print("Böyle Bir Basınç Birimi Bulunmuyor!")
        basinc_kismi()
def atm_cevirici():
    global atm_to
    global atm_degeri
    global sonuc
    
    slow_print("ATM ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevrileceğini seçiniz.(1-atm, 2-cmHG, 3-mmHG, 4-Torr)\n")
    atm_to = input()
    if atm_to == "atm" or atm_to == "1":
        print("Lütfen çevirmek istediğiniz atm değerini giriniz:")
        atm_to = "atm"
        atm_degeri = int(input())
        sonuc = atm_degeri * 1
        atm_sonuc_kismi()
    elif atm_to == "cmHG" or atm_to == "2":
        print("Lütfen çevirmek istediğiniz atm değerini giriniz:")
        atm_to = "cmHG"
        atm_degeri = int(input())
        sonuc = atm_degeri * 76
        atm_sonuc_kismi()
    elif atm_to == "mmHG" or atm_to == "3":
        print("Lütfen çevirmek istediğiniz atm değerini giriniz:")
        atm_to = "mmHG"
        atm_degeri = int(input())
        sonuc = atm_degeri * 760
        atm_sonuc_kismi()
    elif atm_to == "Torr" or atm_to == "4":
        print("Lütfen çevirmek istediğiniz atm değerini giriniz:")
        atm_to = "Torr"
        atm_degeri = int(input())
        sonuc = atm_degeri * 760
        atm_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        atm_cevirici()
def cmHG_cevirici():
    global cmHG_to
    global cmHG_degeri
    global sonuc
    
    slow_print("CMHG ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevrileceğini seçiniz.(1-atm, 2-cmHG, 3-mmHG, 4-Torr)\n")
    cmHG_to = input()
    if cmHG_to == "atm" or cmHG_to == "1":
        print("Lütfen çevirmek istediğiniz cmHG değerini giriniz:")
        cmHG_to = "atm"
        cmHG_degeri = int(input())
        sonuc = cmHG_degeri / 76
        cmHG_sonuc_kismi()
    elif cmHG_to == "cmHG" or cmHG_to == "2":
        print("Lütfen çevirmek istediğiniz cmHG değerini giriniz:")
        cmHG_to = "cmHG"
        cmHG_degeri = int(input())
        sonuc = cmHG_degeri * 1
        cmHG_sonuc_kismi()
    elif cmHG_to == "mmHG" or cmHG_to == "3":
        print("Lütfen çevirmek istediğiniz cmHG değerini giriniz:")
        cmHG_to = "mmHG"
        cmHG_degeri = int(input())
        sonuc = cmHG_degeri * 10
        cmHG_sonuc_kismi()
    elif cmHG_to == "Torr" or cmHG_to == "4":
        print("Lütfen çevirmek istediğiniz cmHG değerini giriniz:")
        cmHG_to = "Torr"
        cmHG_degeri = int(input())
        sonuc = cmHG_degeri * 10
        cmHG_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        cmHG_cevirici()

def mmHG_cevirici():
    global mmHG_to
    global mmHG_degeri
    global sonuc
    
    slow_print("MMHG ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevrileceğini seçiniz.(1-atm, 2-cmHG, 3-mmHG)\n")
    mmHG_to = input()
    if mmHG_to == "atm" or mmHG_to == "1":
        print("Lütfen çevirmek istediğiniz mmHG değerini giriniz:")
        mmHG_to = "atm"
        mmHG_degeri = int(input())
        sonuc = mmHG_degeri / 760
        mmHG_sonuc_kismi()
    elif mmHG_to == "cmHG" or mmHG_to == "2":
        print("Lütfen çevirmek istediğiniz mmHG değerini giriniz:")
        mmHG_to = "cmHG"
        mmHG_degeri = int(input())
        sonuc = mmHG_degeri / 10
        mmHG_sonuc_kismi()
    elif mmHG_to == "mmHG" or mmHG_to == "3":
        print("Lütfen çevirmek istediğiniz mmHG değerini giriniz:")
        mmHG_to = "mmHG"
        mmHG_degeri = int(input())
        sonuc = mmHG_degeri / 1
        mmHG_sonuc_kismi()
    elif mmHG_to == "Torr" or mmHG_to == "4":
        print("Lütfen çevirmek istediğiniz mmHG değerini giriniz:")
        mmHG_to = "Torr"
        mmHG_degeri = int(input())
        sonuc = mmHG_degeri / 1
        mmHG_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        mmHG_cevirici()
        
def torr_cevirici():
    global torr_to
    global torr_degeri
    global sonuc
    
    slow_print("TORR ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevrileceğini seçiniz.(1-atm, 2-cmHG, 3-mmHG, 4-Torr)\n")
    torr_to = input()
    if torr_to == "atm" or torr_to == "1":
        print("Lütfen çevirmek istediğiniz Torr değerini giriniz:")
        torr_to = "atm"
        torr_degeri = int(input())
        sonuc = torr_degeri / 760
        torr_sonuc_kismi()
    elif torr_to == "cmHG" or torr_to == "2":
        print("Lütfen çevirmek istediğiniz Torr değerini giriniz:")
        torr_to = "cmHG"
        torr_degeri = int(input())
        sonuc = torr_degeri / 10
        torr_sonuc_kismi()
    elif torr_to == "mmHG" or torr_to == "3":
        print("Lütfen çevirmek istediğiniz Torr değerini giriniz:")
        torr_to = "mmHG"
        torr_degeri = int(input())
        sonuc = torr_degeri * 1
        torr_sonuc_kismi()
    elif torr_to == "Torr" or torr_to == "4":
        print("Lütfen çevirmek istediğiniz Torr değerini giriniz:")
        torr_to = "Torr"
        torr_degeri = int(input())
        sonuc = torr_degeri * 1
        torr_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        torr_cevirici()
        
def atm_sonuc_kismi():
    print(atm_degeri,"atm  --->  ",sonuc,atm_to)
    basinc_kismi()
    
def cmHG_sonuc_kismi():
    print(cmHG_degeri,"cmHG  --->  ",sonuc,cmHG_to)
    basinc_kismi()

def mmHG_sonuc_kismi():
    print(mmHG_degeri,"mmHG  --->  ",sonuc,mmHG_to)
    basinc_kismi()

def torr_sonuc_kismi():
    print(torr_degeri,"Torr  --->  ",sonuc,torr_to)
    basinc_kismi()


def hacim_kismi():
    global hacim_birimi
    global mililitre
    global santilitre
    global desilitre
    global litre
    global dekalitre
    global hektolitre
    global kilolitre

    slow_print("HACİM ÇEVİRİCİ\n")
    fast_print("Lütfen çevirmek istediğin hacim birimini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    hacim_birimi = input()
    if hacim_birimi == "mL" or hacim_birimi == "1":
        mililitre_cevirici()
    elif hacim_birimi == "cL" or hacim_birimi == "2":
        santilitre_cevirici()
    elif hacim_birimi == "dL" or hacim_birimi == "3":
        desilitre_cevirici()
    elif hacim_birimi == "L" or hacim_birimi == "4":
        litre_cevirici()
    elif hacim_birimi == "daL" or hacim_birimi == "5":
        dekalitre_cevirici()
    elif hacim_birimi == "hL" or hacim_birimi == "6":
        hektolitre_cevirici()
    elif hacim_birimi == "kL" or hacim_birimi == "7":
        kilolitre_cevirici()
    else:
        print("Böyle Bir Hacim Birimi Bulunmuyor!")
        hacim_kismi()
def mililitre_cevirici():
    global mL_to
    global mL_degeri
    global sonuc_hcm

    slow_print("MİLİLİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    mL_to = input()
    if mL_to == "mL" or mL_to == "1":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "mL"
        mL_degeri = int(input())
        sonuc2 = mL_degeri * 1
        mL_sonuc_kismi()
    elif mL_to == "cL" or mL_to == "2":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "cL"
        mL_degeri = int(input())
        sonuc2 = mL_degeri / 10
        mL_sonuc_kismi()
    elif mL_to == "dL" or mL_to == "3":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "dL"
        mL_degeri = int(input())
        sonuc2 = mL_degeri / 100
        mL_sonuc_kismi()
    elif mL_to == "L" or mL_to == "4":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "L"
        mL_degeri = int(input())
        sonuc2 = mL_degeri / 1000
        mL_sonuc_kismi()
    elif mL_to == "daL" or mL_to == "5":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "daL"
        mL_degeri = int(input())
        sonuc2 = mL_degeri / 10000
        mL_sonuc_kismi()
    elif mL_to == "hL" or mL_to == "6":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "hL"
        mL_degeri = int(input())
        sonuc2 = mL_degeri / 100000
        mL_sonuc_kismi()
    elif mL_to == "kL" or mL_to == "7":
        print("Lütfen çevirmek istediğin mL değerini giriniz:")
        mL_to = "kL"
        mL_degeri = int(input())
        sonuc2 = mL_degeri / 1000000
        mL_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        mililitre_cevirici()

def santilitre_cevirici():
    global cL_to
    global cL_degeri
    global sonuc2

    slow_print("SANTİLİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    cL_to = input()
    if cL_to == "mL" or cL_to == "1":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "mL"
        cL_degeri = int(input())
        sonuc2 = cL_degeri * 10
        cL_sonuc_kismi()
    elif cL_to == "cL" or cL_to == "2":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "cL"
        cL_degeri = int(input())
        sonuc2 = cL_degeri / 1
        cL_sonuc_kismi()
    elif cL_to == "dL" or cL_to == "3":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "dL"
        cL_degeri = int(input())
        sonuc2 = cL_degeri / 10
        cL_sonuc_kismi()
    elif cL_to == "L" or cL_to == "4":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "L"
        cL_degeri = int(input())
        sonuc2 = cL_degeri / 100
        cL_sonuc_kismi()
    elif cL_to == "daL" or cL_to == "5":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "daL"
        cL_degeri = int(input())
        sonuc2 = cL_degeri / 1000
        cL_sonuc_kismi()
    elif cL_to == "hL" or cL_to == "6":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "hL"
        cL_degeri = int(input())
        sonuc2 = cL_degeri / 10000
        cL_sonuc_kismi()
    elif cL_to == "kl" or cL_to == "7":
        print("Lütfen çevirmek istediğin cL değerini giriniz:")
        cL_to = "kL"
        cL_degeri = int(input())
        sonuc2 = cL_degeri / 100000
        cL_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        santilitre_cevirici()

def desilitre_cevirici():
    global dL_to
    global dL_degeri
    global sonuc2

    slow_print("DESİLİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    dL_to = input()
    if dL_to == "mL" or dL_to == "1":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "mL"
        dL_degeri = int(input())
        sonuc2 = dL_degeri * 100
        dL_sonuc_kismi()
    elif dL_to == "cL" or dL_to == "2":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "cL"
        dL_degeri = int(input())
        sonuc2 = dL_degeri * 10
        dL_sonuc_kismi()
    elif dL_to == "dL" or dL_to == "3":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "dL"
        dL_degeri = int(input())
        sonuc2 = dL_degeri / 1
        dL_sonuc_kismi()
    elif dL_to == "L" or dL_to == "4":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "L"
        dL_degeri = int(input())
        sonuc2 = dL_degeri / 10
        dL_sonuc_kismi()
    elif dL_to == "daL" or dL_to == "5":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "daL"
        dL_degeri = int(input())
        sonuc2 = dL_degeri / 100
        dL_sonuc_kismi()
    elif dL_to == "hL" or dL_to == "6":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "hL"
        dL_degeri = int(input())
        sonuc2 = dL_degeri / 1000
        dL_sonuc_kismi()
    elif dL_to == "kl" or dL_to == "7":
        print("Lütfen çevirmek istediğin dL değerini giriniz:")
        dL_to = "kL"
        dL_degeri = int(input())
        sonuc2 = dL_degeri / 10000
        dL_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        desilitre_cevirici()

def litre_cevirici():
    global L_to
    global L_degeri
    global sonuc2

    slow_print("LİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    L_to = input()
    if L_to == "mL" or L_to == "1":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "mL"
        L_degeri = int(input())
        sonuc2 = L_degeri * 1000
        L_sonuc_kismi()
    elif L_to == "cL" or L_to == "2":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "cL"
        L_degeri = int(input())
        sonuc2 = L_degeri * 100
        L_sonuc_kismi()
    elif L_to == "dL" or L_to == "3":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "dL"
        L_degeri = int(input())
        sonuc2 = L_degeri * 10
        L_sonuc_kismi()
    elif L_to == "L" or L_to == "4":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "L"
        L_degeri = int(input())
        sonuc2 = L_degeri / 1
        L_sonuc_kismi()
    elif L_to == "daL" or L_to == "5":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "daL"
        L_degeri = int(input())
        sonuc2 = L_degeri / 10
        L_sonuc_kismi()
    elif L_to == "hL" or L_to == "6":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "hL"
        L_degeri = int(input())
        sonuc2 = L_degeri / 100
        L_sonuc_kismi()
    elif L_to == "kl" or L_to == "7":
        print("Lütfen çevirmek istediğin L değerini giriniz:")
        L_to = "kL"
        L_degeri = int(input())
        sonuc2 = L_degeri / 1000
        L_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        litre_cevirici()

def dekalitre_cevirici():
    global daL_to
    global daL_degeri
    global sonuc2

    slow_print("DEKALİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    daL_to = input()
    if daL_to == "mL" or daL_to == "1":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "mL"
        daL_degeri = int(input())
        sonuc2 = daL_degeri * 10000
        daL_sonuc_kismi()
    elif daL_to == "cL" or daL_to == "2":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "cL"
        daL_degeri = int(input())
        sonuc2 = daL_degeri * 1000
        daL_sonuc_kismi()
    elif daL_to == "dL" or daL_to == "3":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "dL"
        daL_degeri = int(input())
        sonuc2 = daL_degeri * 100
        daL_sonuc_kismi()
    elif daL_to == "L" or daL_to == "4":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "L"
        daL_degeri = int(input())
        sonuc2 = daL_degeri * 10
        daL_sonuc_kismi()
    elif daL_to == "daL" or daL_to == "5":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "daL"
        daL_degeri = int(input())
        sonuc2 = daL_degeri / 1
        daL_sonuc_kismi()
    elif daL_to == "hL" or daL_to == "6":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "hL"
        daL_degeri = int(input())
        sonuc2 = daL_degeri / 10
        daL_sonuc_kismi()
    elif daL_to == "kl" or daL_to == "7":
        print("Lütfen çevirmek istediğin daL değerini giriniz:")
        daL_to = "kL"
        daL_degeri = int(input())
        sonuc2 = daL_degeri / 100
        daL_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        dekalitre_cevirici()

def hektolitre_cevirici():
    global hL_to
    global hL_degeri
    global sonuc2

    slow_print("HEKTOLİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    hL_to = input()
    if hL_to == "mL" or hL_to == "1":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "mL"
        hL_degeri = int(input())
        sonuc2 = hL_degeri * 100000
        hL_sonuc_kismi()
    elif hL_to == "cL" or hL_to == "2":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "cL"
        hL_degeri = int(input())
        sonuc2 = hL_degeri * 10000
        hL_sonuc_kismi()
    elif hL_to == "dL" or hL_to == "3":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "dL"
        hL_degeri = int(input())
        sonuc2 = hL_degeri * 1000
        hL_sonuc_kismi()
    elif hL_to == "L" or hL_to == "4":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "L"
        hL_degeri = int(input())
        sonuc2 = hL_degeri * 100
        hL_sonuc_kismi()
    elif hL_to == "daL" or hL_to == "5":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "daL"
        hL_degeri = int(input())
        sonuc2 = hL_degeri * 10
        hL_sonuc_kismi()
    elif hL_to == "hL" or hL_to == "6":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "hL"
        hL_degeri = int(input())
        sonuc2 = hL_degeri / 1
        hL_sonuc_kismi()
    elif hL_to == "kl" or hL_to == "7":
        print("Lütfen çevirmek istediğin hL değerini giriniz:")
        hL_to = "kL"
        hL_degeri = int(input())
        sonuc2 = hL_degeri / 10
        hL_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        hektolitre_cevirici()

def kilolitre_cevirici():
    global kL_to
    global kL_degeri
    global sonuc2

    slow_print("KİLOLİTRE ÇEVİRİCİ\n")
    fast_print("Lütfen hangi birime çevirmek istediğini seç.(1-mL, 2-cL, 3-dL, 4-L, 5-daL, 6-hL, 7-kL)\n")
    kL_to = input()
    if kL_to == "mL" or kL_to == "1":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "mL"
        kL_degeri = int(input())
        sonuc2 = kL_degeri * 1000000
        kL_sonuc_kismi()
    elif kL_to == "cL" or kL_to == "2":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "cL"
        kL_degeri = int(input())
        sonuc2 = kL_degeri * 100000
        kL_sonuc_kismi()
    elif kL_to == "dL" or kL_to == "3":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "dL"
        kL_degeri = int(input())
        sonuc2 = kL_degeri * 10000
        kL_sonuc_kismi()
    elif kL_to == "L" or kL_to == "4":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "L"
        kL_degeri = int(input())
        sonuc2 = kL_degeri * 1000
        kL_sonuc_kismi()
    elif kL_to == "daL" or kL_to == "5":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "daL"
        kL_degeri = int(input())
        sonuc2 = kL_degeri * 100
        kL_sonuc_kismi()
    elif kL_to == "hL" or kL_to == "6":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "hL"
        kL_degeri = int(input())
        sonuc2 = kL_degeri * 10
        kL_sonuc_kismi()
    elif kL_to == "kl" or kL_to == "7":
        print("Lütfen çevirmek istediğin kL değerini giriniz:")
        kL_to = "kL"
        kL_degeri = int(input())
        sonuc2 = kL_degeri / 1
        kL_sonuc_kismi()
    else:
        print("Lütfen Belirtilen Birimlerden Seçiniz!")
        kilolitre_cevirici()

def mL_sonuc_kismi():
    print(mL_degeri,"mL  --->  ",sonuc2,mL_to)
    hacim_kismi()
def cL_sonuc_kismi():
    print(cL_degeri,"cL  --->  ",sonuc2,cL_to)
    hacim_kismi()
def dL_sonuc_kismi():
    print(dL_degeri,"dL  --->  ",sonuc2,dL_to)
    hacim_kismi()
def L_sonuc_kismi():
    print(L_degeri,"L  --->  ",sonuc2,L_to)
    hacim_kismi()
def daL_sonuc_kismi():
    print(daL_degeri,"daL  --->  ",sonuc2,daL_to)
    hacim_kismi()
def hL_sonuc_kismi():
    print(hL_degeri,"hL  --->  ",sonuc2,hL_to)
    hacim_kismi()
def kL_sonuc_kismi():
    print(kL_degeri,"kL  --->  ",sonuc2,kL_to)
    hacim_kismi()

ana_giris()
    
