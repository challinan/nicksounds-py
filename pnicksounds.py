__module_name__ = "helloworld" 
__module_version__ = "1.0" 
__module_description__ = "Python module example" 
 
import os
import xchat

mynick = "challinan"
play_cmd = "afplay"
sounds_dir = "/Users/chris/Library/Sounds"

# Associate sounds with channels here
nick_sound = "c-d-g.wav"
mel_sound = "mel_sound.wav";
codebench_sound = "gmorse-n.wav"
watercooler_sound = "g440-380-drop.wav"
montavista_sound = "gbullet.wav"
marketing_sound = "gPurr.aiff"
plat_sound = "gchirp.wav"
ae_sound = "gmorse-a.wav"
other_sound = "g440-short-dot.wav"

sounds_dic = {'#mel' : 'mel_sound.wav',
			  '#codebench'  : 'morse-n.wav',
			  '#watercooler'  : '440-380-drop.wav',
			  '#montavista'  : 'bullet.wav',
			  '#marketing' : 'Purr.aiff',
			  '#platform' : 'chirp.wav',
			  '#test' : 'ringout.wav',
			  '#other' : '440-short-dot.wav'}

# xchat.prnt("This is xchat.prnt")

nick = xchat.get_prefs("irc_nick1")
#if xchat.nickcmp(nick, mynick) == 0: 
#	print "They are the same!"

# This function retrieves the xchat setting (see /set)
# print "Current preferred nick:", xchat.get_prefs("irc_nick1")

# This code produces a list of channels
# channel_list = xchat.get_list("channels") 
# if channel_list: 
#     print "--- channel list ------------------" 
#     for i in channel_list: 
#        print i.channel

# This code produces a list of users in a channel
# user_list = xchat.get_list("users")
# if user_list:
# 	print "--- user list ---------------------"
#	for i in user_list:
# 		print i.nick

def channel_processor(word, word_eol, userdata):
	current_channel = xchat.get_info("channel")
	current_nick = xchat.get_info("nick")
	
	if mynick in word:
		os.system('afplay /Users/chris/Library/Sounds/c-d-g.wav')
		return

	sound_cmd = 'afplay ' + sounds_dir + '/'
	# print "Channel message received on %s" % (current_channel)
	if (current_channel == '#marketing'):
		sound_cmd = sound_cmd + sounds_dir + Purr.aiff
		print sound_cmd

	os.system(sound_cmd)
	#os.system('afplay /Users/chris/Library/Sounds/Purr.aiff')

xchat.hook_print("Channel Message", channel_processor)
