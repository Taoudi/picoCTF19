import codecs

c = 3147447460729560968443913059326074795547342902824070732844279278206069336537791901313846694393748293382703273111520429311891139379610133932306810939338727377926257604163840628296622742737483090453329344989322336999157540793116859548978044126443515958685189224026895471437063920806328438426930286335822998153
n = 140297698240308373090225043783111038103162800190432255235618216058476803178553092773164096580335264228730821585372122240235942352766688012879397071562575178814954334606543529084057508763248557683961583326169735225862757738220170195901863225515894665861705427478052720964145474166468939562592365690987042719869
e = 3219673438720475351750895919096067890003461426162474813835997939361721042778031517018459820510921119367855648937236551098079822063278739816754096092743229523904371321027890944370242627516509253079427473670056388509396797345955201071135527656094792572224735134323453325702531921569264804376982542313063675905

d = 0


def bruteforce(size):
    d = 0
    while d < (1/3)*n**(1/4):
        m = (c ** d) % n
        print(hex(m))
        print(codecs.decode(hex(m), "hex"))
        print()
        d = d + 1


bruteforce(10)
