import time , os , transpositionDecryption , transpositionCeaser
def main():
    inputFilename=  'frankenstein.txt'
    outputFilename= 'frankenstein.encrypted.text'
    keys = 10
    mymode= 'encrypt'
    fileobj=open(inputFilename)
    content = fileobj.read()
    fileobj.close()
    print('%sing...' % (mymode.title()))
    starttime=time.time()
    if mymode=='encrypt':
        translated=transpositionCeaser.encryptmessage(content,keys)
    elif mymode=='decrypt':
        translated=transpositionDecryption.decrypted(content,keys)
    totaltime=round(time.time()-starttime,2)
    print('%sion : %s sec' %(mymode.title() , totaltime))
    outputFileobj=open(outputFilename,'w')
    outputFileobj.write(translated)
    outputFileobj.close()
    print('Done %sing %s (%s characters).' % (mymode, inputFilename, len(content)))
    print('%sed file is %s.' % (mymode.title(), outputFilename))
if __name__=='__main__':
    main()
