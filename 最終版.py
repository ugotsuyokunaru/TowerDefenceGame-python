# -*- coding: utf-8 -*-
#使用unicode編碼
import pygame		   # 載入 pygame 模組
import os
import sys

#初始參數設定
grayroad = (100,100,100)	#道路顏色(淺灰)
blackboard = (40,40,40)	 	#操作面板顏色
coincolor = (230, 200, 0)   #金幣顏色
brick = (148, 20, 20)	  	#磚塊(不可放置塔區域)顏色
roundcolor = (0, 255, 255)  #第幾波字樣顏色
bloodcolor = (220, 20, 60)  #血條顏色
white = (248, 248, 255)	 	#白色
blue = (106,90,205)		 	#藍色
coins = 400				 	#初始金幣金額
Tower_brush_price = 50	  	#牙刷塔價錢
Tower_toothpaste_price = 100#牙膏塔價錢
Tower_mouthwash_price = 170 #漱口水塔價錢
rounds = 1				 	#初始為第1波
toothblood = 120			#牙齒血量
sb = 0					  	#總扣血
attack_tooth = False		#怪物攻擊牙齒的判定變數
tooth_dead = False		  	#牙齒生存狀態0時生存
decay = False			   	#牙齒是否已黑判定
be_delay = 0				#結局延遲控制
clean = False			   	#遊戲結束並勝利
nomoney = False			 	#沒錢買塔時的判定
cannot_locate1 = False	  	#拉塔1放到不可放置位置的判定
cannot_locate2 = False	  	#拉塔2放到不可放置位置的判定
cannot_locate3 = False	  	#拉塔3放到不可放置位置的判定
hint1 = False			   	#因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數
hint2 = False			   	#因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數
hint3 = False			   	#因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數

tower1_center = []		  	#紀錄牙刷塔的左上角座標
# 放下去之後，往左移40
tower1_left_center = []		  	#紀錄漱口水塔的左上角座標
tower1_left_range = 60		  	#塔1的攻擊範圍(以塔3視覺中心點為圓心，半徑=100)
tower1_left_r_whole = 40
tower1_left_r_adjust = 20
tower1_left_attack_power = 10	#塔1的攻擊力(每段時間內可使怪物損多少血)
tower1_left_adjust_left = 40	#向左打牙刷塔專用，放下去之後，往左移40

# 跟放下去時tower1_center，同樣座標(但動畫要用，另外開一個list，數量跟tower1_center不一定同)
tower1_right_center = []		#紀錄漱口水塔的左上角座標
tower1_right_range = 60		  	#塔1的攻擊範圍(以塔3視覺中心點為圓心，半徑=100)
tower1_right_r_whole = 40
tower1_right_r_adjust = 20
tower1_right_attack_power = 10	#塔1的攻擊力(每段時間內可使怪物損多少血)
tower1_right_adjust_left = 0	# 向左打牙刷塔專用，此用不到，設為0

tower2_center = []		 		#紀錄牙膏塔的左上角座標
tower2_range = 90		   		#塔2的攻擊範圍(以塔2視覺中心點為圓心，半徑=90)
tower2_r_whole = 40
tower2_r_adjust = 20
tower2_attack_power = 1	 		#塔2的攻擊力(每段時間內可使怪物損多少血)
tower2_adjust_left = 0			# 向左打牙刷塔專用，此用不到，設為0

tower3_center = []		  	#紀錄漱口水塔的左上角座標
tower3_range = 100		  	#塔3的攻擊範圍(以塔3視覺中心點為圓心，半徑=100)
tower3_r_whole = 50
tower3_r_adjust = 10
tower3_attack_power = 2	 	#塔3的攻擊力(每段時間內可使怪物損多少血)
tower3_adjust_left = 0		# 向左打牙刷塔專用，此用不到，設為0

snowballs = []				#所有牙膏球的發射起點座標
snowballs_move = []	 		#所有牙膏球的移動距離
waterballs = []		 		#所有水球的發射起點座標
waterballs_move = []		#所有水球的移動距離
road_center = []			#道路中心座標list
mindistance_road_to_tower = 1000000000  #道路到塔視覺中心最短距離
mindistance_x = int()	   	#道路到塔視覺中心最短距離之x座標
tower1_left = []			#道路左側防禦塔list
tower1_right = []	   		#道路右側防禦塔list
add = 0 					#牙刷塔放置用
brush1_list = [] 			#牙刷塔動畫用
brush2_list = [] 			#牙刷塔動畫用
#建置道路中心座標
for h in range(0,171):
	road_center.append([70,h])
for h in range(1,150-70+1):
	road_center.append([70+h,170])
for h in range(1,450-170+1):
	road_center.append([150,170+h])
for h in range(1,150-70+1):
	road_center.append([150-h,450]) 
for h in range(1,590-450+1):
	road_center.append([70,450+h])
for h in range(1,370-70+1):
	road_center.append([70+h,590])  
for h in range(1,590-450+1):
	road_center.append([370,590-h])
for h in range(1,370-290+1):
	road_center.append([370-h,450]) 
for h in range(1,450-230+1):
	road_center.append([290,450-h])
for h in range(1,390-290+1):
	road_center.append([290+h,230]) 
for h in range(1,230-110+1):
	road_center.append([390,230-h])
for h in range(1,730-390+1):
	road_center.append([390+h,110]) 
for h in range(1,330-110+1):
	road_center.append([730,110+h])   
for h in range(1,730-590+1):
	road_center.append([730-h,330]) 
for h in range(1,550-330+1):
	road_center.append([590,330+h])
for h in range(1,810-590+1):
	road_center.append([590+h,550]) 		#道路中心座標list  建立完成
	
pygame.init()
font = pygame.font.get_fonts() 				#pygame可用字體列表 
usefont = pygame.font.SysFont('simhei',25)	#設定使用字體，大小25，可用字體為'simhei'，'yumincho'，68最佳，70，72[標楷體]
# 載入牙齒、牙刷等圖片
brush_image_filename = "./resources/brush修正.png"
brushesleft_image_filename = "./resources/brushes left.png"
brushesright_image_filename = "./resources/brushes right.png"
toothpaste_image_filename = "./resources/牙膏0.png"
tooth_image_filename = "./resources/牙齒0拷貝.png"
teeth_image_filename = "./resources/teeth.png"
mouthwash_image_filename = "./resources/漱口水.png"
snowball_image_filename = "./resources/牙膏.png"
waterball_image_filename = "./resources/漱口水滴.png"
sheep_image_filename = "./resources/sheeptest.png"
bat_image_filename = "./resources/bats.png"
pumpkin_image_filename = "./resources/testpumpkin.png"
brush_image2_filename = "./resources/brush不能放置修正.png"
toothpaste_image2_filename = "./resources/牙膏不能放置.png"
mouthwash_image2_filename = "./resources/漱口水不能放置.png"
background_image_filename = "./resources/background.png"
start_image_filename = "./resources/開始畫面更新.png"
happy_ending_image_filename = "./resources/he.png"
bad_ending_image_filename = "./resources/be.png"
befont_image_filename = "./resources/be標題.png"
hefont_image_filename = "./resources/he標題.png"
begin_image_filename = "./resources/start.png"
halloween_music_filename = "./resources/FGO萬聖節.mp3"
he_music_filename = "./resources/安眠曲.mp3"
be_music_filename = "./resources/電鑽聲.mp3"

#################################################
time_passed = 0					# 遊戲經過時間
clock = pygame.time.Clock()		# Clock对象，後續使用time_passed += clock.tick()取得已經過時間

def addsnowball(list,a):#定義牙膏球分布位置(塔四角) # list固定放snowballs，a放每個塔的位置
	list.append((a[0]-10,a[1]+10))#(x,y+10)
	list.append((a[0]+60,a[1]+10))#(x+60,y+10)
	list.append((a[0]+60,a[1]+80))#(x+60,y+80)
	list.append((a[0]-10,a[1]+80))#(x,y+80)
	
def addwaterball(list,w):#定義水球分布位置(八個球)
	list.append((w[0]-18,w[1]+3))#(x-9,y)
	list.append((w[0]+65,w[1]+3))#(x+80,y)
	list.append((w[0]+23,w[1]+3))#(x+40,y)
	list.append((w[0]+65,w[1]+43))#(x+80,y+60)
	list.append((w[0]-18,w[1]+43))#(x=9,y+60)	
	list.append((w[0]+65,w[1]+83))#(x+80,y+90)
	list.append((w[0]+23,w[1]+83))#(x+40,y+90)
	list.append((w[0]-18,w[1]+83))#(x-9,y+100)

def addbrush(leftright,towerlist,image,screen,group):#left or right list,brush1_list,brushesleft_image_filename,self.screen,self.animation_group
	k = []
	n = len(leftright)
	for o in range(n):
		k.append(Animation_brush ( screen ))
		k[o].load( image, 80, 80, 12 , leftright[o][0] , leftright[o][1])
		k[o].idle = 0
		group.add(k[o])
		towerlist.append(k[o])
	
def distance(n,m):#取得兩點間距離(n in list of tower,locations of monsters)
	x = n[0]
	y = n[1]
	a = m[0]
	b = m[1]
	d2 = (x - a)**2 + (y - b)**2
	dist = d2**(1/2)
	return dist
	
