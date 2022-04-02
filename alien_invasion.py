import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvation:
	"""整个游戏的资源和行为"""

	def __init__(self):
		"""初始化一些基本的信息和资源"""
		pygame.init()

		pygame.display.set_caption("外星人入侵！！！吼吼吼")
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_height = self.screen.get_rect().height
		self.settings.screen_width = self.screen.get_rect().width
		self.ship = Ship(self)

	def run_game(self):
		"""游戏开始运行的主循环"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		"""鼠标和键盘响应的事件"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			
	def _check_keydown_events(self, event):
		"""响应按键"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()

	def _check_keyup_events(self, event):
		"""响应松开"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		"""更新屏幕和切换新屏幕"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()
			# 绘制屏幕可见


if __name__ == '__main__':
	ai = AlienInvation()
	ai.run_game()
# 单独作为一个主文件来运行
