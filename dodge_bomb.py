import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = { #移動量の辞書
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,+5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(+5,0)
}

def main():
    
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900,400)

    bd_img = pg.Surface((20, 20))#練習１：爆弾surfaceをつくる
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()#１練習１：SurfaceからRectを抽出
    (x, y) =(random.randint(0,WIDTH), random.randint(0,HEIGHT)) 
    bd_rct.center = (x, y)#Rectにランダムな座標を設定する
    clock = pg.time.Clock()
    tmr = 0
    (vx, vy) = (+5, +5)#練習２　移動の値設定


    
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])

        """こうかとん"""
        key_lst = pg.key.get_pressed()
        sum_move = [0,0]
        for key,move in delta.items():
            if key_lst[key]:
                sum_move[0] += move[0] #横方向の移動値の計算
                sum_move[1] +=move[1] #縦方向の移動値の計算
        kk_rct.move_ip(sum_move[0],sum_move[1])

        screen.blit(kk_img, kk_rct)
        """爆弾"""
        screen.blit(bd_img, bd_rct) 
        bd_rct.move_ip(vx,vy)#練習２　移動おの値に応じた距離を移動し続ける
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()