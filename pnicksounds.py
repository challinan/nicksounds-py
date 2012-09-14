__module_name__ = "nicksounds.py" 
__module_version__ = "1.1" 
__module_description__ = "Play custom sounds based on channel" 
 
import os
import xchat

# My first python program - probably 100 better ways to do this...
# Includes a command handler to enable and disable sounds without unloading the plugin
# /ns off or /ns on to disable/enable sounds

sounds_on = 1
play_cmd = "afplay"
sounds_dir = "/Users/chris/Library/Sounds"

# Associate sounds with channels here
sounds_dic = {'#mel' : 'mel_sound.wav',
			  '#codebench'  : 'morse-n.wav',
			  '#watercooler'  : '440-380-drop.wav',
			  '#montavista'  : 'bullet.wav',
			  '#marketing' : 'Purr.aiff',
			  '#platform' : 'chirp.wav',
			  '#test' : 'ringout.wav',
			  'hilite' : 'c-d-g.wav',
			  'other' : '440-short-dot.wav'}

mynick = xchat.get_prefs("irc_nick1")
print "mynick is %s - sounds are enabled" % mynick

def channel_msg_processor(word, word_eol, userdata):
	if (sounds_on == 0):
		return xchat.EAT_NONE

	current_channel = xchat.get_info("channel")
	current_nick = xchat.get_info("nick")
	
	sound_cmd = 'afplay ' + sounds_dir + '/'
	# print "Channel message received on %s" % (current_channel)
	if current_channel in sounds_dic:
		sound_cmd = sound_cmd + sounds_dic[current_channel]
	else:
		sound_cmd = sound_cmd + sounds_dic['other']

	os.system(sound_cmd)
	return xchat.EAT_NONE

# This hook is called whenever my nick appears in a channel message
def channel_hilite_processor(word, word_eol, userdata):
	if (sounds_on == 0):
		return xchat.EAT_NONE

	sound_cmd = 'afplay ' + sounds_dir + '/' + sounds_dic['hilite']
	os.system(sound_cmd)
	return xchat.EAT_NONE

def do_sound_control(word, word_eol, userdata):
	global sounds_on

	if ('off' in word):
		sounds_on = 0
		print "Nicksounds are OFF"
		return xchat.EAT_ALL

	if ('on' in word):
		sounds_on = 1
		print "Nicksounds are ON"
		return xchat.EAT_ALL

xchat.hook_print("Channel Message", channel_msg_processor)
xchat.hook_print("Channel Msg Hilight", channel_hilite_processor)
xchat.hook_print("Private Message", channel_hilite_processor)
xchat.hook_command("ns", do_sound_control)
