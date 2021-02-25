import sys   
soundFile = r'Z:\Projects\North\North_Scratch\TD\Immortals.wav'    
def soundStart():    
    import winsound 
    winsound.PlaySound(soundFile, winsound.SND_ASYNC) 