import random
import pygame,sys
import time
from pygame.math import Vector2

#*****VARIABLES*******
pygame.init()
screen_width=1300
screen_height=1730
screen=pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
#height = screen.get_height()
#width = screen.get_width()650 865
#Color RBG
yellow=(221,224,0)
green=(125, 139, 217)
black=(6,6,1)
red=(255,0,0)
white = (255,255,255)
#global image_list1
hit=False
dealer_hit=False
active=False
win=False
bust_val=False
card_move=0
card_val=False
drag=0
win_move=0
play=False
play_once=False
imgWidth = 100
imgHeight = 155
bal=2000
bet=0
#x=70
#y=124
index=52
sum_player1=0
sum_player2=0
font=pygame.font.Font('Floppy_bird/josefin-sans/JosefinSans-Bold.ttf',40)
chipslist=["Cards/1dollar.jpg","Cards/5dollar.jpg","Cards/10dollar.jpg",\
            "Cards/25dollar.jpg","Cards/50dollar.jpg","Cards/100dollar.jpg","Cards/500dollar.jpg"]
chipvalue=[1,5,10,25,50,100,500]


card_suite=[["kingH", 10, "Cards/kingH.jpg"],["kingD" ,10, "Cards/kingD.jpg"],\
        ["kingC", 10, "Cards/kingC.jpg"],["kingS", 10, "Cards/kingS.jpg"],
        ["queenH", 10, "Cards/queenH.jpg"],["queenD", 10, "Cards/queenD.jpg"],
        ["queenC", 10, "Cards/queenC.jpg"],["queenS", 10, "Cards/queenS.jpg"],
        ["jackH", 10, "Cards/jackH.jpg"],["jackD", 10, "Cards/jackD.jpg"],
        ["jackC", 10, "Cards/jackC.jpg"],["jackS", 10, "Cards/jackS.jpg"],
        ["aceH", 1, "Cards/aceH.jpg"],["aceD", 1, "Cards/aceD.jpg"],
        ["aceC", 1, "Cards/aceC.jpg"],["aceS", 1, "Cards/aceS.jpg"],
        ["diamond", 2, "Cards/twoD.jpg"],["spade", 2, "Cards/twoS.jpg"],
        ["club", 2, "Cards/twoC.jpg"],["heart", 2, "Cards/twoH.jpg"],
        ["diamond", 3, "Cards/threeD.jpg"],["spade", 3, "Cards/threeS.jpg"],
        ["club", 3, "Cards/threeC.jpg"],["heart", 3, "Cards/threeH.jpg"],
        ["diamond", 4, "Cards/fourD.jpg"],["spade", 4, "Cards/fourS.jpg"],
        ["club", 4, "Cards/fourC.jpg"],["heart", 4, "Cards/fourH.png"],
        ["diamond", 5, "Cards/fiveD.jpg"],["spade", 5, "Cards/fiveS.jpg"],
        ["club", 5, "Cards/fiveC.jpg"],["heart", 5, "Cards/fiveH.png"],
        ["diamond", 6, "Cards/sixD.jpg"],["spade", 6, "Cards/sixS.jpg"],
        ["club", 6, "Cards/sixC.jpg"],["heart", 6, "Cards/sixH.jpg"],
        ["diamond", 7, "Cards/sevenD.jpg"],["spade", 7, "Cards/sevenS.jpg"],
        ["club", 7, "Cards/sevenC.jpg"],["heart", 7, "Cards/sevenH.jpg"],
        ["diamond", 8, "Cards/eightD.jpg"],["spade", 8, "Cards/eightS.jpg"],
        ["club", 8, "Cards/eightC.jpg"],["heart", 8, "Cards/eightH.jpg"],
        ["diamond", 9, "Cards/nineD.jpg"],["spade", 9, "Cards/nineS.jpg"],
        ["club", 9, "Cards/nineC.jpg"],["heart", 9, "Cards/nineH.jpg"],
        ["diamond", 10, "Cards/tenD.jpg"],["spade", 10, "Cards/tenS.jpg"],
        ["club", 10, "Cards/tenC.jpg"],["heart", 10, "Cards/tenH.jpg"]]

