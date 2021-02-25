'''
import sys   
soundFile = r'Z:\Projects\Strawberry\Strawberry_Scratch\TD\music\CD2.wav'     
def soundStart():     
    import winsound  
    winsound.PlaySound(soundFile,  winsound.SND_ASYNC) 
    
def music():        
    soundStart()
'''

'''
import subprocess
soundFile = r'Z:\Projects\Strawberry\Strawberry_Scratch\TD\music\said.mp3'
subprocess.Popen(soundFile, shell = True)
'''