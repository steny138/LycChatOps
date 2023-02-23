import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

# Errbot will start in text mode (console only mode) and will answer commands from there.
BACKEND = "Text"

BOT_DATA_DIR = r"/Users/yuchenliu/Documents/projects/lyc_chatops/lyc_chatops/data"
BOT_EXTRA_PLUGIN_DIR = r"/Users/yuchenliu/Documents/projects/lyc_chatops/lyc_chatops/plugins"

BOT_LOG_FILE = r"/Users/yuchenliu/Documents/projects/lyc_chatops/lyc_chatops/errbot.log"
BOT_LOG_LEVEL = logging.INFO

BOT_ADMINS = (
    "@SKY",
)
