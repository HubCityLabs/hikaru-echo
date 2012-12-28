import bottle
import requests
import ConfigParser
import urllib
import winsound

### INITIALIZATION ###
# load configs
config = ConfigParser.ConfigParser()
config.read("server.cfg")

# set configs
host = config.get('Server', 'host')
port = config.getint('Server', 'port')

# set MaryTTS settings
marytts_host = config.get('MaryTTS', 'host')
marytts_port = config.get('MaryTTS', 'port')
marytts_locale = config.get('MaryTTS', 'locale')
marytts_voice = config.get('MaryTTS', 'voice')
marytts_voice_selections = config.get('MaryTTS', 'voice_selections')


### ROUTES ###
@bottle.route('/')
def index():
    return 'test'


@bottle.route('/speak/<speech_content>')
def speak(speech_content):
    """Speak using the MaryTTS engine
    the string that was sent"""

    url_string = ("http://" + marytts_host +
                  ":" + marytts_port +
                  "/process?INPUT_TYPE=TEXT"
                  "&OUTPUT_TYPE=AUDIO"
                  "&INPUT_TEXT=" + urllib.quote(speech_content) +
                  "&OUTPUT_TEXT="
                  "&effect_Volume_selected="
                  "&effect_Volume_parameters=amount%3A2.0%3B"
                  "&effect_Volume_default=Default"
                  "&effect_Volume_help=Help"
                  "&effect_TractScaler_selected="
                  "&effect_TractScaler_parameters=amount%3A1.5%3B"
                  "&effect_TractScaler_default=Default"
                  "&effect_TractScaler_help=Help"
                  "&effect_F0Scale_selected=on"
                  "&effect_F0Scale_parameters=f0Scale%3A2.0%3B"
                  "&effect_F0Scale_default=Default"
                  "&effect_F0Scale_help=Help"
                  "&effect_F0Add_selected="
                  "&effect_F0Add_parameters=f0Add%3A50.0%3B"
                  "&effect_F0Add_default=Default"
                  "&effect_F0Add_help=Help"
                  "&effect_Rate_selected="
                  "&effect_Rate_parameters=durScale%3A1.5%3B"
                  "&effect_Rate_default=Default"
                  "&effect_Rate_help=Help"
                  "&effect_Robot_selected=on"
                  "&effect_Robot_parameters=amount%3A50.0%3B"
                  "&effect_Robot_default=Default"
                  "&effect_Robot_help=Help"
                  "&effect_Whisper_selected="
                  "&effect_Whisper_parameters=amount%3A100.0%3B"
                  "&effect_Whisper_default=Default"
                  "&effect_Whisper_help=Help"
                  "&effect_Stadium_selected="
                  "&effect_Stadium_parameters=amount%3A100.0"
                  "&effect_Stadium_default=Default"
                  "&effect_Stadium_help=Help"
                  "&effect_Chorus_selected="
                  "&effect_Chorus_parameters=delay1%3A466%3Bamp1%3A0.54%3Bdelay2%3A600%3Bamp2%3A-0.10%3Bdelay3%3A250%3Bamp3%3A0.30"
                  "&effect_Chorus_default=Default&"
                  "effect_Chorus_help=Help"
                  "&effect_FIRFilter_selected="
                  "&effect_FIRFilter_parameters=type%3A3%3Bfc1%3A500.0%3Bfc2%3A2000.0"
                  "&effect_FIRFilter_default=Default"
                  "&effect_FIRFilter_help=Help"
                  "&effect_JetPilot_selected="
                  "&effect_JetPilot_parameters="
                  "&effect_JetPilot_default=Default"
                  "&effect_JetPilot_help=Help"
                  "&HELP_TEXT="
                  "&VOICE_SELECTIONS=" + marytts_voice_selections +
                  "&AUDIO_OUT=WAVE_FILE"
                  "&LOCALE=" + marytts_locale +
                  "&VOICE=" + marytts_voice +
                  "&AUDIO=WAVE_FILE")
    r = requests.get(url_string)
    winsound.PlaySound(r.content, winsound.SND_MEMORY)  # This is a Windows only solution. Need to find/test Linux solution for RPi.
    return 'I said "' + speech_content + '"'

### RUN THE SERVER ###
bottle.run(server='paste', host=host, port=port)
