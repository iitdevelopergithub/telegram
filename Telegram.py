import configparser
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import telethon
import sys
import csv
import traceback
import time
import random
import os, sys
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
