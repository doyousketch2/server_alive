#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
##=========================================================
##  server_alive.py                                Oct 2018
##
##  Eli Innis   @Doyousketch2      Doyousketch2 @ yahoo.com
##
##  GNU GPLv3                 gnu.org/licenses/gpl-3.0.html

""" required  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

##  sudo apt-get install fping

"""  libs  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

import time
import os
import gi                         ##  GObject Introspection
gi .require_version( 'Gtk', '3.0' )
from gi .repository import Gtk             ##  GIMP Toolkit
from gi .repository import Gdk             ##  GIMP Drawkit
from subprocess import Popen, PIPE

""" vars  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

server  = 'hometownserver.com'

minutes_between_ping  = 30
seconds_between_ping  = minutes_between_ping *60

fping  = ['fping', '-e', '--timeout=333', server]

default_width   = 400
default_height  = 200

ver    = '1.6'
appname  = os .path .basename(__file__)
window  = Gdk .get_default_root_window()

""" functions  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

class MainWindow( Gtk .Window ):

    def __init__( self ):
        Gtk .Window .__init__( self,  title = appname )

        horiz_box, vert_box  = 0, 1
        container  = Gtk .Box .new( vert_box, 0 )
        self .add( container )

        label  = Gtk .Label .new()
        label .set_markup( "<span foreground='blue' size='30000' font_weight='bold' underline='double'>It's Alive!</span>" )
        container .pack_start( label, True, True, 0 )

        ok  = Gtk .Button( label = 'OK' )
        ok .connect( 'clicked',  self .ok_clicked )
        container .pack_start( ok, False, False, 0 )

    def ok_clicked( self,  widget ):
        self .destroy()

"""  main ping loop  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

ping  = Popen( fping,  stdout=PIPE,  stderr=PIPE )
stdout, stderr = ping .communicate()

while stderr is not None and len(stdout) > 8 and stdout[-12:-1] == 'unreachable':

  current_time  = time .strftime( '%-H :%M',  time .localtime() )
  print( '{} ~ {}' ).format( current_time, stdout.rstrip() )

  time .sleep( seconds_between_ping )
  ping  = Popen( fping,  stdout=PIPE,  stderr=PIPE )
  stdout, stderr = ping .communicate()

"""  popup  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

if stderr:
  print( '{} ~ {}' ).format( current_time, stderr )
else:
  win  = MainWindow()
  win .connect( 'destroy',  Gtk .main_quit )
  win .set_default_size( default_width,  default_height )
  win .set_position( Gtk .WindowPosition .CENTER_ALWAYS )
  win .set_title( appname )
  win .show_all()
  Gtk .main()

"""  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
