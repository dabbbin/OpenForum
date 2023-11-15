from .base import * 

#ALLOWED_HOSTS = ['43.202.81.190']
ALLOWED_HOSTS = ['*']
#base_dir : /home/ubuntu/projects/mysite
STATIC_ROOT = BASE_DIR / 'static/'
#base.py staticfiles_dirs 와 중복 오류를 막기 위해 
STATICFILES_DIRS = []
DEBUG = False