aces=["aceH","aceS","aceD","aceC"]


class cardshuffle:
    
    def __init__(self,suit,number,image):        
        self.suit = suit 
        self.number = number
        self.image= image

    def background_image():
        bg_surface=pygame.image.load("Cards/redchips.jpg").convert()
        bg_surface=pygame.transform.scale2x(bg_surface)
        #bg_surface=pygame.transform.scale2x(bg_surface) 
        screen.blit(bg_surface,(0,0))

    def background_image2():
        bg_surface=pygame.image.load("Cards/tumblingchips.jpg").convert()
        bg_surface=pygame.transform.scale2x(bg_surface)
        #bg_surface=pygame.transform.scale2x(bg_surface) 
        screen.blit(bg_surface,(0,0))

    def win():
        global win, win_surface,win_move
        win=True
        win_surface=pygame.image.load("Cards/fireworks-blue.jpeg").convert()      

    def bust():
        global bust_val,bust_surface,bust_x,bust_x_move
        bust_val=True
        bust_surface=pygame.image.load("Cards/emotiguy2.jpg").convert()                  

    def message_display():        
        global message_surface,message_rect,font
        message_surface=font.render('PLAY BLACKJACK',True,(255,255,255))      
        message_rect=message_surface.get_rect(center=(488,30))
        screen.blit(message_surface,message_rect)            

    def drawRect(display,color,tuple):
        pygame.draw.rect(display,color,tuple)

    def arrow_image():
        arrow_surface=pygame.image.load("replay_buttons/play18.jpg").convert()
        screen.blit(arrow_surface,(552,685))

    def hand_image():
        hand_surface=pygame.image.load("replay_buttons/stop5.jpg").convert()
        screen.blit(hand_surface,(272,685)) 

    def restart_button():
        global image_list1
        restart_surface=pygame.image.load("replay_buttons/play8.5.jpg").convert()
        screen.blit(restart_surface,(692,685))

    def hit_button():
        hit_surface=pygame.image.load("replay_buttons/hit8.5.jpg").convert()
        screen.blit(hit_surface,(410,685))

    def move_cards():
        global card_move,remove_surface       
        remove_surface=pygame.image.load("Cards/back2.jpg").convert_alpha()
        screen.blit(remove_surface,(310,120))

    def score_count():
        global sum_player1
        #rgb(255,255,255)--white
        venetianchip=pygame.image.load("Cards/red_emptychip_black.jpg").convert_alpha()
        venetianchip_rect=venetianchip.get_rect(center=(250,250))
        screen.blit(venetianchip,venetianchip_rect)

        score_surface=font.render(str(int(sum_player1)),True,(255,255,255))
        #f'Score   :{(int(score)}'makes the whole thing into a string inc int part
        #score_surface=font.render(f'Score:{int(sum_player1)}',True,(255,255,255))
        score_rect=score_surface.get_rect(center=(250,250))
        screen.blit(score_surface,score_rect)

                 
        venetianchip2=pygame.image.load("Cards/red_emptychip_black.jpg").convert_alpha()
        venetianchip2_rect=venetianchip2.get_rect(center=(250,550))
        screen.blit(venetianchip2,venetianchip2_rect)

        score_surface2=font.render(str(int(sum_player2)),True,(255,255,255))
        #f'Score   :{(int(score)}'makes the whole thing into a string inc int part
        #score_surface2=font.render(f'Score:{int(sum_player1)}',True,(255,255,255))
        score_rect2=score_surface2.get_rect(center=(250,550))
        screen.blit(score_surface2,score_rect2)

    def new_deck():     
        w.shuffle_card_suite()

    def shuffle_card_suite():
        random.seed(random.seed(15))
        shuffled=random.shuffle(card_suite)
        

    def pot(bet):
        global bal
        bal+=bet
        bet_surface=font.render(f'POT',True,(255,255,255))
        bet_rect=bet_surface.get_rect(center=(175,130))
        screen.blit(bet_surface,bet_rect)
        card_surface3=pygame.image.load("replay_buttons/play16.jpg").convert_alpha()
        card_rect3=card_surface3.get_rect(center=(175,180))
        screen.blit(card_surface3,card_rect3)
        score_surface=font.render(str(int(bal)),True,(255,255,255))       
        score_rect=score_surface.get_rect(center=(175,180))
        screen.blit(score_surface,score_rect)

    def chips():
        bet_surface=font.render(f'BET',True,(255,255,255))
        bet_rect=bet_surface.get_rect(center=(40,130))
        screen.blit(bet_surface,bet_rect)
        for chip in range(0,len(chipslist)):           
            chiplist=pygame.image.load(chipslist[chip]).convert_alpha()
            chiplist_rect=chiplist.get_rect(center=(40,180+chip*75))
            screen.blit(chiplist,chiplist_rect)     
    def card_stack():
        for i in range(20,0,-1):
            card_surface=pygame.image.load("Cards/back_female_stack.jpg").convert_alpha()
            card_rect=card_surface.get_rect(center=(490+2*i,int(350+i*2/5)))
            screen.blit(card_surface,card_rect)
        

    def setup_display():
        global image_list1
        w=cardshuffle       
        w.background_image()
        w.message_display() 
        w.arrow_image()
        w.hand_image()
        w.restart_button()
        w.hit_button()
        w.pot(0)
        w.chips()
        #w.move_cards()
        
        card_surface=pygame.image.load("Cards/back_female.jpg").convert_alpha()
        card_rect=card_surface.get_rect(center=(360,200))
        screen.blit(card_surface,card_rect)

        card_surface1=pygame.image.load("Cards/back_female.jpg").convert_alpha()
        card_rect1=card_surface1.get_rect(center=(360+30,200))
        screen.blit(card_surface1,card_rect1)

        card_surface2=pygame.image.load("Cards/back_female.jpg").convert_alpha()
        card_rect2=card_surface2.get_rect(center=(360,500))
        screen.blit(card_surface2,card_rect2)

        card_surface3=pygame.image.load("Cards/back_female.jpg").convert_alpha()
        card_rect3=card_surface3.get_rect(center=(360+30,500))
        screen.blit(card_surface3,card_rect3)
        #remove_surface=pygame.image.load("Cards/blackrect.png").convert_alpha()
        #screen.blit(remove_surface,(440,122))
        #w.drawRect(screen,yellow,(440,122,100,155))does not work**********           

    def play_game():         
        w.draw_player1(2)
        w.draw_player2(2)

    #player1 is dealer
    def draw_player1(number_of_cards):
        global p1_index,sum_player1,image_list1,card_surface,\
               card_rect,card,index         
        image_list1=[]
        card_surface=[0]*(number_of_cards+2)
        card_rect=[0]*(number_of_cards+2)             
        sum_player1=0        
                  
        for p1_index in range (0,number_of_cards):
            print(index)
            index-=1            
            if index==0:
                index=51
                w.new_deck()
            card_surface[p1_index]=pygame.image.load(card_suite[index][2]).convert_alpha()
            card_rect[p1_index]=card_surface[p1_index].get_rect(center=(360+p1_index*30,200))
            sum_player1+=card_suite[index][1]
            image_list1.append(card_suite[index][2])
        card_surface[2]=pygame.image.load("Cards/back_female.jpg").convert_alpha()
        card_rect[2]=card_surface[2].get_rect(center=(360+30,200))
        #see if this works
        for k in range (0,p1_index+1 ):        
            screen.blit(card_surface[k],card_rect[k])
            
    #player
    def draw_player2(number_of_cards):
        global p2_index,sum_player2,image_list2,card_surface2,card_rect2,card_surface,\
               card_rect,index         
        #image_list2=[]
        card_surface2=[0]*(number_of_cards+2)
        card_rect2=[0]*(number_of_cards+2)
        sum_player2=0                          
        for p2_index in range (0,number_of_cards):
            print(index)
            index-=1
            if index==0:
                index=51
                w.new_deck()
            card_surface2[p2_index]=pygame.image.load(card_suite[index][2]).convert_alpha()
            card_rect2[p2_index]=card_surface2[p2_index].get_rect(center=\
                                (360+p2_index*30,500))           
            sum_player2+=card_suite[index][1]                
        #see if this works
        for l in range (0, p2_index+1):
            screen.blit(card_surface2[l],card_rect2[l])
        screen.blit(card_surface[2],card_rect[2])

