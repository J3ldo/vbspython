from pathlib import Path

class tts:
    def __init__(self, outer):
        self.outer = outer
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                "Set tts = CreateObject(\"SAPI.SpVoice\")\n"
            )

    def rate(self, rate=0):
        if int(rate) > 10 or int(rate) < -10:
            raise Exception("You can't have the rate above 10 or under -10")
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Rate = {rate}\n"
            )

    def say(self, text):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Speak \"{text}\"\n"
            )

    def speak(self, text):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Speak \"{text}\"\n"
            )

    def voice(self, speaker):
        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"Set tts.Voice = tts.GetVoices.Item({speaker})\n"
            )

    def volume(self, volume):
        if int(volume) > 100 or int(volume) < 0:
            raise Exception("Volume can't be higher then 100 or lower then 0")

        with open(f'{str(Path(__file__).absolute())[:-11]}\\files\\{self.outer.filename}.vbs', 'a') as f:
            f.write(
                f"tts.Volume = {volume}\n"
            )
