oo000 = [ 'urllib' , 'urllib2' , 're' , 'os' , 'sys' , 'xbmcplugin' , 'xbmcgui' , 'xbmc' , 'TVClibs' , 'xbmcaddon' ]
ii = map ( __import__ , oo000 )
ii
if 51 - 51: IiI1i11I
__scriptname__ = "plugin.video.tvcatchup"
__author__ = 'dj_gerbil [tvc@killergerbils.co.uk]'
__svn_url__ = "http://tvcatchup-xbmc-addon.googlecode.com/svn/trunk/ tvcatchup-xbmc-addon-read-only"
__version__ = "1.3.5"
__phpurl__ = ii [ 8 ] . Ii ( "WVQvbHNDPXB3L3dyOUtJXVg1c3ApNHFpeC5qdj9fcTtUZmh6UFFmdGZ1ZHJrQFksS0h+Mld4Mm1meHJkOVtvXTgwbXFVZWV4ZmMyMGtVRWg+ZSB0a10jIGsgcyJMbSlSMg==" , 3 )
__cachefolder__ = "addon_data"
__settings__ = ii [ 9 ] . Addon ( id = 'plugin.video.tvcatchup' )
__addon__ = ii [ 9 ].Addon('plugin.video.tvcatchup')
if 16 - 16: iI11I1II1I1I + iiiii % ii1I - II1 - O0ooooo00oOO - ooOoO
def o0Oo ( ) :
 i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ ) )
 IIiIiII11i = i1IiI1I11 + ii [ 3 ] . sep + __scriptname__
 if not ii [ 3 ] . path . isdir ( IIiIiII11i ) :
  try :
   print "%s doesn't exist, creating" % IIiIiII11i
   ii [ 3 ] . makedirs ( IIiIiII11i )
  except IOError , o0oOOo0O0Ooo :
   print "Couldn't create %s, %s" % ( IIiIiII11i , str ( o0oOOo0O0Ooo ) )
   raise
 IIiIiII11i = i1IiI1I11 + ii [ 3 ] . sep + __scriptname__ + ii [ 3 ] . sep + 'TVC_cache'
 if not ii [ 3 ] . path . isdir ( IIiIiII11i ) :
  try :
   print "%s doesn't exist, creating" % IIiIiII11i
   ii [ 3 ] . makedirs ( IIiIiII11i )
  except IOError , o0oOOo0O0Ooo :
   print "Couldn't create %s, %s" % ( IIiIiII11i , str ( o0oOOo0O0Ooo ) )
   raise
 i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
 I1ii11iIi11i = ii [ 3 ] . path . join ( i1IiI1I11 , 'TVC_cache' )
 I1IiI = __settings__ . getSetting ( 'uname' )
 o0OOO = __settings__ . getSetting ( 'pwd' )
 if o0OOO . find ( '.enc.' ) < 0 :
  print "Not Encoded"
  iIiiiI = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( "bXFjQzRNcHJzb2hmTF8/OGBNbmkuVWRyQHRqZ20tS19MKmNoXnVxdSk9aWcoXE8ydlAmcnlCaGRmcHJjQk1laGpjIHcqYSMgdiBAInJeeU1A" , 3 ) + o0OOO )
  Iii1ii1II11i = iIiiiI . read ( )
  __settings__ . setSetting ( 'pwd' , Iii1ii1II11i + '.enc.' )
 iI111iI = __settings__ . getSetting ( 'whatson' )
 if ( not I1IiI or I1IiI == '' ) or ( not o0OOO or o0OOO == '' ) :
  IIiIiII11i = ii [ 6 ] . Dialog ( )
  IIiIiII11i . ok ( 'Welcome to the TVCatchup plugin.' , 'To start using this plugin first go to www.TVCatchup.com' , 'and create a (free) account.' )
  __settings__ . openSettings ( )
  if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