def compare():
    global win_move,bust_x,bust_x_move
    #player1 is dealer
    #active=True   
    while sum_player2 >= sum_player1:
        #pygame.time.wait(100)
        hit_dealer()
        #pygame.time.wait(1000)
        #time.sleep(.5)
    print(sum_player1,"  compare   ",sum_player2)    
    #dealer_hit=False    
    if sum_player1 > 21:
        print("you win")
        win_move=0
        w.win()
        #if sum_player1!=0:        
    elif sum_player2 >= sum_player1 and sum_player1<=21:        
        print("you win")
        win_move=0
        w.win()
    elif sum_player1 > 21:
        print("house wins")        
        bust_x=Vector2(650,40)
        bust_x_move=Vector2(1,1)
        w.bust()
    elif sum_player1 == 21 and sum_player1 > sum_player2 :
        print("house wins")        
        bust_x=Vector2(650,40)
        bust_x_move=Vector2(1,1)
        w.bust()        
    elif sum_player1 > sum_player2 :
        print("house wins")        
        bust_x=Vector2(650,40)
        bust_x_move=Vector2(2,1)
        w.bust()
        
    w.score_count()    
    play=False
  
def uncover_card():
    global uncover_card_surface,uncover_card_rect,active    
    active=True    
    uncover_card_surface=pygame.image.load(image_list1[1]).convert_alpha()
    uncover_card_rect=uncover_card_surface.get_rect(center=(360+30,200))   
    screen.blit(uncover_card_surface,uncover_card_rect)
    compare()

