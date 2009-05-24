# These variables are used to control image quality and performance.    
# See /usr/share/doc/nvidia-x11-drv-<version>/README.txt for more information.

# Setting this to 1 might prevent certain OpenGL apps from crasching.
setenv __GL_SINGLE_THREADED 0

# This setting controls full-scene anti aliasing.
# Depending on your chipset, different values give different types of FSAA.
setenv __GL_FSAA_MODE 0

# Anisotrpic filtering. This setting is also chip dependent, see above. 
setenv __GL_DEFAULT_LOG_ANISO 0

# Sync buffer swap with monitor refresh. A value > 0 enables.  
setenv __GL_SYNC_TO_VBLANK 0

# If you have more than one monitor, this setting determines which display
# should be synced.
setenv __GL_SYNC_DISPLAY_DEVICE 