def Oo ( ) :
 I1IiI = __settings__ . getSetting ( 'uname' )
 o0OOO = __settings__ . getSetting ( 'pwd' )
 if o0OOO . find ( '.enc.' ) > 0 :
  print "Encoded"
  I1Ii11I1Ii1i = __settings__ . getSetting ( 'pwd' )
  o0OOO = I1Ii11I1Ii1i . rstrip ( '.enc.' )
 else:
  print "Not Encoded"
  iIiiiI = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( "bXFjQzRNcHJzb2hmTF8/OGBNbmkuVWRyQHRqZ20tS19MKmNoXnVxdSk9aWcoXE8ydlAmcnlCaGRmcHJjQk1laGpjIHcqYSMgdiBAInJeeU1A" , 3 ) + o0OOO )
  Iii1ii1II11i = iIiiiI . read ( )
  __settings__ . setSetting ( 'pwd' , Iii1ii1II11i + '.enc.' )
  print "Encoded"
  I1Ii11I1Ii1i = __settings__ . getSetting ( 'pwd' )
  o0OOO = I1Ii11I1Ii1i . rstrip ( '.enc.' )
 iIiiiI = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( 'd2pjQzwycHJzb2hmQ3hXUD9cbmk1ZWRyQHRqZzxjOFV2SGNoKnlxdSk9aWMxQ2gzaChzeVcoeCZ3ZWt0LnFRbkY8IEFANiMgIyAjIlt2dEtk' , 3 ) + I1IiI + "&pass=" + o0OOO )
 Iii1ii1II11i = iIiiiI . read ( )
 Ooo = ii [ 2 ] . compile ( 'authKey] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 if len ( Ooo ) <= 0 :
  o0oOoO00o = ii [ 2 ] . compile ( ' #FFFFFF">(.+?)</div>' ) . findall ( Iii1ii1II11i )
  IIiIiII11i = ii [ 6 ] . Dialog ( )
  IIiIiII11i . ok ( 'TVCatchup Plugin Error.' , o0oOoO00o [ 0 ] , 'Please check your settings.' )
 else :
  return Ooo [ 0 ]
  if 43 - 43: O0OOo . II1Iiii1111i
def i1IIi11111i ( authkey , name ) :
 iIiiiI = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( 'ZUJjQz4scHJzb2hmaEJQS2Jnbmk6WmRyQHRqZ0MyNUpNOWNoTk5xdSk9aWVpbnczSmZubClfbGxka3EiO2lCWlY=' , 3 ) + authkey )
 Iii1ii1II11i = iIiiiI . read ( )
 o000o0o00o0Oo = ii [ 2 ] . compile ( 'channel_streamer] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 oo = ii [ 2 ] . compile ( 'channel_file] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1ii = ii [ 2 ] . compile ( 'title] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 if len ( o000o0o00o0Oo ) <= 0 :
  o0oOoO00o = ii [ 2 ] . compile ( ' #FFFFFF">(.+?)</div>' ) . findall ( Iii1ii1II11i )
  IIiIiII11i = ii [ 6 ] . Dialog ( )
  IIiIiII11i . ok ( 'TVCatchup Plugin Error.' , o0oOoO00o [ 0 ] , 'Please contact DJ_Gerbil or TVC Support for advice.' )
 else :
  ii [ 7 ] . executebuiltin ( "xbmc.Notification('Now Playing...'," + name [ 0 : name . find ( "-" ) ] + " - " + IiII1I1i1i1ii [ 0 ] + " , 10000, %s)" % ( ii [ 3 ] . path . join ( __addon__.getAddonInfo('path') , "icon.png" ) , ) )
  IIIII = o000o0o00o0Oo [ 0 ] . replace ( "\\/" , "/" ) + "/" + oo [ 0 ]
  I1 = __settings__ . getSetting ( 'libRTMP' )
  O0OoOoo00o = str ( IIIII ) . split ( "/" )
  IIIII = O0OoOoo00o [ 0 ] + "//" + O0OoOoo00o [ 2 ] + "/" + O0OoOoo00o [ 3 ] + "/" + O0OoOoo00o [ 4 ] + "/" + O0OoOoo00o [ 5 ] + "/" + O0OoOoo00o [ 6 ] + "/" + O0OoOoo00o [ 7 ] + "/" + O0OoOoo00o [ 8 ] + " app=" + O0OoOoo00o [ 3 ] + "/" + O0OoOoo00o [ 4 ] + "/" + O0OoOoo00o [ 5 ] + "/" + O0OoOoo00o [ 6 ] + "/" + O0OoOoo00o [ 7 ] + "/" + O0OoOoo00o [ 8 ] + " playpath=" + O0OoOoo00o [ 9 ] + " live=1"
  iiiI11 = ii [ 6 ] . ListItem ( IiII1I1i1i1ii [ 0 ] )
  iiiI11 . setIconImage ( 'defaultVideo.png' )
  i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
  OOooO = ii [ 3 ] . path . join ( i1IiI1I11 , 'TVC_cache' , name [ 0 : name . find ( ":" ) ] + "enabled.png" )
  iiiI11 . setThumbnailImage ( OOooO )
  ii [ 7 ] . Player ( ii [ 7 ] . PLAYER_CORE_DVDPLAYER ) . play ( IIIII , iiiI11 )
  if 58 - 58: i11iiII + OooooO0oOO + oOo0 / oo0Ooo0
def I1I11I1I1I ( ) :
 Ooo = Oo ( )
 i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
 I1ii11iIi11i = ii [ 3 ] . path . join ( i1IiI1I11 , 'TVC_cache' )
 iI111iI = __settings__ . getSetting ( 'whatson' )
 iIiiiI = ii [ 1 ] . urlopen ( ii [ 8 ] . Ii ( 'Tj4vbDlwPXB3L3d5OVY9TktbY3tNLHl0emExdjt4azlNU2NnZ2sxcGtveG9NLzhhN0FoMzNVZmFCZWY/NXVDSVxjIDU9YSMgIyAjIk0wYSo2' , 3 ) )
 OooO0OO = iIiiiI . read ( )
 iiiIi = ii [ 2 ] . compile ( '"channel_id":"(.+?)"' ) . findall ( OooO0OO )
 IiIIIiI1I1 = ii [ 2 ] . compile ( '"channel_name":"(.+?)"' ) . findall ( OooO0OO )
 OoO000 = ii [ 2 ] . compile ( '"channel_status":"(.+?)"' ) . findall ( OooO0OO )
 IIiiIiI1 = ii [ 2 ] . compile ( '"channel_logo":"(.+?)"' ) . findall ( OooO0OO )
 iiiI11 = ii [ 2 ] . compile ( '"now":{"programme_name":"(.+?)"' ) . findall ( OooO0OO )
 iiIiIIi = ii [ 2 ] . compile ( '"programme_start":"(.+?)"' ) . findall ( OooO0OO )
 ooOoo0O = ii [ 2 ] . compile ( '"programme_end":"(.+?)"' ) . findall ( OooO0OO )
 OooO0 = 0
 for II11iiii1Ii in range ( 0 , len ( iiiIi ) ) :
  if OoO000 [ II11iiii1Ii ] == "enabled" :
   if not ii [ 3 ] . path . exists ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "enabled.png" ) :
    iIiiiI = ii [ 1 ] . urlopen ( IIiiIiI1 [ II11iiii1Ii ] . replace ( "\\/" , "/" ) )
    Iii1ii1II11i = iIiiiI . read ( )
    file = open ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "enabled.png" , mode = "wb" )
    file . write ( Iii1ii1II11i )
    file . close ( )
   if iI111iI == "true" :
    OO0o ( str ( II11iiii1Ii + 1 ) + ": " + IiIIIiI1I1 [ II11iiii1Ii ] + " - " + iiiI11 [ OooO0 ] . replace ( "\\" , "" ) + " - From: " + iiIiIIi [ OooO0 ] [ 11 : 16 ] + " - To: " + ooOoo0O [ OooO0 ] [ 11 : 16 ] , '&auth=' + Ooo + '&chan=' + iiiIi [ II11iiii1Ii ] , 3 , I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "enabled.png" , len ( iiiIi ) )
    OooO0 = OooO0 + 1
   else :
    OO0o ( str ( II11iiii1Ii + 1 ) + ": " + IiIIIiI1I1 [ II11iiii1Ii ] , '&auth=' + Ooo + '&chan=' + iiiIi [ II11iiii1Ii ] , 3 , I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "enabled.png" , len ( iiiIi ) )
  else :
   if not ii [ 3 ] . path . exists ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "disabled.png" ) :
    iIiiiI = ii [ 1 ] . urlopen ( IIiiIiI1 [ II11iiii1Ii ] . replace ( "\\/" , "/" ) )
    Iii1ii1II11i = iIiiiI . read ( )
    file = open ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "disabled.png" , mode = "wb" )
    file . write ( Iii1ii1II11i )
    file . close ( )
   OO0o ( str ( II11iiii1Ii + 1 ) + ": " + IiIIIiI1I1 [ II11iiii1Ii ] + " - Channel Is Currently Offline" , '&auth=' + Ooo + '&chan=' + iiiIi [ II11iiii1Ii ] , 3 , I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "disabled.png" , len ( iiiIi ) )
   OooO0 = OooO0 + 1
   if 82 - 82: i1I1i1Ii11 . iiiii - i11iiII * O00oOoOoO0o0O + Oo0ooO0oo0oO + ooOoO