d=0
dealer_card_surface=[0]*52
dealer_card_rect=[0]*52
def hit_dealer():
    global d, dealer_card_surface,dealer_card_rect,\
           dealer_hit,sum_player1,img,index        
    dealer_hit=True
    play=False
    print(index)
    index-=1
    if index==0:
        index=51
        w.new_deck()    
    sum_player1 += card_suite[index][1]
    dealer_card_surface[d]=pygame.image.load(card_suite[index][2]).convert_alpha()
    dealer_card_rect[d]=dealer_card_surface[d].get_rect(center=(420+d*35,200))
    d+=1

t=0
new_card_surface=[0]*52
new_card_rect=[0]*52
number_of_cards=0

def hit_player():
    global t, new_card_surface,new_card_rect,hit,\
           sum_player2,number_of_cards,image_list2,index,bust_x_move,bust_x        
    hit=True
    print(index)
    index-=1
    if index==0:
        index=51
        w.new_deck()
    sum_player2 += card_suite[index][1]
    print(sum_player1,"  compare   ",sum_player2)
    if sum_player2>21:
        play=False
        print("in here",bust_x)
        bust_x=Vector2(650,40)
        bust_x_move=Vector2(5,1)
        w.bust()
        print ("house wins---in hit")
    new_card_surface[t]=pygame.image.load(card_suite[index][2]).convert_alpha()    
    new_card_rect[t]=new_card_surface[t].get_rect(center=(420+t*35,500))
    t+=1
    #print(number_of_cards,"number_of_images",image_list2)
    """for i in range(i,len(image_list2)):
         new_card_surface[i]=pygame.image.load(image_list2[i]).convert_alpha()    
         new_card_rect[i]=new_card_surface[i].get_rect(center=(420+i*35,500))
         print(image_list2[i],i)"""
    play=False
w=cardshuffle
w.new_deck()
w.setup_display()

