import area_modulo as area

def main():
    print(area.area_tri(2, 2))
    print(area.area_ret(2, 2))
    print(area.area_qua(2))
    print(area.area_cir(2))

    print(area.area_cir.__doc__)
    print(area.area_tri.__doc__)

if __name__ == '__main__':
    main()