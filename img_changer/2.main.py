from personal_project.img_changer.myclass import MyImage
import argparse

P = argparse.ArgumentParser()
P.add_argument('-f', type=str)
P.add_argument('-e', type=str)
P.add_argument('-r', action='store_true')
P.add_argument('-rw', type=int, default=500)
P.add_argument('-rh', type=int, default = 500)

args = P.parse_args()

if args.f and (args.e or args.r):  # ( or ) 둘 중 하나 True
    myimg = MyImage(folder = args.f,
                    ext = args.e,
                    resize = args.r,
                    r_width = args.rw,
                    r_height = args.rh)

    cnt_resize, cnt_ext = myimg.start()
    print('resize : {},  change_format : {}'.format(cnt_resize, cnt_ext))

else:
    print("사용법 : python main.py -f <대상폴더> -e <변경될확장자>, -r [리사이즈], -rw 500 -rh 500")