bust_x=Vector2(950,40)
bust_x_move=Vector2(5,1)

#v=bust_x+bust_x_move
#bust_x += bust_x_move
#print(bust_x[0],bust_x[1])

while True:        
    #must be placed before event    
    if win:        
        screen.blit(win_surface,(0+win_move,0))
        #screen.blit(win_surface,(0+win_move-1052,0)) 
        win_move+=2        
        if win_move>=screen_width:
            #dealer_hit=False
            #hit=False
            w.pot(bet)
            win=False            
        #if win_move>=screen_width:
            #win_move=0"""

    if bust_val:
        #print(bust_x[0],bust_x[1])
        screen.blit(bust_surface,(int(bust_x[0]),int(bust_x[1]))) 
        bust_x += bust_x_move
        if bust_x[0]>=screen_width:            
            #dealer_hit=False
            #hit=False
            w.pot(-bet)
            bust_val=False

    for event in pygame.event.get():        
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #checks if a mouse is clicked                     
        mouse = pygame.mouse.get_pos()
        mouse1 = pygame.mouse.get_pos()
        #print(mouse[0],mouse[1])
        
        if event.type == pygame.MOUSEBUTTONDOWN:                                      
            #hit
            #active is false at start.Changed to true at uncover()
            #to deactivate hit button
            if 410 <= mouse1[0] <= 523 and 685 <= mouse1[1]\
                   <= 741 and not active and play:                                 
                    hit_player()                           
          
            #play button
            if 552<=mouse[0]<=665 and  685<=mouse[1]<=741 and play_once:
                play=True
                active=False
                play_once=False
                w.play_game()

            # stand hand
            if 272<=mouse[0]<=385 and  685<=mouse[1]<=741\
               and not active and play:
                #print(sum_player1,"  just 2 dst  ",sum_player2)                
                uncover_card()
                play=False
            # restart
            if 692<=mouse[0]<=805 and  685<=mouse[1]<=741:
               play_once=True
               play=False 
               bet=0              
               sum_player1=0              
               """black_card=[0]*52
               black_card_rect=[0]*52       
               for m in range(0,d+2):             
                    black_card[m]=pygame.image.load("Cards/blackrect.png").convert_alpha()       
                    black_card_rect[m]=black_card[m].get_rect(center=(360+m*35,200))
                    screen.blit(black_card[m],black_card_rect[m])
               for p in range(0,t+2):             
                    black_card[p]=pygame.image.load("Cards/back_female_stack.jpg").convert_alpha()       
                    black_card_rect[p]=black_card[p].get_rect(center=(360+p*35,500))
                    screen.blit(black_card[p],black_card_rect[p])"""
               t=0
               d=0
               w.setup_display()
               w.card_stack()

            #value chip buttons
            for j in range (0,len(chipvalue)):   
                if 0<=mouse[0]<=80 and  145+75*j<=mouse[1]<=145+69+75*j:
                    bet+=chipvalue[j]
                    #print("chip  ",bet,len(chipvalue))
                    chiplist=pygame.image.load(chipslist[j]).convert_alpha()
                    chiplist_rect=chiplist.get_rect(center=(380,355))
                    screen.blit(chiplist,chiplist_rect)

                    black_bet =pygame.image.load("Cards/blackrectbet.png").convert_alpha()
                    black_bet_rect=black_bet.get_rect(center=(300,355))
                    screen.blit(black_bet,black_bet_rect)
            
                    bet_surface=font.render(str(int(bet)),True,(255,255,255))
                    bet_rect=bet_surface.get_rect(center=(300,355))
                    screen.blit(bet_surface,bet_rect)
                        
    if hit:
        for m in range(0,t):
            screen.blit(new_card_surface[m],new_card_rect[m])        
        hit=False   
 
    if dealer_hit :
        for n in range(0,d):
            screen.blit(dealer_card_surface[n],dealer_card_rect[n])           
        dealer_hit=False                         
                    
    pygame.display.update()
    clock.tick(120) #120 frames/sec
