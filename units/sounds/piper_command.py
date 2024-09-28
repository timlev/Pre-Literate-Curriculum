import wave
from piper.voice import PiperVoice
wordlist = ['minnesota', 'fighters', 'kitchen,', 'backpack', 'rug', 'restroom', 'moves', 'usa', 'pencils', 'emergency?', 'oh', 'st', 'dresser', 'shopping', 'runny', 'scarf', 'what’s', 'whiteboard', 'janitor', 'no!', 'socks', 'leaking', 'i’m', 'erasers', 'mittens', 'ave', 'women’s', '612-543-6719', 'room,', 'bedroom,', 'it’s', 'look', 'elementary', 'ramsey', 'school', 'dc', 'to', '16', 'aids', 'restrooms', 'do', 'the', 'interpreter', '$900', '2', 'attack!', 'men’s', 'headache', 'babies', 'orange', 'factory', 'check-out', 'folders', 'shower', 'signature', 'hurts', 'don’t', 'clinic', 'food', 'closets', 'fit!', 'tub', 'bedrooms', 'paul', 'sandals', 'doesn’t', '3301', 'preschool', 'fridge', 'cashier', 'bhutan', 'al', 'dale', 'say,', 'aspirin', 'you”', '911', 'tapti', 'notebooks', '“thank', 'buys', 'ointment']

print(len(wordlist))
model = "/home/levtim/piper/en_US-lessac-medium.onnx"
voice = PiperVoice.load(model)

for word in wordlist:
    wav_file = wave.open(word + ".wav", "w")
    text = word
    audio = voice.synthesize(text, wav_file)
