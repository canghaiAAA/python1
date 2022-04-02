import pygame


class Ship:

	def __init__(self, ai_game):
		"""初始化飞船和初始位置"""
		# 定义屏幕
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

        # 定义飞船和屏幕位置中下方
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

        # 控制左右移动
		self.moving_right = False
		self.moving_left = False

        # x储存小数值
		self.x = float(self.rect.x)

	def update(self):
		"""飞船移动"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0 :
			self.x -= self.settings.ship_speed

		self.rect.x = self.x

	def blitme(self):
		"""绘制飞船"""
		self.screen.blit(self.image,self.rect)