igital data consists of binary information and is stored as a collection of 0’s and 1’s. On a computer system, numbers, text, pictures, sound files, video clips and computer programs are all stored using binary code.

Storing text files in binary
Text files are stored using a character set such as ASCII code or UNICODE. The number of bits used to encode one character has an impact on the total number of characters included in the character set.
For instance:

ASCII code uses 7 bits per characters and contains 128 codes/characters.
Extended ASCII code uses 8 bits per characters and contains 256 codes/characters.
UNICODE uses either 2 Bytes (UTF-16) or 4 Bytes (UTF-32) per character and contains either 65,536 or 4,294,967,296 characters, enough to include all the characters and symbols used in every language worldwide.
Storing bitmap pictures in binary
A bitmap picture is a 2D grid of pixels of different colours. You can read more about how bitmap pictures are stored in binary on this post.

Two criteria will impact the file size of a bitmap picture:

The resolution: The number of pixels it contains which can be defined as: width in pixels x height in pixels. For instance a picture of 640 by 480 pixels would contain 640 x 480 = 307,200 pixels.
The colour depth: The number of bits used to encode the colour of one pixel. For instance a 1-bit colour depth means that the graphic can only include 2 colours (e.g. 1 = black, 0 = white), and 8-bit colour depth means that the graphic can include up to 256 colours, and a 3-Byte colour depth (RGB code) would include 16,777,216 colours.
Storing sound files in binary
An analogue sound wave can be digitalised using a process called sound sampling. You can find out more about sound sampling on this post.

Three criteria will impact the file size of a sound file:

The sample rate: The sample rate correspond to the number of samples being recorded per second. For instance a phone call would have a sample rate of 8kHz (8,000 samples per second) whereas an audio CD would record music with a sample rate of 44.1kHZ (44,000 samples per second) resulting in a higher quality sound.
The bit depth: The bit depths correspond to the number of bits used to record one sample. For instance retro-arcade games used to use 8-bit music. Old mobile phones used to use 16-bit ringtones. Higher quality sound files may use a 32-bit bit-depth or higher.
The duration: The duration of a the sound files in seconds will impact on the number of samples needed to record the sound file and hence it will have an impact on the file size.
Note that the above formula is used to estimate the file size of a mono sound file. some sound files use multiple channels such as stereo files (2 channels) or Dolby-surround sound files (6 channels). To estimate their file size, you need to multiply the above formula by the number of channels.
Also, similar to picture files, a sound file would also include some meta-data (sample rate, bit depth, number of channels) needed for the computer to interpret the data, however we will once again ignore this data in our file size estimation.
Programming Task
Your task is to write three procedures used to estimate the file size of text files, bitmap pictures and sound files as follows:

estimateTextFileSize() will take two parameters, the number of bits per character and the number of characters in the file. It will output the estimated file size using the formula provided earlier in this post.
estimatePictureFileSize() will take three parameters, the width and height of the picture in pixels and its colour depth. It will output the estimated file size using the formula provided earlier in this post.
estimateSoundFileSize() will take four parameters, the sample rate (in Hz), the bit depth, the duration (in seconds) and the number of channels. It will output the estimated file size using the formula provided earlier in this post.
Note that for all three procedures, the output information should be displayed using the most suitable unit (bits, Bytes, KB, MB or GB)