def O0O ( ) :
 O00o0OO = [ ]
 I11i1 = ii [ 4 ] . argv [ 2 ]
 if len ( I11i1 ) >= 2 :
  iIi1ii1I1 = ii [ 4 ] . argv [ 2 ]
  o0 = iIi1ii1I1 . replace ( '?' , '' )
  if ( iIi1ii1I1 [ len ( iIi1ii1I1 ) - 1 ] == '/' ) :
   iIi1ii1I1 = iIi1ii1I1 [ 0 : len ( iIi1ii1I1 ) - 2 ]
  I11II1i = o0 . split ( '&' )
  O00o0OO = { }
  for IIIIIooooooO0oo in range ( len ( I11II1i ) ) :
   IIiiiiiiIi1I1 = { }
   IIiiiiiiIi1I1 = I11II1i [ IIIIIooooooO0oo ] . split ( '=' )
   if ( len ( IIiiiiiiIi1I1 ) ) == 2 :
    O00o0OO [ IIiiiiiiIi1I1 [ 0 ] ] = IIiiiiiiIi1I1 [ 1 ]
 return O00o0OO
 if 13 - 13: oOo0 + O0oo0OO0 - ii1I + oo0Ooo0 . OooooO0oOO + O00oOoOoO0o0O
def OO0o ( name , url , mode , iconimage , total ) :
 Ii = ii [ 4 ] . argv [ 0 ] + "?url=" + ii [ 0 ] . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + ii [ 0 ] . quote_plus ( name )
 oo0O0oOOO00oO = True
 OooOooooOOoo0 = ii [ 6 ] . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOooooOOoo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oo0O0oOOO00oO = ii [ 5 ] . addDirectoryItem ( handle = int ( ii [ 4 ] . argv [ 1 ] ) , url = Ii , listitem = OooOooooOOoo0 , isFolder = False , totalItems = total )
 return oo0O0oOOO00oO
 if 71 - 71: oo0Ooo0 % II % O0OOo
def oO00ooo0 ( ) :
 iIi1ii1I1 = O0O ( )
 o00 = o0Oo ( )
 OooOooo = None
 O000oo0O = None
 OOOO = None
 if 10 - 10: O0OOo / ooOoO * O0OOo
 try :
  OooOooo = ii [ 0 ] . unquote_plus ( iIi1ii1I1 [ "url" ] )
 except :
  pass
 try :
  O000oo0O = ii [ 0 ] . unquote_plus ( iIi1ii1I1 [ "name" ] )
 except :
  pass
 try :
  OOOO = int ( iIi1ii1I1 [ "mode" ] )
 except :
  pass
  if 29 - 29: I1i1iI1i % ooOoO + i1I1i1Ii11 / Oo0ooO0oo0oO + O0OOo * Oo0ooO0oo0oO
 if OOOO == None or OooOooo == None or len ( OooOooo ) < 1 :
  I1I11I1I1I ( )
 elif OOOO == 1 :
  I1I11I1I1I ( )
 elif OOOO == 3 :
  i1IIi11111i ( OooOooo , O000oo0O )
  if 42 - 42: i11iiII + II
 ii [ 5 ] . endOfDirectory ( int ( ii [ 4 ] . argv [ 1 ] ) )