step = 1 #怪物初始速度 可以調整為1、2、5、10、20
speed = [0, step] #一開始往y軸移動
#################################################
# 所有怪物
class Animation_Monster(pygame.sprite.Sprite):
		def __init__(self, target):
				pygame.sprite.Sprite.__init__(self)
				self.target_surface = target
				self.master_image = None
				self.image = None
				self.rect = None
				self.topleft = 0,0
				self.frame = 0
				self.old_frame = -1
				self.frame_width = 1
				self.frame_height = 1
				self.first_frame = 0
				self.last_frame = 0
				self.columns = 1
				self.last_time = 0
				#### NEW ADD ######################
				self.width = 0
				self.height = 0
				self.x = 0
				self.y = 0
				self.step = 0
				self.move_x = 0
				self.move_y = 0
				self.health = 0
				self.dead = False
				self.money = 0
				self.monster_power = 0
		def load(self, filename, width, height, columns, x, y, step, health, money, monster_power):
				self.master_image = pygame.image.load(filename).convert_alpha()
				self.width = width
				self.height = height
				self.columns = columns
				self.x = x
				self.y = y
				self.step = step
				self.move_y = step
				self.health = health
				self.money = money
				self.monster_power = monster_power
		def run(self):
				global sb, attack_tooth
				a = False # 攻擊到牙齒的話 = True
				
				self.x += self.move_x
				self.y += self.move_y
				if decay != True:
					if self.x == 40 and self.y == 135:
							self.move_x = self.step
							self.move_y = 0
					elif self.x == 115 and self.y == 135:
							self.move_x = 0
							self.move_y = self.step
					elif self.x == 115 and self.y == 420:
							self.move_x = -self.step
							self.move_y = 0
					elif self.x == 40 and self.y == 420:
							self.move_x = 0
							self.move_y = self.step
					elif self.x == 40 and self.y == 555:
							self.move_x = self.step
							self.move_y = 0
					elif self.x == 340 and self.y == 555:
							self.move_x = 0
							self.move_y = -self.step
					elif self.x == 340 and self.y == 420:
							self.move_x = -self.step
							self.move_y = 0
					elif self.x == 265 and self.y == 420:
							self.move_x = 0
							self.move_y = -self.step
					elif self.x == 265 and self.y == 195:
							self.move_x = self.step
							self.move_y = 0
					elif self.x == 355 and self.y == 195:
							self.move_x = 0
							self.move_y = -self.step
					elif self.x == 355 and self.y == 75:
							self.move_x = self.step
							self.move_y = 0
					elif self.x == 700 and self.y == 75:
							self.move_x = 0
							self.move_y = self.step
					elif self.x == 700 and self.y == 300:
							self.move_x = -self.step
							self.move_y = 0
					elif self.x == 565 and self.y == 300:
							self.move_x = 0
							self.move_y = self.step
					elif self.x == 565 and self.y == 525:
							self.move_x = self.step
							self.move_y = 0
					elif self.x == 880 and self.y == 525:
							self.move_x = 0
							self.move_y = 0
							self.x == 40
							self.y == 0
							sb += self.monster_power		#(總共120滴血)
							self.x = 10000
							self.y = 10000
							# self.health = 0
							a = True
							attack_tooth = a # 綿羊攻擊到牙齒，0變1，觸發動畫的變數
					self.frame_width = self.width
					self.frame_height = self.height
					self.rect = self.x, self.y, self.width, self.height
					rect = self.master_image.get_rect()
					self.last_frame = (rect.width // self.width) * (rect.height // self.height) - 1
				
				
		def draw(self, screen):
			global be_delay
			if be_delay <= 100:
				screen.blit(self, self.rect)
		def update(self, current_time, rate=60):
				if current_time > self.last_time + rate:
					self.frame += 1
					if self.frame > self.last_frame:
						self.frame = self.first_frame
					self.last_time = current_time
				if self.frame != self.old_frame:
					frame_x = (self.frame % self.columns) * self.frame_width
					frame_y = (self.frame // self.columns) * self.frame_height
					rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
					self.image = self.master_image.subsurface(rect)
					self.old_frame = self.frame
		def delete(self,list,di,r_whole,r_adjust,attack_power,r_adjust_left):	# r_adjust_left 專門給向左牙刷塔用的
					#towers lists,tower range(塔中心點開始算 的攻擊半徑),tower_r_whole,tower_r_adjust(調成視覺上中心用)
			global coins 
			for ni in list:
				dis = distance( (ni[0] + r_whole - r_adjust - r_adjust_left , ni[1] + r_whole + r_adjust ) , ( self.x+30 , self.y+30 ) )
				# r_adjust_left 專門給向左牙刷塔用的
				if dis >= di:
					self.health -= 0
				else:
					self.health -= attack_power
				if self.health <= 0 and self.dead == False:
					coins += self.money
					self.x = 10000
					self.y = 10000
					self.dead = True

# 定義動畫功能
class Animation(pygame.sprite.Sprite):
	#動畫(動圖)的基本設定
	def __init__( self, target ):
		#初始設定
		pygame.sprite.Sprite.__init__(self)
		self.target_surface = target
		self.image = None
		self.master_image = None
		self.rect = None
		self.topleft = 0,0
		self.frame = 0 #目前在哪一張圖(編號)
		self.old_frame = -1
		self.frame_width = 1
		self.frame_height = 1
		self.first_frame = 0 #開始圖的編號
		self.last_frame = 0 #結束圖的編號
		self.columns = 1 #一橫排有幾張圖
		self.last_time = 0 #已經過的時間
		self.state_mode = 0 #0=靜止發呆 ; 1=動畫中
		self.run_mode = 0 #跑圖順序不同: 0 = fisrt→last 單趟 ; 1/-1 = first→last→first 來回
	def load( self , filename , width , height , columns , x , y ): #依序輸入檔案、小圖長、小圖寬、一排小圖張數、放置的xy座標
		#讀進來的設定
		self.master_image = pygame.image.load( filename ).convert_alpha() #讀檔
		self.frame_width = width #小長
		self.frame_height = height #小寬
		self.rect = x , y , width , height #放的位置
		self.columns = columns #一橫排有幾張圖
		rect = self.master_image.get_rect()
		
	def update( self, current_time, rate = 60 ): #rate是換圖速度，後面每張動畫重新輸入不同的rate
		#跑圖
		#由左至右、由上至下
		#會在主程式的迴圈內用group執行這部分
		if current_time > self.last_time + rate: #時間判斷，是否該換圖了
			if self.run_mode == 0: #fisrt→last
				self.frame += 1 #換下一張編號
				if self.frame > self.last_frame: #跑超過最後一張編號=動畫結束
					self.state_mode = 0
			else : #first→last→first
				if self.run_mode == 1: #正跑
					self.frame += 1
			
					
					if self.frame > self.last_frame: #跑超過最後一張=該折返了
						self.frame = self.last_frame - 1
						self.run_mode = -1
				elif self.run_mode == -1: #逆跑
					self.frame -= 1
				
					if self.frame < self.first_frame: #跑超過第一張=動畫結束
						self.run_mode = 0
						self.state_mode = 0
			self.last_time = current_time #時間基準換成現在
			
		if self.state_mode == 0: #靜止發呆模式
			self.frame = self.idle
			
		if self.frame != self.old_frame: #剛剛是否有換過圖的編號，有則換圖
			frame_x = (self.frame % self.columns) * self.frame_width 
			frame_y = (self.frame // self.columns) * self.frame_height 
			rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
			self.image = self.master_image.subsurface(rect)
			self.old_frame = self.frame

# 塔1:牙刷塔
class Tower_brush(object):
	def __init__(self , pos):
		self.image = pygame.image.load(brush_image_filename).convert_alpha()# 底座:40x40 / 全圖:80x80 / pos:中間下面 #底座位置:數值算好後y要-40
		self.screen = pygame.display.get_surface() # Get reference to the display.
		self.rect = self.image.get_rect()   # 紀錄( x座標 , y座標 , 寬 , 高 ) 四項資訊，x,y座標是起始點(左上角)座標，type() = pygame.Rect
		
		self.rect.center = pos # pos 是塔的中心位置，type() = tuple
		
		self.image2 = pygame.image.load(brush_image2_filename).convert_alpha()
		self.located = False
		self.click = False
		self.clickup = False
		self.animation_group = pygame.sprite.Group()
	def check_click(self, pos): # 檢查滑鼠按下去，有沒有事件要發生 (且要還沒located 按下去才有用)
		global nomoney
		if self.rect.collidepoint(pos) and coins >= Tower_brush_price and self.located == False:
			self.click = True
			pygame.mouse.get_rel()
		# 若錢不夠買塔時
		elif self.rect.collidepoint(pos) and coins < Tower_brush_price and self.located == False: 
			nomoney = True
	def update(self, screen_rect):
		if self.click:
			self.rect.move_ip(pygame.mouse.get_rel())
			self.rect.clamp_ip(screen_rect)
	def draw(self, surface):
		global coins, cannot_locate1, tower1_center, tower2_center, tower3_center, hint1, mindistance_road_to_tower, mindistance_x, tower1_left, brush_test , add
		if self.rect[0] <= 820-40+1 and self.rect[1] >= 0-1:   #因為是center當作起點座標，不是左上角
			
			if self.located == False:   # 因為不管已放置與否，會一直draw，所以只要判定還沒放置好的塔就行
				# 判定是否在道路內
				counter = len(road_center)+len(tower1_center)+len(tower2_center)+len(tower3_center)
				for i in range(len(road_center)):
					if (	(road_center[i][0]-30 <= self.rect[0]+1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+40+1 <= road_center[i][1]+30)  	#塔左上角
						or  (road_center[i][0]-30 <= self.rect[0]+40-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+40+1 <= road_center[i][1]+30)   #塔右上角
						or  (road_center[i][0]-30 <= self.rect[0]+1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+80-1 <= road_center[i][1]+30)  	#塔左下角
						or  (road_center[i][0]-30 <= self.rect[0]+40-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+80-1 <= road_center[i][1]+30)   #塔右下角
						or  (road_center[i][0]-30 <= self.rect[0]+20-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+40+20-1 <= road_center[i][1]+30)#塔視覺中心
					):				  
						counter -= 1
				
				# if有1個以上座塔1，判定是否與已放置的塔1重疊
				if len(tower1_center) > 0:
					for i in range(len(tower1_center)):
						if (	(tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+40+1 <= tower1_center[i][1]+60+20)  	#塔左上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+40-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+40+1 <= tower1_center[i][1]+60+20)   #塔右上角
							or  (tower1_center[i] [0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1 <= tower1_center[i][1]+60+20)  	#塔左下角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+40-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1 <= tower1_center[i][1]+60+20)   #塔右下角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+20-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+40+20-1 <= tower1_center[i][1]+60+20)#塔視覺中心
						
							or	(tower1_center[i][0]+20-20 <= self.rect[0]+1+20 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+40+1 <= tower1_center[i][1]+60+20)  	#上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+40-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+40+1+20 <= tower1_center[i][1]+60+20)#右角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1-20 <= tower1_center[i][1]+60+20)  	#左角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+40-1-20 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1 <= tower1_center[i][1]+60+20)#下角
						):				  
							counter -= 1
				# if有1個以上座塔2，判定是否與已放置的塔2重疊
				if len(tower2_center) > 0:
					for i in range(len(tower2_center)):
						if (	(tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+40+1 <= tower2_center[i][1]+50+30)  	#塔左上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+40-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+40+1 <= tower2_center[i][1]+50+30)   #塔右上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1 <= tower2_center[i][1]+50+30)  	#塔左下角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+40-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1 <= tower2_center[i][1]+50+30)   #塔右下角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+20-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+40+20-1 <= tower2_center[i][1]+50+30)#塔視覺中心
						
							or	(tower2_center[i][0]+30-30 <= self.rect[0]+1+20 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+40+1 <= tower2_center[i][1]+50+30)  	#上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+40-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+40+1+20 <= tower2_center[i][1]+50+30)#右角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1-20 <= tower2_center[i][1]+50+30)  	#左角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+40-1-20 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1 <= tower2_center[i][1]+50+30)#下角
						):				  
							counter -= 1
				# if有1個以上座塔3，判定是否與已放置的塔3重疊
				if len(tower3_center) > 0:
					for i in range(len(tower3_center)):
						if (	(tower3_center[i][0]+40-40-10 <= self.rect[0]+1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+40+1 <= tower3_center[i][1]+60+40-10)  	#塔左上角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+40-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+40+1 <= tower3_center[i][1]+60+40-10)   #塔右上角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+80-1 <= tower3_center[i][1]+60+40-10)  	#塔左下角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+40-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+80-1 <= tower3_center[i][1]+60+40-10)   #塔右下角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+20-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+40+20-1 <= tower3_center[i][1]+60+40-10)#塔視覺中心
						):				  
							counter -= 1
				
				# 若在道路內或重疊其他塔，不可放置，顯示紅色圖案
				if counter != len(road_center)+len(tower1_center)+len(tower2_center)+len(tower3_center):			
					surface.blit(Tower_brush(pygame.mouse.get_rel()).image2 , self.rect)
					if self.click == False and self.clickup == False:   # 若在道路上放開滑鼠，讓塔仍能拉動，但要放置完成，才可再放新塔
						self.located = False
						cannot_locate2 = True
					
				# 若不在道路內，若放開滑鼠即完成放置
				else:
					cannot_locate2 = False  # 已放置到正確位置，"無法放置"的提示文字可消失
					
					# pygame.mouse.get_rel() 為滑鼠移動量( x , y )，不是絕對位置座標，型態為 tuple 
					# blit( 要blit的東西 , 位置座標(左上角起始) )
					""" 在目前image所在位置get_rect()，
						在這個範圍內(  而非整個surface，所以滑鼠不動時get_rel()=(0,0)，但是這範圍內的左上角(0,0)，非全畫面的左上角(0,0)  )
						持續blit牙刷塔圖像，不管滑鼠是否click，是否在移動 """
					surface.blit( Tower_brush(pygame.mouse.get_rel()).image , self.rect )
					
					if self.click == False and self.clickup == False:
						tower1_center.append(  ( list(self.rect.center)[0]-40 , list(self.rect.center)[1]-40 )  ) 
							# 紀錄新append上去的塔的整張image的左上角座標( 由中心點座標(tuple)轉換 )
						self.located = True	 # 已放置到正確位置，不可再移動
						hint1 = True	#因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數
						self.clickup = True # 已放開滑鼠，位置確定後，讓塔的位置不會記錄第二次
						coins -= Tower_brush_price  #扣錢
						
						#if len ( tower1_center ) == 1 :
							#A = brush_test
						
						# 啟動攻擊動畫
						for i in range(0, len(road_center)):
							distance_road_to_tower = distance(road_center[i],(self.rect[0]+20,self.rect[1]+60))
							distance_x = road_center[i][0]
							if distance_road_to_tower < mindistance_road_to_tower and self.rect[1]+60 == road_center[i][1]:
								mindistance_road_to_tower = distance_road_to_tower
								mindistance_x = distance_x
						if mindistance_x >= self.rect[0]+20:
							#brush_test.idle = 0
							tower1_left.append([self.rect[0], self.rect[1]])
							add = 1
						if mindistance_x < self.rect[0]+20:
							#brush_test.idle = 12
							tower1_right.append([self.rect[0]-40, self.rect[1]])
							add = 2
						
						mindistance_road_to_tower = 1000000000
						mindistance_x = int()
						
			elif self.located == True:  # 塔已放置好，只要一直draw就行
				#surface.blit(Tower_brush(pygame.mouse.get_rel()).image , self.rect)
				add = 0
			   			
# 塔2:牙膏塔
class Tower_toothpaste(object):
	def __init__(self , pos):
		self.image = pygame.image.load(toothpaste_image_filename).convert_alpha()# 底座:60x60/全圖:80x80/pos:靠左 #底座起點:數值算好後y-20
		self.screen = pygame.display.get_surface() # Get reference to the display.
		self.rect = self.image.get_rect()   # 紀錄( x座標 , y座標 , 寬 , 高 ) 四項資訊，x,y座標是起始點(左上角)座標，type() = pygame.Rect
		
		self.rect.center = pos # pos 是塔的中心位置
		
		self.image2 = pygame.image.load(toothpaste_image2_filename).convert_alpha()
		self.located = False
		self.click = False
		self.clickup = False
	def check_click(self, pos): # 檢查滑鼠按下去，有沒有事件要發生 (且要還沒located 按下去才有用)
		global nomoney
		if self.rect.collidepoint(pos) and coins >= Tower_toothpaste_price and self.located == False:
			self.click = True
			pygame.mouse.get_rel()
		# 若錢不夠買塔時
		elif self.rect.collidepoint(pos) and coins < Tower_toothpaste_price and self.located == False: 
			nomoney = True
	def update(self, screen_rect):
		if self.click:
			self.rect.move_ip(pygame.mouse.get_rel())
			self.rect.clamp_ip(screen_rect)
	def draw(self, surface):
		global coins, cannot_locate2, tower1_center, tower2_center, tower3_center, hint2
		if self.rect[0] <= 820-60 and self.rect[1] >= 20-1:   #因為是center當作起點座標，不是左上角
			
			if self.located == False:   # 因為不管已放置與否，會一直draw，所以只要判定還沒放置好的塔就行
				# 判定是否在道路內
				counter = len(road_center)+len(tower1_center)+len(tower2_center)+len(tower3_center)
				for i in range(len(road_center)):
					if (	(road_center[i][0]-30 <= self.rect[0]+1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+20+1 <= road_center[i][1]+30)  	#塔左上角
						or  (road_center[i][0]-30 <= self.rect[0]+60-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+20+1 <= road_center[i][1]+30)   #塔右上角
						or  (road_center[i][0]-30 <= self.rect[0]+1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+80-1 <= road_center[i][1]+30) 	 	#塔左下角
						or  (road_center[i][0]-30 <= self.rect[0]+60-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+80-1 <= road_center[i][1]+30)   #塔右下角
						or  (road_center[i][0]-30 <= self.rect[0]+30-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+30+20-1 <= road_center[i][1]+30)#塔視覺中心
					):				  
						counter -= 1
				
				# if有1個以上座塔1，判定是否與已放置的塔1重疊
				if len(tower1_center) > 0:
					for i in range(len(tower1_center)):
						if (	(tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1 <= tower1_center[i][1]+60+20)  	#塔左上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+60-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1 <= tower1_center[i][1]+60+20)   #塔右上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1 <= tower1_center[i][1]+60+20)  	#塔左下角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+60-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1 <= tower1_center[i][1]+60+20)   #塔右下角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+30-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+30+20-1 <= tower1_center[i][1]+60+20)#塔視覺中心
						
							or	(tower1_center[i][0]+20-20 <= self.rect[0]+1+20 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1 <= tower1_center[i][1]+60+20)  	#上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+60-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1+20 <= tower1_center[i][1]+60+20)#右角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1-20 <= tower1_center[i][1]+60+20)  	#左角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+60-1-20 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+80-1 <= tower1_center[i][1]+60+20)#下角
						):				  
							counter -= 1
				# if有1個以上座塔2，判定是否與已放置的塔2重疊
				if len(tower2_center) > 0:
					for i in range(len(tower2_center)):
						if (	(tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1 <= tower2_center[i][1]+50+30)  	#塔左上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+60-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1 <= tower2_center[i][1]+50+30)   #塔右上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1 <= tower2_center[i][1]+50+30) 	 	#塔左下角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+60-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1 <= tower2_center[i][1]+50+30)   #塔右下角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+30-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+30+20-1 <= tower2_center[i][1]+50+30)#塔視覺中心
							
							or	(tower2_center[i][0]+30-30 <= self.rect[0]+1+20 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1 <= tower2_center[i][1]+50+30)  	#上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+60-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1+20 <= tower2_center[i][1]+50+30)#右角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1-20 <= tower2_center[i][1]+50+30)  	#左角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+60-1-20 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+80-1 <= tower2_center[i][1]+50+30)#下角
						):				  	
							counter -= 1
				# if有1個以上座塔3，判定是否與已放置的塔3重疊
				if len(tower3_center) > 0:
					for i in range(len(tower3_center)):
						if (	(tower3_center[i][0]+40-40-10 <= self.rect[0]+1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+20+1 <= tower3_center[i][1]+60+40-10)  	#塔左上角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+60-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+20+1 <= tower3_center[i][1]+60+40-10)   #塔右上角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+80-1 <= tower3_center[i][1]+60+40-10)  	#塔左下角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+60-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+80-1 <= tower3_center[i][1]+60+40-10)   #塔右下角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+30-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+30+20-1 <= tower3_center[i][1]+60+40-10)#塔視覺中心
						):				  
							counter -= 1
				
				# 若在道路內或重疊其他塔，不可放置，顯示紅色圖案
				if counter != len(road_center)+len(tower1_center)+len(tower2_center)+len(tower3_center):			
					surface.blit(Tower_toothpaste(pygame.mouse.get_rel()).image2 , self.rect)
					if self.click == False and self.clickup == False:   # 若在道路上放開滑鼠，讓塔仍能拉動，但要放置完成，才可再放新塔
						self.located = False
						cannot_locate2 = True
					
				# 若不在道路內，若放開滑鼠，即完成放置
				else:   
					cannot_locate2 = False  # 已放置到正確位置，"無法放置"的提示文字可消失
					""" 在目前image所在位置get_rect()，
						在這個範圍內(  而非整個surface，所以滑鼠不動時get_rel()=(0,0)，但是這範圍內的左上角(0,0)，非全畫面的左上角(0,0)  )
						持續blit牙刷塔圖像，不管滑鼠是否click，是否在移動 """
					surface.blit(Tower_toothpaste(pygame.mouse.get_rel()).image , self.rect)
					
					if self.click == False and self.clickup == False:
						self.located = True	 # 已放置到正確位置，不可再移動
						tower2_center.append(  ( list(self.rect.center)[0]-40 , list(self.rect.center)[1]-40 )  ) 
							# 紀錄新append上去的塔的整張image的左上角座標( 由中心點座標(tuple)轉換 )
						self.clickup = True # 已放開滑鼠，位置確定後，讓塔的位置不會記錄第二次
						hint2 = True	#因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數
						coins -= Tower_toothpaste_price #扣錢
						addsnowball(snowballs,tower2_center[len(tower2_center)-1])  #啟動攻擊動畫 
						while len(snowballs) != len(snowballs_move):
							snowballs_move.append([0,0])
			elif self.located == True:  # 塔已放置好，只要一直draw就行
				surface.blit(Tower_toothpaste(pygame.mouse.get_rel()).image , self.rect)
								
# 塔3:漱口水塔
class Tower_mouthwash(object):
	def __init__(self , pos):
		self.image2 = pygame.image.load(mouthwash_image2_filename).convert_alpha()
		self.image = pygame.image.load(mouthwash_image_filename).convert_alpha()# 底座:80x80/全圖:100x100/pos:靠左  #底座起點:數值算好後y-20
		self.screen = pygame.display.get_surface() # Get reference to the display.
		self.rect = self.image.get_rect()   # 紀錄( x座標 , y座標 , 寬 , 高 ) 四項資訊，x,y座標是起始點(左上角)座標，type() = pygame.Rect
		
		self.rect.center = pos # pos 是塔的中心位置
		
		self.located = False
		self.click = False
		self.clickup = False
	def check_click(self, pos): # 檢查滑鼠按下去，有沒有事件要發生 (且要還沒located 按下去才有用)
		global nomoney
		if self.rect.collidepoint(pos) and coins >= Tower_mouthwash_price and self.located == False:
			self.click = True
			pygame.mouse.get_rel()
		# 若錢不夠買塔時
		elif self.rect.collidepoint(pos) and coins < Tower_mouthwash_price and self.located == False: 
			nomoney = True
	def update(self, screen_rect):
		if self.click:
			self.rect.move_ip(pygame.mouse.get_rel())
			self.rect.clamp_ip(screen_rect)
	def draw(self, surface):
		global coins, cannot_locate3, tower1_center, tower2_center, tower3_center, hint3
		if self.rect[0] <= 820-80 and self.rect[1] >= 20-1:   #因為是center當作起點座標，不是左上角
			
			if self.located == False:   # 因為不管已放置與否，會一直draw，所以只要判定還沒放置好的塔就行
				# 判定是否在道路內
				counter = len(road_center)+len(tower1_center)+len(tower2_center)+len(tower3_center)
				for i in range(len(road_center)):
					if (	(road_center[i][0]-30 <= self.rect[0]+1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+20+1 <= road_center[i][1]+30)  	#塔左上角
						or  (road_center[i][0]-30 <= self.rect[0]+80-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+20+1 <= road_center[i][1]+30)   #塔右上角
						or  (road_center[i][0]-30 <= self.rect[0]+1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+100-1 <= road_center[i][1]+30) 	#塔左下角
						or  (road_center[i][0]-30 <= self.rect[0]+80-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+100-1 <= road_center[i][1]+30)  #塔右下角
						or  (road_center[i][0]-30 <= self.rect[0]+40-1 <= road_center[i][0]+30 and road_center[i][1]-30 <= self.rect[1]+40+20-1 <= road_center[i][1]+30)#塔視覺中心
					):
						counter -= 1
				
				# if有1個以上座塔1，判定是否與已放置的塔1重疊
				if len(tower1_center) > 0:
					for i in range(len(tower1_center)):
						if (	(tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1 <= tower1_center[i][1]+60+20)  	#塔左上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+80-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1 <= tower1_center[i][1]+60+20)   #塔右上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+100-1 <= tower1_center[i][1]+60+20) 	#塔左下角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+80-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+100-1 <= tower1_center[i][1]+60+20)  #塔右下角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+40-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+40+20-1 <= tower1_center[i][1]+60+20)#塔視覺中心
						
							or	(tower1_center[i][0]+20-20 <= self.rect[0]+1+20 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1 <= tower1_center[i][1]+60+20)  	#上角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+80-1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+20+1+20 <= tower1_center[i][1]+60+20)#右角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+1 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+100-1-20 <= tower1_center[i][1]+60+20)  #左角
							or  (tower1_center[i][0]+20-20 <= self.rect[0]+80-1-20 <= tower1_center[i][0]+20+20 and tower1_center[i][1]+60-20 <= self.rect[1]+100-1 <= tower1_center[i][1]+60+20)#下角
						):				  
							counter -= 1
				# if有1個以上座塔2，判定是否與已放置的塔2重疊
				if len(tower2_center) > 0:
					for i in range(len(tower2_center)):
						if (	(tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1 <= tower2_center[i][1]+50+30)  	#塔左上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+80-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1 <= tower2_center[i][1]+50+30)   #塔右上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+100-1 <= tower2_center[i][1]+50+30)	 	#塔左下角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+80-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+100-1 <= tower2_center[i][1]+50+30)  #塔右下角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+40-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+40+20-1 <= tower2_center[i][1]+50+30)#塔視覺中心
						
							or	(tower2_center[i][0]+30-30 <= self.rect[0]+1+20 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1 <= tower2_center[i][1]+50+30)  	#上角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+80-1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+20+1+20 <= tower2_center[i][1]+50+30)#右角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+1 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+100-1-20 <= tower2_center[i][1]+50+30)  	#左角
							or  (tower2_center[i][0]+30-30 <= self.rect[0]+80-1-20 <= tower2_center[i][0]+30+30 and tower2_center[i][1]+50-30 <= self.rect[1]+100-1 <= tower2_center[i][1]+50+30)#下角
						):				  
							counter -= 1
				# if有1個以上座塔3，判定是否與已放置的塔3重疊
				if len(tower3_center) > 0:
					for i in range(len(tower3_center)):
						if (	(tower3_center[i][0]+40-40-10 <= self.rect[0]+1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+20+1 <= tower3_center[i][1]+60+40-10)  	#塔左上角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+80-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+20+1 <= tower3_center[i][1]+60+40-10)   #塔右上角
							or  (tower3_center[i][0]+40-40-10 <= self.rect[0]+1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+100-1 <= tower3_center[i][1]+60+40-10) 	#塔左下角
							or  (tower3_center[i][0]+40-40-10<= self.rect[0]+80-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+100-1 <= tower3_center[i][1]+60+40-10)  #塔右下角
							or  (tower3_center[i][0]+40-40-10<= self.rect[0]+40-1 <= tower3_center[i][0]+40+40-10 and tower3_center[i][1]+60-40-10 <= self.rect[1]+40+20-1 <= tower3_center[i][1]+60+40-10)#塔視覺中心
						):				  
							counter -= 1
				
				# 若在道路內或重疊其他塔，不可放置，顯示紅色圖案
				if counter != len(road_center)+len(tower1_center)+len(tower2_center)+len(tower3_center):		
					surface.blit(Tower_mouthwash(pygame.mouse.get_rel()).image2 , self.rect)
					if self.click == False and self.clickup == False:   # 若在道路上放開滑鼠，讓塔仍能拉動，但要放置完成，才可再放新塔
						self.located = False
						cannot_locate3 = True
						
				# 若不在道路內，若放開滑鼠，即完成放置
				else:	   
					cannot_locate3 = False  # 已放置到正確位置，"無法放置"的提示文字可消失
					""" 在目前image所在位置get_rect()，
						在這個範圍內(  而非整個surface，所以滑鼠不動時get_rel()=(0,0)，但是這範圍內的左上角(0,0)，非全畫面的左上角(0,0)  )
						持續blit牙刷塔圖像，不管滑鼠是否click，是否在移動 """
					surface.blit(Tower_mouthwash(pygame.mouse.get_rel()).image , self.rect)
					if self.click == False and self.clickup == False:
						tower3_center.append(  ( list(self.rect.center)[0]-40 , list(self.rect.center)[1]-40 )  ) 
							# 紀錄新append上去的塔的整張image的左上角座標( 由中心點座標(tuple)轉換 )
						self.located = True	 # 已放置到正確位置，不可再移動
						hint3 = True	#因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數
						self.clickup = True # 已放開滑鼠，位置確定後，讓塔的位置不會記錄第二次
						coins -= Tower_mouthwash_price #扣錢
						addwaterball(waterballs,tower3_center[len(tower3_center)-1])	#啟動攻擊動畫
						while len(waterballs) != len(waterballs_move):
							waterballs_move.append([0,0])
			elif self.located == True:  # 塔已放置好，只要一直draw就行
				surface.blit(Tower_mouthwash(pygame.mouse.get_rel()).image , self.rect)
							
# 牙刷動畫1:(牙刷)			
class Animation_brush (Animation):
	def __init__( self, target ):
		Animation.__init__( self , target )
		self.idle = 0 #沒動畫時的發呆圖編號
		self.level = 0 #升級標示用
	
	def update( self, current_time, rate = 15 ): #跑圖
		Animation.update( self , current_time , rate = 15 )
	def attack( self , direction = 'right'): #攻擊
		#direction == left 左邊 right 右邊
		self.run_mode = 1 
		self.state_mode = 1
		if direction == 'right':
			self.frame = 1
			self.first_frame = 0
			self.last_frame = 11
			self.idle = 0
		if direction == 'left':
			self.frame = 1
			self.first_frame = 0
			self.last_frame = 11
			self.idle = 0
				
# 攻擊動畫2:(牙膏塔)
class Toothpastes_Attack(object):
	#塔的攻擊動作
	def __init__(self , image, pos, game_area):# pos 是塔的中心位置
		pygame.sprite.Sprite.__init__(self)
		
		self.screen = pygame.display.get_surface() # Get reference to the display.
		self.rect = self.image.get_rect()
	def draw(self, screen,time,d):#讀入經過時間及設定攻擊範圍
		image = pygame.image.load(snowball_image_filename).convert_alpha()#全圖:10x10
		global snowballs, snowballs_move, time_passed #所有雪球的初始座標，雪球移動列表，移動速度及經過時間
		tp = time/1000
		listlenth = len(snowballs)
		dis = d #塔攻擊速度控制項
		if snowballs_move == []:
			for i in range(listlenth):
				snowballs_move.append([0,0])
		elif snowballs_move[0][0] <= (-20):#當到達一固定範圍
			snowballs_move = []
		for i in range(listlenth):
			ni = i%4  
			if snowballs_move != []:
				if ni == 0 : #左上的球 --
					snowballs_move[i][0] -= dis*tp
					snowballs_move[i][1] -= dis*tp
					x = snowballs[i][0] + snowballs_move[i][0]
					y = snowballs[i][1] + snowballs_move[i][1]
					self.screen.blit(image,(x,y))
				elif ni == 1:#右上的球 +-
					snowballs_move[i][0] += dis*tp
					snowballs_move[i][1] -= dis*tp
					x = snowballs[i][0] + snowballs_move[i][0]
					y = snowballs[i][1] + snowballs_move[i][1]
					self.screen.blit(image,(x,y))
				elif ni == 2:#右下的球 ++
					snowballs_move[i][0] += dis*tp
					snowballs_move[i][1] += dis*tp
					x = snowballs[i][0] + snowballs_move[i][0]
					y = snowballs[i][1] + snowballs_move[i][1]
					self.screen.blit(image,(x,y))				
				elif ni == 3:#左下的球 -+
					snowballs_move[i][0] -= dis*tp
					snowballs_move[i][1] += dis*tp
					x = snowballs[i][0] + snowballs_move[i][0]
					y = snowballs[i][1] + snowballs_move[i][1]
					self.screen.blit(image,(x,y))
	
# 攻擊動畫3:(漱口水塔)				
class Mouthwashs_Attack(object):
	#塔的攻擊動作
	def __init__(self , pos, game_area):# pos 是塔的中心位置
		pygame.sprite.Sprite.__init__(self)
		self.screen = pygame.display.get_surface() # Get reference to the display.
		self.rect = self.image.get_rect()
	def draw(self, screen,time,di):#讀入經過時間及設定攻擊範圍
		image = pygame.image.load(waterball_image_filename).convert_alpha()#全圖:15x15
		global waterballs, waterballs_move, time_passed #所有水球的初始座標，水球移動列表，移動速度及經過時間
		tp = time/1000
		listlenth = len(waterballs)
		dis = di #塔攻擊速度控制項
		if waterballs_move == []:
			for i in range(listlenth):
				waterballs_move.append([0,0])
		elif waterballs_move[0][0] <= (-40):#當到達一固定範圍
			waterballs_move = []
		for i in range(listlenth):
			ni = i%8
			if waterballs_move != []:
				if ni == 0 : #左上的球 --
					waterballs_move[i][0] -= dis*tp
					waterballs_move[i][1] -= dis*tp
					x = waterballs[i][0] + waterballs_move[i][0]
					y = waterballs[i][1] + waterballs_move[i][1]
					self.screen.blit(image,(x,y))
		
				elif ni == 1:#右上 +-
					waterballs_move[i][0] += dis*tp
					waterballs_move[i][1] -= dis*tp
					x = waterballs[i][0] + waterballs_move[i][0]
					y = waterballs[i][1] + waterballs_move[i][1]
					self.screen.blit(image,(x,y))
				elif ni == 2:#上中 0-
					waterballs_move[i][1] -= dis*tp
					x = waterballs[i][0] 
					y = waterballs[i][1] + waterballs_move[i][1]
					self.screen.blit(image,(x,y))			   
				elif ni == 3: #3 右中 +0
					waterballs_move[i][0] += dis*tp
					x = waterballs[i][0] + waterballs_move[i][0]
					y = waterballs[i][1]
					self.screen.blit(image,(x,y))
				elif ni == 4:#4 左中 -0
					waterballs_move[i][0] -= dis*tp
					x = waterballs[i][0] + waterballs_move[i][0]
					y = waterballs[i][1] 
					self.screen.blit(image,(x,y))
				elif ni == 5:#右下 ++
					waterballs_move[i][0] += dis*tp
					waterballs_move[i][1] += dis*tp
					x = waterballs[i][0] + waterballs_move[i][0]
					y = waterballs[i][1] + waterballs_move[i][1]
					self.screen.blit(image,(x,y))
				elif ni == 6:#下中 0+
					waterballs_move[i][1] += dis*tp
					x = waterballs[i][0] 
					y = waterballs[i][1] + waterballs_move[i][1]
					self.screen.blit(image,(x,y))
				elif ni == 7:#左下 -+
					waterballs_move[i][0] -= dis*tp
					waterballs_move[i][1] += dis*tp
					x = waterballs[i][0] + waterballs_move[i][0]
					y = waterballs[i][1] + waterballs_move[i][1]
					self.screen.blit(image,(x,y))

# 牙齒動畫(被攻擊/死亡)		  
class Animation_tooth(Animation):
	def __init__( self, target ):
		Animation.__init__(self,target)
		self.idle = 42 #沒動畫時的發呆圖編號
	def update( self, current_time, rate = 90 ): #跑圖
		Animation.update( self , current_time , rate = 90 )
	def be_attacked( self ): #一個怪物進來
		self.run_mode = 1
		self.state_mode = 1
		self.frame = self.first_frame = 42
		self.last_frame = 55
		self.idle = 42
	
	def dead( self ): #血條扣完
		self.run_mode = 0
		self.state_mode = 1
		self.frame = self.first_frame = 0
		self.last_frame = 41
		self.idle = 41
###<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Box(pygame.sprite.Sprite):
		def __init__(self, color, pos):
				pygame.sprite.Sprite.__init__(self)
				self.image = pygame.Surface([20, 20])
				self.image.fill(color)
				self.rect = self.image.get_rect()
				self.rect.topleft = pos
		def update(self):
				self.rect.y += 1
				if (self.rect.y > 660):
					self.rect.y = -1 * 20
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		
# 主程式的函數 : App
class App(object):
	def __init__(self):
		self.screen = pygame.display.get_surface() # Get reference to the display.
		self.screen_rect = self.screen.get_rect()
		self.done = False # A flag to tell our game when to quit.
		self.keys = pygame.key.get_pressed() # All the keys currently held.
		self.clock = pygame.time.Clock() # Create a clock to restrict framerate.
		self.fps = 60   # Define your max framerate.
		
		self.tower1s = []
		self.tower2s = []
		self.tower3s = []
		self.tower1s.append( Tower_brush((820+40+40 , 100+40)) ) # 繪製初始牙刷塔 (因為繪製時是輸入center當作起點座標，不是左上角
		self.tower2s.append( Tower_toothpaste((820+40+40 , 200+40)) ) # 繪製初始牙膏塔 
		self.tower3s.append( Tower_mouthwash((820+40+50 , 300+50)) ) # 繪製初始牙膏塔 
		
		self.animation_group = None #12_30晚.py
		
	def event_loop(self):
		global nomoney, hint1, hint2, hint3,decay
		for event in pygame.event.get():
			if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]: # 按下 ESC 鍵 或者觸發一個 QUIT 事件時，更動self.done這個flag
				self.done = True
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:	# 按下滑鼠左鍵時
				# 塔一
				for i in range(0,len(self.tower1s)):
					self.tower1s[i].check_click(event.pos)
				# 塔二
				for i in range(0,len(self.tower2s)):
					self.tower2s[i].check_click(event.pos)
				# 塔三
				for i in range(0,len(self.tower3s)):
					self.tower3s[i].check_click(event.pos)
				hint1 = False   # 因為解決不了 放置好塔之後要再按一下才能拉新塔的bug，而加的提示字顯示變數(再按一下使回歸False)
				hint2 = False
				hint3 = False
					
			elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:	  # 放開滑鼠左鍵時
				# 塔一
				for i in range(0,len(self.tower1s)):
					self.tower1s[i].click = False
				# 塔二
				for i in range(0,len(self.tower2s)):
					self.tower2s[i].click = False
				# 塔三
				for i in range(0,len(self.tower3s)):
					self.tower3s[i].click = False
				
				if self.tower1s[-1].located == True:
					self.tower1s.append( Tower_brush((820+40+40 , 100+40)) ) # 新塔放置成功，才再畫一張在操作面板上
				if self.tower2s[-1].located == True:
					self.tower2s.append( Tower_toothpaste((820+40+40 , 200+40)) ) # 新塔放置成功，才再畫一張在操作面板上
				if self.tower3s[-1].located == True:
					self.tower3s.append( Tower_mouthwash((820+40+50 , 300+50)) ) # 新塔放置成功，才再畫一張在操作面板上
				
				nomoney = False # 因沒錢時拉塔時，會讓nomoney = True，下面render()就會畫面顯示文字，所以放開滑鼠時要回歸False

			elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
				self.keys = pygame.key.get_pressed()
				
	def render(self):
		global nomoney, cannot_locate1, cannot_locate2, cannot_locate3, hint1, hint2, hint3,be_delay, brush_test1  
		#繪製背景，道路寬度60
		"""rect繪製一個矩形(畫布,RGB三色值參數(0為完全不顯示，255為完全顯示),
			矩形區域(left, up, width, height))
			left 是矩型最左邊的 x 座標，而 up 代表最上邊的 y 座標，width 代表寬度，height 代表高度。
			程式裡的(250, 250, 10, 10) 就是說在座標 (250, 250) 的地方，繪出一個 10x10 的矩形"""
		self.screen.blit(pygame.image.load(background_image_filename).convert(), (0, 0)) #使用綠色草地填滿整個背景，*必須使用(( ))
		self.screen.fill(brick, (0, 0, 820, 40))			#繪製不可放置塔區域
		self.screen.fill(blackboard, (820 , 0, 180, 660))   #繪製操作面板
		usefont = pygame.font.SysFont('simhei',25)	  #設定使用字體，大小25，可用字體為'simhei'，'yumincho'，'simhei'最佳，70，72[標楷體]
		usefont2 = pygame.font.SysFont('simhei',20)
		round_font = usefont.render("  第 " + " 波", True, roundcolor)  # 第幾波放怪
		coin_font = usefont.render("金幣：" , True, coincolor)  # 金幣：黑底黃字
		coin_font01 = usefont2.render("50元" , True, blue)
		coin_font011 = usefont2.render("(按z鍵攻擊)" , True, blue)
		coin_font02 = usefont2.render("100元" , True, blue)
		coin_font03 = usefont2.render("170元" , True, blue)
		coin_font2 = usefont.render(str(coins), True, coincolor)	# 金幣：黑底黃字
		round_font2 = usefont.render(str(rounds), True, roundcolor)  # 第幾波放怪
		self.screen.blit(round_font, ( 820+20 , 20) )	   # 繪製第幾波放怪至操作面板
		self.screen.blit(coin_font, ( 820+20 , 60) )		# 繪製金幣餘額至操作面板
		self.screen.blit(round_font2, ( 820+80 , 20) )	  # 繪製第幾波放怪至操作面板
		self.screen.blit(coin_font2, ( 820+90 , 60) )	   # 繪製金幣餘額至操作面板
		self.screen.blit(coin_font01, ( 820+5 , 120) )
		self.screen.blit(coin_font011, ( 820+70 , 120) )
		self.screen.blit(coin_font02, ( 820+5 , 190+5) )
		self.screen.blit(coin_font03, ( 820+5 , 290+5) )
		
		
			#繪製血條。扣血時，減少第三個參數(寬度)值，其他參數不變
		self.screen.fill(bloodcolor, (820+30, 500-40, 1000-820-30-30-sb, 20))
		self.screen.fill(bloodcolor, (820+30, 500-40, 1000-820-30-30,1))	#上界
		self.screen.fill(bloodcolor, (820+30, 500-20, 1000-820-30-30,1))	#下界
		self.screen.fill(bloodcolor, (820+30, 500-40, 1,20))				#左界
		self.screen.fill(bloodcolor, (820+30+120, 500-40, 1,20))			#右界
		
			#繪製完左半邊的道路
		self.screen.fill(grayroad, (40, 0, 60, 200))
		self.screen.fill(grayroad, (100, 140, 80, 60))
		self.screen.fill(grayroad, (120, 200, 60, 280))
		self.screen.fill(grayroad, (40, 420, 80, 60))
		self.screen.fill(grayroad, (40, 480, 60, 140))
		self.screen.fill(grayroad, (100, 560, 300, 60))
		self.screen.fill(grayroad, (340, 420, 60, 140))
		self.screen.fill(grayroad, (260, 420, 80, 60))
		self.screen.fill(grayroad, (260, 200, 60, 220))
		self.screen.fill(grayroad, (320, 200, 100, 60))
		self.screen.fill(grayroad, (360, 80, 60, 120))
	
			#繪製完右半邊的道路
		self.screen.fill(grayroad, (420, 80, 340, 60))
		self.screen.fill(grayroad, (700, 140, 60, 220))
		self.screen.fill(grayroad, (560, 300, 140, 60))
		self.screen.fill(grayroad, (560, 360, 60, 220))
		self.screen.fill(grayroad, (620, 520, 240, 60))
		
		self.screen.fill(grayroad, (860, 500, 100, 100))				#繪製完100x100牙齒區域
		#self.screen.blit(tooth, (860 , 500))						   # 繪製牙齒圖案至操作面板(要比道路晚畫，否則會被覆蓋)
		self.screen.blit(pygame.image.load(brush_image_filename).convert_alpha(), (820+40 , 100))					   # 繪製牙刷塔(不放圖的話，拉塔出去放置時，操作面板上會暫時空掉)
		self.screen.blit(pygame.image.load(toothpaste_image_filename).convert_alpha(), (820+40 , 200))					# 繪製牙膏塔
		self.screen.blit(pygame.image.load(mouthwash_image_filename).convert_alpha(), (820+40 , 300))					 # 繪製漱口水
		
		#繪製每個已經放置的塔
		for i in range(0,len(self.tower1s)):
			self.tower1s[i].draw(self.screen)
		for i in range(0,len(self.tower2s)):
			self.tower2s[i].draw(self.screen)
			# print(len(self.tower2s))
			# print(len(tower2_center))
		for i in range(0,len(self.tower3s)):
			self.tower3s[i].draw(self.screen)
		
		if nomoney == True:
			self.screen.fill( bloodcolor, (820+20-2.5, 60-5, 140-5+10 , 30+5+10))
			self.screen.fill( white, (820+20+2.5, 60, 140-5 , 30+5))
			self.screen.blit( usefont.render("錢不夠喔QQ", True, coincolor), ( 820+20+2.5 , 60+5) )
			
		if hint1 == True or hint2 == True or hint3 == True:
			self.screen.fill( blue, (820+20-2.5, 410-5, 140+10 , 37+5+10))
			self.screen.fill( white, (820+20+2.5, 410, 140 , 37+5))
			self.screen.blit( usefont2.render("在任意處按下滑", True, bloodcolor), ( 820+20+2.5 , 410) )
			self.screen.blit( usefont2.render("鼠左鍵以拉塔", True, bloodcolor), ( 820+20+2.5 , 430) )

		if hint1 == False and hint2 == False and hint3 == False:
			self.screen.fill( blackboard, (820+20-2.5, 410-5, 140+10 , 37+5+10))
		
		if cannot_locate1 == True or cannot_locate2 == True or cannot_locate3 == True:
			self.screen.fill( blue, (820+20-2.5, 410-5, 140+10 , 37+5+10))
			self.screen.fill( white, (820+20+2.5, 410, 140 , 37+5))
			self.screen.blit( usefont2.render("塔不能放在道路", True, bloodcolor), ( 820+20+2.5 , 410) )
			self.screen.blit( usefont2.render("上或重疊塔喔!!", True, bloodcolor), ( 820+20+2.5 , 430) )
		
		#繪製動畫
		self.animation_group.update(pygame.time.get_ticks())
		self.animation_group.draw( self.screen )
		
		time_passed = clock.tick()#塔攻擊動畫的計時器
		Toothpastes_Attack.draw(self, self.screen, time_passed,120)#讀入經過時間及設定攻擊速度
		Mouthwashs_Attack.draw(self, self.screen, time_passed,115)#讀入經過時間及設定攻擊速度
		"""
		全場只會有一個pygame.display.update()且他只會在這裡
		"""
		#pygame.display.update() #不斷將繪好的圖形更新到螢幕上
		# display.update() / display.flip() 差別 : https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
	def main_loop(self):
		global clean, brush_test
		framerate = pygame.time.Clock() #計時相關
		#brush_test = Animation_brush ( self.screen ) #牙刷動畫登場
		tooth_test = Animation_tooth ( self.screen ) #牙齒動畫登場
		tooth_test.load( teeth_image_filename, 100, 100, 14 , 860 , 500)
		self.animation_group = pygame.sprite.Group() #要把動畫塞到一個group內才能做事(動)
		self.animation_group.add(tooth_test)
		
		########################################################################
		x = 40
		y = 0
		"""load round_1 的怪物"""
		## load(filename, width, height, columns, x, y, step, health, money, monster_power(x/120) ):
		batMonster1_1 = Animation_Monster(self.screen)
		batMonster1_1.load(bat_image_filename, 60, 63, 17, x, y, 5, 100, 30, 15)  #速度5血100錢50
		batMonster1_1.run()
		
		batMonster1_2 = Animation_Monster(self.screen)
		batMonster1_2.load(bat_image_filename, 60, 63, 17, x, -50, 5, 100, 30, 15)
		batMonster1_2.run()
		
		batMonster1_3 = Animation_Monster(self.screen)
		batMonster1_3.load(bat_image_filename, 60, 63, 17, x, -100, 5, 100, 30, 15)
		batMonster1_3.run()
		
		sheepMonster1_1 = Animation_Monster(self.screen)
		sheepMonster1_1.load(sheep_image_filename, 59, 58, 4, x, -60, 3, 150 , 40, 20)
		sheepMonster1_1.run()
		
		sheepMonster1_2 = Animation_Monster(self.screen)
		sheepMonster1_2.load(sheep_image_filename, 59, 58, 4, x, -120, 3, 150 , 40, 20)
		sheepMonster1_2.run()
		
		round_1 = pygame.sprite.Group()
		round_1.add(batMonster1_1, batMonster1_2, batMonster1_3, sheepMonster1_1, sheepMonster1_2)
		
	    ##############################################################################################	
		"""load round_2 的怪物"""
		## load(filename, width, height, columns, x, y, step, health, money, monster_power(x/120) ):
		
		batMonster2_1 = Animation_Monster(self.screen)
		batMonster2_1.load(bat_image_filename, 60, 63, 17, x, y, 7.5, 100, 30, 15) #速度、血量、加錢、攻擊力
		batMonster2_1.run()
		
		batMonster2_2 = Animation_Monster(self.screen)
		batMonster2_2.load(bat_image_filename, 60, 63, 17, x, -60, 7.5, 100, 30, 15)
		batMonster2_2.run()
		
		batMonster2_3 = Animation_Monster(self.screen)
		batMonster2_3.load(bat_image_filename, 60, 63, 17, x, -105, 7.5, 100, 30, 15)
		batMonster2_3.run()
		
		sheepMonster2_1 = Animation_Monster(self.screen)
		sheepMonster2_1.load(sheep_image_filename, 59, 58, 4, x, -100, 5, 150 , 30, 20)
		sheepMonster2_1.run()
		
		sheepMonster2_2 = Animation_Monster(self.screen)
		sheepMonster2_2.load(sheep_image_filename, 59, 58, 4, x, -160, 5, 150 , 30, 20)
		sheepMonster2_2.run()
		
		sheepMonster2_3 = Animation_Monster(self.screen)
		sheepMonster2_3.load(sheep_image_filename, 59, 58, 4, x, -220, 5, 150 , 30, 20)
		sheepMonster2_3.run()
		
		pumpkinMonster2_1 = Animation_Monster(self.screen)
		pumpkinMonster2_1.load(pumpkin_image_filename,60, 58, 38, x, -180, 3, 250, 30, 30)
		pumpkinMonster2_1.run()
		
		round_2 = pygame.sprite.Group()
		round_2.add(batMonster2_1, batMonster2_2, batMonster2_3, sheepMonster2_1, sheepMonster2_2, sheepMonster2_3, pumpkinMonster2_1)
		
		############################################################################################
		"""load round_3 的怪物"""
		
		batMonster3_1 = Animation_Monster(self.screen)
		batMonster3_1.load(bat_image_filename, 60, 63, 17, x, y, 15, 100, 20, 15) #速度、血量、加錢、攻擊力
		batMonster3_1.run()
		
		batMonster3_2 = Animation_Monster(self.screen)
		batMonster3_2.load(bat_image_filename, 60, 63, 17, x, -60, 15, 100, 20, 15)
		batMonster3_2.run()
		
		batMonster3_3 = Animation_Monster(self.screen)
		batMonster3_3.load(bat_image_filename, 60, 63, 17, x, -120, 15, 100, 20, 15)
		batMonster3_3.run()
		
		batMonster3_4 = Animation_Monster(self.screen)
		batMonster3_4.load(bat_image_filename, 60, 63, 17, x, -180, 15, 100, 20, 15)
		batMonster3_4.run()
		
		batMonster3_5 = Animation_Monster(self.screen)
		batMonster3_5.load(bat_image_filename, 60, 63, 17, x, -240, 15, 100, 20, 15)
		batMonster3_5.run()
		
		sheepMonster3_1 = Animation_Monster(self.screen)
		sheepMonster3_1.load(sheep_image_filename, 59, 58, 4, x, -150, 7.5, 200 , 20, 20)
		sheepMonster3_1.run()
		
		sheepMonster3_2 = Animation_Monster(self.screen)
		sheepMonster3_2.load(sheep_image_filename, 59, 58, 4, x, -240, 7.5, 200 , 20, 20)
		sheepMonster3_2.run()
		
		sheepMonster3_3 = Animation_Monster(self.screen)
		sheepMonster3_3.load(sheep_image_filename, 59, 58, 4, x, -330, 7.5, 200 , 20, 20)
		sheepMonster3_3.run()
		
		sheepMonster3_4 = Animation_Monster(self.screen)
		sheepMonster3_4.load(sheep_image_filename, 59, 58, 4, x, -420, 7.5, 200 , 20, 20)
		sheepMonster3_4.run()
		
		sheepMonster3_5 = Animation_Monster(self.screen)
		sheepMonster3_5.load(sheep_image_filename, 59, 58, 4, x, -510, 7.5, 200 , 20, 20)
		sheepMonster3_5.run()
		
		pumpkinMonster3_1 = Animation_Monster(self.screen)
		pumpkinMonster3_1.load(pumpkin_image_filename,60, 58, 38, x, -360, 5, 400, 30, 30)
		pumpkinMonster3_1.run()
		
		pumpkinMonster3_2 = Animation_Monster(self.screen)
		pumpkinMonster3_2.load(pumpkin_image_filename,60, 58, 38, x, -420, 5, 400, 30, 30)
		pumpkinMonster3_2.run()
		
		round_3 = pygame.sprite.Group()
		round_3.add(batMonster3_1, batMonster3_2, batMonster3_3, batMonster3_4, batMonster3_5, 
					sheepMonster3_1, sheepMonster3_2, sheepMonster3_3, sheepMonster3_4, sheepMonster3_5, 
					pumpkinMonster3_1, pumpkinMonster3_2)
		#####################################################################################################
		"""load round_4 的怪物"""
		batMonster4_1 = Animation_Monster(self.screen)
		batMonster4_1.load(bat_image_filename, 60, 63, 17, x, y, 15, 150, 20, 15) #速度、血量、加錢、攻擊力
		batMonster4_1.run()
		
		batMonster4_2 = Animation_Monster(self.screen)
		batMonster4_2.load(bat_image_filename, 60, 63, 17, x, -90, 15, 150, 20, 15)
		batMonster4_2.run()
		
		batMonster4_3 = Animation_Monster(self.screen)
		batMonster4_3.load(bat_image_filename, 60, 63, 17, x, -180, 15, 150, 20, 15)
		batMonster4_3.run()
		
		batMonster4_4 = Animation_Monster(self.screen)
		batMonster4_4.load(bat_image_filename, 60, 63, 17, x, -270, 15, 150, 20, 15)
		batMonster4_4.run()
		
		batMonster4_5 = Animation_Monster(self.screen)
		batMonster4_5.load(bat_image_filename, 60, 63, 17, x, -360, 15, 150, 20, 15)
		batMonster4_5.run()
		
		batMonster4_6 = Animation_Monster(self.screen)
		batMonster4_6.load(bat_image_filename, 60, 63, 17, x, -450, 15, 150, 20, 15)
		batMonster4_6.run()
		
		batMonster4_7 = Animation_Monster(self.screen)
		batMonster4_7.load(bat_image_filename, 60, 63, 17, x, -540, 15, 150, 20, 15)
		batMonster4_7.run()
		
		batMonster4_8 = Animation_Monster(self.screen)
		batMonster4_8.load(bat_image_filename, 60, 63, 17, x, -630, 15, 150, 20, 15)
		batMonster4_8.run()
		
		batMonster4_9 = Animation_Monster(self.screen)
		batMonster4_9.load(bat_image_filename, 60, 63, 17, x, -720, 15, 150, 20, 15)
		batMonster4_9.run()
		
		batMonster4_10 = Animation_Monster(self.screen)
		batMonster4_10.load(bat_image_filename, 60, 63, 17, x, -810, 15, 150, 20, 15)
		batMonster4_10.run()
		
		sheepMonster4_1 = Animation_Monster(self.screen)
		sheepMonster4_1.load(sheep_image_filename, 59, 58, 4, x, -420, 7.5, 300, 20, 20)
		sheepMonster4_1.run()
		
		sheepMonster4_2 = Animation_Monster(self.screen)
		sheepMonster4_2.load(sheep_image_filename, 59, 58, 4, x, -480, 7.5, 300 , 20, 20)
		sheepMonster4_2.run()
		
		sheepMonster4_3 = Animation_Monster(self.screen)
		sheepMonster4_3.load(sheep_image_filename, 59, 58, 4, x, -540, 7.5, 300 , 20, 20)
		sheepMonster4_3.run()
		
		sheepMonster4_4 = Animation_Monster(self.screen)
		sheepMonster4_4.load(sheep_image_filename, 59, 58, 4, x, -600, 7.5, 300 , 20, 20)
		sheepMonster4_4.run()
		
		sheepMonster4_5 = Animation_Monster(self.screen)
		sheepMonster4_5.load(sheep_image_filename, 59, 58, 4, x, -660, 7.5, 300 , 20, 20)
		sheepMonster4_5.run()
		
		sheepMonster4_6 = Animation_Monster(self.screen)
		sheepMonster4_6.load(sheep_image_filename, 59, 58, 4, x, -720, 7.5, 300 , 20, 20)
		sheepMonster4_6.run()
		
		pumpkinMonster4_1 = Animation_Monster(self.screen)
		pumpkinMonster4_1.load(pumpkin_image_filename,60, 58, 38, x, -480, 5, 500, 30, 30)
		pumpkinMonster4_1.run()
		
		pumpkinMonster4_2 = Animation_Monster(self.screen)
		pumpkinMonster4_2.load(pumpkin_image_filename,60, 58, 38, x, -540, 5, 500, 30, 30)
		pumpkinMonster4_2.run()
		
		pumpkinMonster4_3 = Animation_Monster(self.screen)
		pumpkinMonster4_3.load(pumpkin_image_filename,60, 58, 38, x, -600, 5, 500, 30, 30)
		pumpkinMonster4_3.run()
		
		pumpkinMonster4_4 = Animation_Monster(self.screen)
		pumpkinMonster4_4.load(pumpkin_image_filename,60, 58, 38, x, -660, 5, 500, 30, 30)
		pumpkinMonster4_4.run()
		
		round_4 = pygame.sprite.Group()
		round_4.add(batMonster4_1, batMonster4_2, batMonster4_3, batMonster4_4, batMonster4_5, 
					batMonster4_6, batMonster4_7, batMonster4_8, batMonster4_9, batMonster4_10,
					sheepMonster4_1, sheepMonster4_2, sheepMonster4_3, sheepMonster4_4, 
					sheepMonster4_5, sheepMonster4_6,
					pumpkinMonster4_1, pumpkinMonster4_2, pumpkinMonster4_3, pumpkinMonster4_4)
		#################################################################################################
		"""load round_5 的怪物"""
		batMonster5_1 = Animation_Monster(self.screen)
		batMonster5_1.load(bat_image_filename, 60, 63, 17, x, y, 15, 200, 20, 15) #速度、血量、加錢、攻擊力
		batMonster5_1.run()
		
		batMonster5_2 = Animation_Monster(self.screen)
		batMonster5_2.load(bat_image_filename, 60, 63, 17, x, -90, 15, 200, 20, 15)
		batMonster5_2.run()
		
		batMonster5_3 = Animation_Monster(self.screen)
		batMonster5_3.load(bat_image_filename, 60, 63, 17, x, -180, 15, 200, 20, 15)
		batMonster5_3.run()
		
		batMonster5_4 = Animation_Monster(self.screen)
		batMonster5_4.load(bat_image_filename, 60, 63, 17, x, -270, 15, 200, 20, 15)
		batMonster5_4.run()
		
		batMonster5_5 = Animation_Monster(self.screen)
		batMonster5_5.load(bat_image_filename, 60, 63, 17, x, -360, 15, 200, 20, 15)
		batMonster5_5.run()
		
		batMonster5_6 = Animation_Monster(self.screen)
		batMonster5_6.load(bat_image_filename, 60, 63, 17, x, -450, 15, 200, 20, 15)
		batMonster5_6.run()
		
		batMonster5_7 = Animation_Monster(self.screen)
		batMonster5_7.load(bat_image_filename, 60, 63, 17, x, -540, 15, 200, 20, 15)
		batMonster5_7.run()
		
		batMonster5_8 = Animation_Monster(self.screen)
		batMonster5_8.load(bat_image_filename, 60, 63, 17, x, -630, 15, 200, 20, 15)
		batMonster5_8.run()
		
		batMonster5_9 = Animation_Monster(self.screen)
		batMonster5_9.load(bat_image_filename, 60, 63, 17, x, -720, 15, 200, 20, 15)
		batMonster5_9.run()
		
		batMonster5_10 = Animation_Monster(self.screen)
		batMonster5_10.load(bat_image_filename, 60, 63, 17, x, -810, 15, 200, 20, 15)
		batMonster5_10.run()
		
		sheepMonster5_1 = Animation_Monster(self.screen)
		sheepMonster5_1.load(sheep_image_filename, 59, 58, 4, x, -420, 7.5, 500, 20, 20)
		sheepMonster5_1.run()
		
		sheepMonster5_2 = Animation_Monster(self.screen)
		sheepMonster5_2.load(sheep_image_filename, 59, 58, 4, x, -480, 7.5, 500, 20, 20)
		sheepMonster5_2.run()
		
		sheepMonster5_3 = Animation_Monster(self.screen)
		sheepMonster5_3.load(sheep_image_filename, 59, 58, 4, x, -540, 7.5, 500, 20, 20)
		sheepMonster5_3.run()
		
		sheepMonster5_4 = Animation_Monster(self.screen)
		sheepMonster5_4.load(sheep_image_filename, 59, 58, 4, x, -600, 7.5, 500, 20, 20)
		sheepMonster5_4.run()
		
		sheepMonster5_5 = Animation_Monster(self.screen)
		sheepMonster5_5.load(sheep_image_filename, 59, 58, 4, x, -660, 7.5, 500, 20, 20)
		sheepMonster5_5.run()
		
		sheepMonster5_6 = Animation_Monster(self.screen)
		sheepMonster5_6.load(sheep_image_filename, 59, 58, 4, x, -720, 7.5, 500, 20, 20)
		sheepMonster5_6.run()
		
		sheepMonster5_7 = Animation_Monster(self.screen)
		sheepMonster5_7.load(sheep_image_filename, 59, 58, 4, x, -780, 7.5, 500, 20, 20)
		sheepMonster5_7.run()
		
		sheepMonster5_8 = Animation_Monster(self.screen)
		sheepMonster5_8.load(sheep_image_filename, 59, 58, 4, x, -840, 7.5, 500, 20, 20)
		sheepMonster5_8.run()
		
		sheepMonster5_9 = Animation_Monster(self.screen)
		sheepMonster5_9.load(sheep_image_filename, 59, 58, 4, x, -900, 7.5, 500, 20, 20)
		sheepMonster5_9.run()
		
		sheepMonster5_10 = Animation_Monster(self.screen)
		sheepMonster5_10.load(sheep_image_filename, 59, 58, 4, x, -960, 7.5, 500, 20, 20)
		sheepMonster5_10.run()
		
		pumpkinMonster5_1 = Animation_Monster(self.screen)
		pumpkinMonster5_1.load(pumpkin_image_filename,60, 58, 38, x, -1080, 7.5, 650, 20, 30)
		pumpkinMonster5_1.run()
		
		pumpkinMonster5_2 = Animation_Monster(self.screen)
		pumpkinMonster5_2.load(pumpkin_image_filename,60, 58, 38, x, -1140, 7.5, 650, 20, 30)
		pumpkinMonster5_2.run()
		
		pumpkinMonster5_3 = Animation_Monster(self.screen)
		pumpkinMonster5_3.load(pumpkin_image_filename,60, 58, 38, x, -1200, 7.5, 650, 20, 30)
		pumpkinMonster5_3.run()
		
		pumpkinMonster5_4 = Animation_Monster(self.screen)
		pumpkinMonster5_4.load(pumpkin_image_filename,60, 58, 38, x, -1260, 7.5, 650, 20, 30)
		pumpkinMonster5_4.run()
		
		pumpkinMonster5_5 = Animation_Monster(self.screen)
		pumpkinMonster5_5.load(pumpkin_image_filename,60, 58, 38, x, -1320, 7.5, 650, 20, 30)
		pumpkinMonster5_5.run()
		
		pumpkinMonster5_6 = Animation_Monster(self.screen)
		pumpkinMonster5_6.load(pumpkin_image_filename,60, 58, 38, x, -1380, 7.5, 650, 20,30)
		pumpkinMonster5_6.run()
		
		round_5 = pygame.sprite.Group()
		round_5.add(batMonster5_1, batMonster5_2, batMonster5_3, batMonster5_4, batMonster5_5, 
					batMonster5_6, batMonster5_7, batMonster5_8, batMonster5_9, batMonster5_10,
					sheepMonster5_1, sheepMonster5_2, sheepMonster5_3, sheepMonster5_4, sheepMonster5_5, 
					sheepMonster5_6, sheepMonster5_7, sheepMonster5_8, sheepMonster5_9, sheepMonster5_10,
					pumpkinMonster5_1, pumpkinMonster5_2, pumpkinMonster5_3, pumpkinMonster5_4,
					pumpkinMonster5_5, pumpkinMonster5_6)
					
		pygame.mixer.music.load(halloween_music_filename)
		pygame.mixer.music.play(-1) 
		
		########################################################################			
		while not self.done:
			global toothblood,attack_tooth,decay, tooth_dead, rounds,be_delay,clean,add
			"""
			請在這裡放可以讓程式偵測到要放動畫的東西
			"""
			self.render()
			
			#這裡有新牙刷
			if add == 1 : #有新左牙刷
				addbrush(tower1_left,brush1_list,brushesleft_image_filename,self.screen,self.animation_group)
				"""
				for i in range(0, len(tower1_left)):
					brush_test.load( brushes_image_filename, 80, 80, 12 , tower1_left[i][0] , tower1_left[i][1])
				"""
			if add == 2 : #有新右牙刷
				addbrush(tower1_right,brush2_list,brushesright_image_filename,self.screen,self.animation_group)

			framerate.tick(60) #計時相關
			ticks = pygame.time.get_ticks()
			
			round_1_health = ( batMonster1_1.health + batMonster1_2.health + batMonster1_3.health
							+sheepMonster1_1.health + sheepMonster1_2.health)
			
			round_2_health = (batMonster2_1.health + batMonster2_2.health + batMonster2_3.health 
							+ sheepMonster2_1.health + sheepMonster2_2.health + sheepMonster2_3.health
							+ pumpkinMonster2_1.health)
			
			round_3_health = (batMonster3_1.health + batMonster3_2.health + batMonster3_3.health 
							+ batMonster3_4.health + batMonster3_5.health
							+ sheepMonster3_1.health + sheepMonster3_2.health + sheepMonster3_3.health + 
							sheepMonster3_4.health + sheepMonster3_5.health
							+ pumpkinMonster3_1.health + pumpkinMonster3_2.health)
			
			round_4_health = (batMonster4_1.health + batMonster4_2.health + batMonster4_3.health 
							+ batMonster4_4.health + batMonster4_5.health + batMonster4_6.health
							+ batMonster4_7.health + batMonster4_8.health + batMonster4_9.health
							+ batMonster4_10.health
							+ sheepMonster4_1.health + sheepMonster4_2.health + sheepMonster4_3.health 
							+ sheepMonster4_4.health + sheepMonster4_5.health + sheepMonster4_6.health
							+ pumpkinMonster4_1.health + pumpkinMonster4_2.health + pumpkinMonster4_3.health
							+ pumpkinMonster4_4.health)
					
			round_5_health = (batMonster5_1.health + batMonster5_2.health + batMonster5_3.health 
							+ batMonster5_4.health + batMonster5_5.health + batMonster5_6.health
							+ batMonster5_7.health + batMonster5_8.health + batMonster5_9.health
							+ batMonster5_10.health
							+ sheepMonster5_1.health + sheepMonster5_2.health + sheepMonster5_3.health 
							+ sheepMonster5_4.health + sheepMonster5_5.health + sheepMonster5_6.health
							+ sheepMonster5_7.health + sheepMonster5_8.health + sheepMonster5_9.health
							+ sheepMonster5_10.health
							+ pumpkinMonster5_1.health + pumpkinMonster5_2.health + pumpkinMonster5_3.health
							+ pumpkinMonster5_4.health + pumpkinMonster5_5.health + pumpkinMonster5_6.health)
					
			if pygame.time.get_ticks() > 3000:	  ## 大於3秒後顯示round_1		   
				round_1.update(ticks)
				round_1.draw(self.screen)
				batMonster1_1.run()
				batMonster1_2.run()
				batMonster1_3.run()
				sheepMonster1_1.run()
				sheepMonster1_2.run()
						
			if round_1_health <= 0:			 #在class Animation_Monster設定怪物一攻擊牙齒，health就等於零		 
				round_2.update(ticks)		   #所以每一波的所有怪物只要死掉或攻擊到牙齒，就會開始下一波怪物
				round_2.draw(self.screen)
				batMonster2_1.run()
				batMonster2_2.run()
				batMonster2_3.run()
				sheepMonster2_1.run()
				sheepMonster2_2.run()
				sheepMonster2_3.run()
				pumpkinMonster2_1.run()
				rounds = 2
				
			if round_2_health <= 0:  
				round_3.update(ticks)
				round_3.draw(self.screen)
				batMonster3_1.run()
				batMonster3_2.run()
				batMonster3_3.run()
				batMonster3_4.run()
				batMonster3_5.run()
				sheepMonster3_1.run()
				sheepMonster3_2.run()
				sheepMonster3_3.run()
				sheepMonster3_4.run()
				sheepMonster3_5.run()
				pumpkinMonster3_1.run()
				pumpkinMonster3_2.run()
				rounds = 3
				
			if round_3_health <= 0:  
				round_4.update(ticks)
				round_4.draw(self.screen)
				batMonster4_1.run()
				batMonster4_2.run()
				batMonster4_3.run()
				batMonster4_4.run()
				batMonster4_5.run()
				batMonster4_6.run()
				batMonster4_7.run()
				batMonster4_8.run()
				batMonster4_9.run()
				batMonster4_10.run()
				sheepMonster4_1.run()
				sheepMonster4_2.run()
				sheepMonster4_3.run()
				sheepMonster4_4.run()
				sheepMonster4_5.run()
				sheepMonster4_6.run()
				pumpkinMonster4_1.run()
				pumpkinMonster4_2.run()
				pumpkinMonster4_3.run()
				pumpkinMonster4_4.run()
				rounds = 4
				
			if round_4_health <= 0:  
				round_5.update(ticks)
				round_5.draw(self.screen)
				batMonster5_1.run()
				batMonster5_2.run()
				batMonster5_3.run()
				batMonster5_4.run()
				batMonster5_5.run()
				batMonster5_6.run()
				batMonster5_7.run()
				batMonster5_8.run()
				batMonster5_9.run()
				batMonster5_10.run()
				sheepMonster5_1.run()
				sheepMonster5_2.run()
				sheepMonster5_3.run()
				sheepMonster5_4.run()
				sheepMonster5_5.run()
				sheepMonster5_6.run()
				sheepMonster5_7.run()
				sheepMonster5_8.run()
				sheepMonster5_9.run()
				sheepMonster5_10.run()
				pumpkinMonster5_1.run()
				pumpkinMonster5_2.run()
				pumpkinMonster5_3.run()
				pumpkinMonster5_4.run()
				pumpkinMonster5_5.run()
				pumpkinMonster5_6.run()
				rounds = 5

			""" 之後 牙刷塔攻擊動話跟損血做完之後，這裡要補tower1_center"""
						# delete(towers lists,tower range,r_whole,r_adjust,attack_power) 
						# r_whole 是讓左上角->整張中心 
						# r_adjust 是讓整張中心->視覺上中心(考慮基座)
						# attack_power 是每種塔的攻擊力
			
			# 第一波
			batMonster1_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster1_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster1_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster1_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)

			batMonster1_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster1_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster1_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster1_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster1_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster1_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster1_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster1_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)

			sheepMonster1_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster1_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster1_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster1_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster1_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster1_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster1_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster1_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			# 第二波
			batMonster2_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster2_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster2_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster2_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			
			batMonster2_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster2_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster2_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster2_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster2_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster2_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster2_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster2_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster2_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster2_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster2_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster2_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster2_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster2_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster2_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster2_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster2_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster2_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster2_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster2_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster2_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster2_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster2_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster2_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			
			# 第三波
			batMonster3_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster3_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster3_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster3_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster3_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster3_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster3_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster3_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster3_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster3_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster3_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster3_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster3_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster3_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster3_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster3_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster3_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster3_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster3_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster3_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster3_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster3_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster3_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster3_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster3_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster3_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster3_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster3_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster3_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster3_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster3_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster3_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster3_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster3_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster3_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster3_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster3_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster3_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster3_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster3_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster3_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster3_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster3_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster3_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster3_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster3_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster3_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster3_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			# 第四波
			batMonster4_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_6.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_6.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_6.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_6.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_7.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_7.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_7.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_7.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_8.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_8.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_8.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_8.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_9.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_9.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_9.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_9.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster4_10.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster4_10.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster4_10.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster4_10.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster4_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster4_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster4_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster4_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster4_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster4_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster4_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster4_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster4_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster4_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster4_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster4_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster4_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster4_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster4_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster4_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster4_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster4_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster4_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster4_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster4_6.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster4_6.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster4_6.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster4_6.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster4_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster4_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster4_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster4_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster4_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster4_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster4_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster4_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster4_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster4_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster4_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster4_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster4_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster4_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster4_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster4_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)

			# 第五波
			batMonster5_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_6.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_6.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_6.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_6.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_7.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_7.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_7.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_7.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_8.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_8.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_8.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_8.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_9.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_9.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_9.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_9.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			batMonster5_10.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			batMonster5_10.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			batMonster5_10.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			batMonster5_10.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_6.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_6.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_6.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_6.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_7.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_7.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_7.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_7.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_8.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_8.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_8.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_8.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_9.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_9.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_9.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_9.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			sheepMonster5_10.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			sheepMonster5_10.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			sheepMonster5_10.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			sheepMonster5_10.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster5_1.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster5_1.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster5_1.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster5_1.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster5_2.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster5_2.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster5_2.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster5_2.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster5_3.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster5_3.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster5_3.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster5_3.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster5_4.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster5_4.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster5_4.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster5_4.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster5_5.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster5_5.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster5_5.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster5_5.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			pumpkinMonster5_6.delete(tower1_left_center,tower1_left_range,tower1_left_r_whole,tower1_left_r_adjust,tower1_left_attack_power,tower1_left_adjust_left)
			pumpkinMonster5_6.delete(tower1_right_center,tower1_right_range,tower1_right_r_whole,tower1_right_r_adjust,tower1_right_attack_power,tower1_right_adjust_left)
			pumpkinMonster5_6.delete(tower2_center,tower2_range,tower2_r_whole,tower2_r_adjust,tower2_attack_power,tower2_adjust_left)
			pumpkinMonster5_6.delete(tower3_center,tower3_range,tower3_r_whole,tower3_r_adjust,tower3_attack_power,tower3_adjust_left)
			
			if decay == True:
				self.screen.blit(pygame.image.load(befont_image_filename).convert_alpha(),(0,0))
				be_delay += 1
				pygame.mixer.music.fadeout(1500)
				if be_delay >= 80:
					self.screen.blit(pygame.image.load(bad_ending_image_filename).convert_alpha(),(0,0))
					pygame.mixer.music.load(be_music_filename) #播放音樂
					pygame.mixer.music.play(-1)	#-1是循環播放的意思
			if clean == True:
				self.screen.blit(pygame.image.load(hefont_image_filename).convert_alpha(),(0,0))
				be_delay += 1
				pygame.mixer.music.fadeout(8500)
				if be_delay >= 80:
					self.screen.blit(pygame.image.load(happy_ending_image_filename).convert_alpha(),(0,0))
					pygame.mixer.music.load(he_music_filename) #播放音樂
					pygame.mixer.music.play(-1)	#-1是循環播放的意思

			"""
			請在這裡放可以讓程式偵測到要放動畫的東西
			"""
			self.event_loop()
			
			for i in range(0,len(self.tower1s)):
				self.tower1s[i].update(self.screen_rect) 
			for i in range(0,len(self.tower2s)):
				self.tower2s[i].update(self.screen_rect)
			for i in range(0,len(self.tower3s)):
				self.tower3s[i].update(self.screen_rect)	# update而已，還沒有bilt (下行執行render才有draw >> bilt)
			
			key = pygame.key.get_pressed() #按下鍵盤對應的鍵會發生對應的動畫
			if key[pygame.K_ESCAPE]:
				exit()
			if key[pygame.K_z]: #按z，牙刷攻擊
				for i in brush2_list :
					i.attack('left')
				for j in brush1_list :
					j.attack('right')
					
			if attack_tooth == True:
				if toothblood-sb > 0:		   #牙齒被攻擊，但血量仍>0
					tooth_test.be_attacked()			
					attack_tooth = False
				if toothblood-sb <= 0:		  #牙齒被攻擊，血量歸零，牙齒死亡
					tooth_dead = True
					attack_tooth = False
			if round_5_health <= 0 and toothblood-sb > 0:
				clean = True
			if tooth_dead == True:
				tooth_test.dead()
				tooth_dead = False
				decay = True	
			############################################
			#self.render() #上背景以及所有圖，動畫會update下一張
			############################################
			pygame.display.update()
			self.clock.tick(self.fps)	# Restrict framerate of program.
			
