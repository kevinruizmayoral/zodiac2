import random
def my_view(request):
	return {'project':'zodiac'}
def home_view(request):
	if request.method=="POST":
		dia = request.POST["dia"]
		mes = request.POST["mes"]
		print "DATA=%s / %s"%(dia,mes)
		signezodiac = " "
		imatgezodiac = " "
		frasesort = random.randint(1,5)
		if frasesort==1:
			frasesort="Amor 100%"
		elif frasesort==2:
			frasesort="Salud 100%"
		elif frasesort==3:
			frasesort="Diners 100%"
		elif frasesort==4:
			frasesort="Moriras en 7 dies"
		elif frasesort==5:
			frasesort="Ets pobre"
		if dia and mes:
			if dia>="21" and mes=="3" or dia <="20" and mes=="4": 
				signezodiac = "Aries"
				imatgezodiac = "aries"
			elif dia>="21" and mes=="4" or dia<="21" and mes=="5":
				signezodiac = "Tauro"
				imatgezodiac = "tauro"
			elif dia>="22" and mes=="5" or dia<="21" and mes=="6":
				signezodiac = "Geminis"
				imatgezodiac = "geminis"
			elif dia>="22" and mes=="6" or dia<="22" and mes=="7":
				signezodiac = "Cancer"
				imatgezodiac = "cancer"
			elif dia>="23" and mes=="7" or dia<="22" and mes=="8":
				signezodiac = "Leo"
				imatgezodiac = "leo"
			elif dia>="23" and mes=="8" or dia<="22" and mes=="9":
				signezodiac = "Virgo"
				imatgezodiac = "virgo"
			elif dia>="23" and mes=="9" or dia<="22" and mes=="10":
				signezodiac = "Libra"
				imatgezodiac = "libra"
			elif dia>="23" and mes=="10" or dia<="22" and mes=="11":
				signezodiac = "Escorpio"
				imatgezodiac = "escorpio"
			elif dia>="23" and mes=="11" or dia<="21" and mes=="12":
				signezodiac = "Sagitario"
				imatgezodiac = "sagitario"
			elif dia>="22" and mes=="12" or dia<="20" and mes=="1":
				signezodiac = "Capricornio"
				imatgezodiac = "capricornio"
			elif dia>="21" and mes=="1" or dia<="19" and mes=="2":
				signezodiac = "Acuario"
				imatgezodiac = "acuario"
			elif dia>="20" and mes=="2" or dia<="20" and mes=="3":
				signezodiac = "Piscis"
				imatgezodiac = "piscis"
			return {'project':'zodiac','signe': signezodiac,'imatge': imatgezodiac , 'frase': frasesort}
	return {'project':'zodiac',"signe": ""}
		
	
