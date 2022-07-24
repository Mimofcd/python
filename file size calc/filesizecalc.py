import re
from unittest import result


def estimateTextFileSize(bits,noofch):
    result=bits*noofch #bits
    if result<8:
            print(str(result)+"bits")
    elif (result>8 and result<8*pow(10,3)):
            print(str(result/8)+"bytes")
    elif result>8*pow(10,3) and result<8*pow(10,6):
            print(str(result/(8*pow(10,3)))+"kb")
    elif result>8*pow(10,6) and result<(8*pow(10,9)):
            print(str(result/(8*pow(10,6)))+"mb")
    elif result>8*pow(10,9) and result<(pow(8,12)):
            print(str(result/(8*pow(10,9)))+"gb")

def estimatePictureFileSize(color_depth,width,height):
    result=color_depth*width*height
    if result<8:
        print(str(result)+"bits")
    elif (result>8 and result<8*pow(10,3)):
            print(str(result/8)+"bytes")
    elif result>8*pow(10,3) and result<8*pow(10,6):
            print(str(result/(8*pow(10,3)))+"kb")
    elif result>8*pow(10,6) and result<(8*pow(10,9)):
            print(str(result/(8*pow(10,6)))+"mb")
    elif result>8*pow(10,9) and result<(pow(8,12)):
            print(str(result/(8*pow(10,9)))+"gb")

def estimateSoundFileSize(sample_rate,bit_depth,duration,channels):
    result=sample_rate*bit_depth*duration*channels
    if result<8:
        print(str(result)+"bits")
    elif (result>8 and result<8*pow(10,3)):
            print(str(result/8)+"bytes")
    elif result>8*pow(10,3) and result<8*pow(10,6):
            print(str(result/(8*pow(10,3)))+"kb")
    elif result>8*pow(10,6) and result<(8*pow(10,9)):
            print(str(result/(8*pow(10,6)))+"mb")
    elif result>8*pow(10,9) and result<(pow(8,12)):
            print(str(result/(8*pow(10,9)))+"gb")

def estimateGifFileSize(width,height,colour_depth,sample_rate,duration):
    result=width*height*colour_depth*sample_rate*duration
    if result<8:
        print(str(result)+"bits")
    elif (result>8 and result<8*pow(10,3)):
            print(str(result/8)+"bytes")
    elif result>8*pow(10,3) and result<8*pow(10,6):
            print(str(result/(8*pow(10,3)))+"kb")
    elif result>8*pow(10,6) and result<(8*pow(10,9)):
            print(str(result/(8*pow(10,6)))+"mb")
    elif result>8*pow(10,9):
            print(str(result/(8*pow(10,9)))+"gb")
def estimateMovieFileSize(width,height,colour_depth,frame_rate,duration,sample_rate,bit_depth,channel):
    result=width*height*colour_depth*frame_rate*duration+duration*bit_depth*channel
    if result<8:
        print(str(result)+"bits")
    elif (result>8 and result<8*pow(10,3)):
            print(str(result/8)+"bytes")
    elif result>8*pow(10,3) and result<8*pow(10,6):
            print(str(result/(8*pow(10,3)))+"kb")
    elif result>8*pow(10,6) and result<(8*pow(10,9)):
            print(str(result/(8*pow(10,6)))+"mb")
    elif result>8*pow(10,9):
            print(str(result/(8*pow(10,9)))+"gb")
    
estimateTextFileSize(8,3000)
estimateTextFileSize(16,12000)
estimatePictureFileSize(8,640,480)
estimatePictureFileSize(24,1920,1080)
estimateSoundFileSize(8000,16,30,1)
estimateSoundFileSize(44100,16,210,2)
estimateGifFileSize(150,150,4,4,6)  
estimateMovieFileSize(1920,1080,24,24,4500,48000,16,6)