def main():
	global be_delay
	game_over = False #設定gameover的參數，初始值為F，遊戲進行中
	game_start = False #遊戲是否開始，初始值為F，遊戲尚未開始
	
	os.environ['SDL_VIDEO_CENTERED'] = '1'   # 使遊戲視窗在scerrn正中央出現
	pygame.init()		 # 初始化 pygame
	pygame.display.set_caption("萬聖夜驚魂")  # 設定 pygame 視窗標題 (caption)
	surface = pygame.display.set_mode((1000, 660)) # 設定 畫布(pygame 視窗)大小 (900 x 600)寬，高。因為其實是兩個參數，所以要用(( ))
	usefont = pygame.font.SysFont('simhei',25)  #設定使用字體，大小25，可用字體為'simhei'，'yumincho'，'simhei'最佳，70，72[標楷體]
	
	# 開始程式與使用者互動部分
	while (not game_over):  
		for event in pygame.event.get():  # 由 pygame 取得事件 (event)
			if (event.type == pygame.QUIT): #or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
			# 取得鍵盤事件的方法: pygame.KEYDOWN是當使用者按下鍵盤時觸發 ( pygame.KEYUP 是當使用放開鍵盤時觸發
				game_over = True
				sys.exit()
			if game_start == False:
				if be_delay < 15:
					begin_image = pygame.image.load(begin_image_filename)
					surface.blit(begin_image,(0,0))
					pygame.display.flip()
					be_delay += 1
				if be_delay >= 15:
					start_image = pygame.image.load(start_image_filename)
					surface.blit(start_image,(0,0))
					pygame.display.flip()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					game_start = True
					be_delay = 0
			if game_start == True:
				App().main_loop() # 執行App().__init__ 時，就會建置初始塔 在操作面板了
		
		if game_over == True:
			pygame.quit()  # end of 萬聖夜驚魂.py
			sys.exit()  # 關閉遊戲視窗
# 執行本程式檔案 (詳細說明 : http://technology-sea.blogspot.tw/2012/03/python-name-import.html?view=timeslide )
if __name__ == "__main__":
	main()
	
# 漱口水判定  跟其他塔重疊時有bug

# 用道路中心點list，放置牙齒時判斷向左或向右  >>  幾個角落有bug  再看要不要解決
# 牙刷不會自動一直打，改成手動操作打，損血判定還有問題 (也可順便增加範圍技功能，概念類似，只是要變成滑鼠操作而已)

# lag問題(牙刷問題，或怪物問題  怪物要能remove) addbrush 的for迴圈  或  add到group後的問題
# 音效 要加強可以加強


