para convertir desde el formato donde estan los tonos arriba al de chordpro
chordpro --a2crd vivir.crd 

para poner en notacion latina, hay que agregar al archivo los define de los
tonos en latin que estan en el archivo tonoslatin
chordpro vivir.cho --output vivir.pdf --transcode=latin
