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




def ck_bound(obj_rct:pg.Rect):
    """
    引数：こうかとんRect　または　ばくだんRect
    戻り値：タプル（横判定結果、縦判定結果）
    画面内ならTrueで外ならFalse
    """
    yoko = True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    tate = True
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko,tate


    
def main():
    
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    
    font = pg.font.Font(None, 80)
    

    """こうかとん"""
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_end_img = pg.image.load("ex02/fig/9.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_end_img = pg.transform.rotozoom(kk_end_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900,400)
    kk_end_rct = kk_end_img.get_rect()

    kk_flip_img = pg.transform.flip(kk_img,True,False)
    kk_img2 = pg.transform.rotozoom(kk_flip_img,270,1.0)
    kk_img3 = pg.transform.rotozoom(kk_flip_img,315,1.0)
    kk_img4 = pg.transform.rotozoom(kk_flip_img,45,1.0)
    kk_img5 = pg.transform.rotozoom(kk_flip_img,90,1.0)

    kk_img6 = pg.transform.rotozoom(kk_img,315,1.0)
    kk_img7 = pg.transform.rotozoom(kk_img,45,1.0)
   
    """ばくだん"""
    bd_img = pg.Surface((20, 20))#練習１：爆弾surfaceをつくる
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()#１練習１：SurfaceからRectを抽出
    (x, y) =(random.randint(0,WIDTH), random.randint(0,HEIGHT)) 
    bd_rct.center = (x, y)#Rectにランダムな座標を設定する

    bd2_img = pg.Surface((20,20))
    bd2_img.set_colorkey((0,0,0))
    pg.draw.circle(bd2_img, (255, 0, 0), (10, 10), 10)
    bd2_rct = bd2_img.get_rect()#１練習１：SurfaceからRectを抽出
    (x, y) =(random.randint(0,WIDTH), random.randint(0,HEIGHT)) 
    bd2_rct.center = (x, y)#Rectにランダムな座標を設定する

    accs = [a for a in range(1,11)]
    bb_imgs = []
    for r in range(1,11):
        bb_img = pg.Surface((20*r,20*r))
        bd_img.set_colorkey((0, 0, 0))
        pg.draw.circle(bb_img,(255,0,0), (10*r, 10*r), 10*r)
        bb_imgs.append(bb_img)
    #avx,avy = vx*accs[min(tmr//500,9)],vy*accs[min(tmr//500,9)]
    #bb_img = bb_imgs[min(tmr//500,9)]
    
    clock = pg.time.Clock()
    tmr = 0
    (vx, vy) = (+5, +5)#練習２　移動の値設定

    kk_lst = { #追加機能１の画像と移動値のリストです
        (+5,0):kk_flip_img,
        (0,-5):kk_img5,
        (+5,-5):kk_img4,
        (+5,+5):kk_img3,
        (0,+5):kk_img2,
        (-5,-0):kk_img,
        (-5,-5):kk_img6,
        (-5,+5):kk_img7,
        (0,0):kk_img
    }

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bd_rct):
            kk_kakudo = kk_end_img
            screen.blit(kk_kakudo, kk_rct)
            print("gameover!")
            return

        screen.blit(bg_img, [0, 0])
        txt = font.render(str(tmr), True, (255, 0, 0))
        screen.blit(txt, [300, 200])

        """こうかとん"""
        key_lst = pg.key.get_pressed()
        sum_move = [0,0]
        for key,move in delta.items():
            if key_lst[key]:
                sum_move[0] += move[0] #横方向の移動値の計算
                sum_move[1] +=move[1] #縦方向の移動値の計算
        kk_kakudo = kk_lst[sum_move[0],sum_move[1]]#辞書から入力に対する画像を代入
        kk_rct.move_ip(sum_move[0],sum_move[1])

        if ck_bound(kk_rct) != (True,True):
             kk_rct.move_ip(-sum_move[0],-sum_move[1])

        screen.blit(kk_kakudo, kk_rct)#お角度にお画像を表示
        """爆弾"""
        avx,avy = vx*accs[min(tmr//500,9)],vy*accs[min(tmr//500,9)]
        bb_img = bb_imgs[min(tmr//500,9)]
        bd_rct.move_ip(vx,vy)#練習２　移動おの値に応じた距離を移動し続ける
        yoko, tate = ck_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        
        screen.blit(bb_img, bd_rct) 
        
        pg.display.update()
        tmr += 1
        clock.tick(60)
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()