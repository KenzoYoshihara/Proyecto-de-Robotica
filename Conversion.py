print("Bienvenido al sistema de conversiones\nSeleccione con la tecla indicada para escoger.")
contador=1
while contador>0:
	print("Seleccione los Factores de conversion que desea convertir")
	print("1.  Factores de Conversion de Longitud.")
	print("2.  Factores de Conversion de Masa.")
	print("3.  Factores de Conversion de Tiempo.")
	print("4.  Factores de Conversion de Area.")
	print("5.  Factores de Conversion de Volumen.")
	print("6.  Factores de Conversion de Fuerza.")
	print("7.  Factores de Conversion de Trabajo.")
	print("8.  Factores de Conversion de Potencia.")
	print("9.  Factores de Conversion de Presion.")
	print("10. Factores de Conversion de Temperatura.")
	print("11. Factores de conversion de Caudal.")
	a=int(input("Nro= "))
	if a==1:
		contador=0
		while contador>=0:
			print("Factores de Conversion de Longitud.")
			a=float(input("Introduzca el numero que desea convertir= \n"))
			print("Seleccione la unidad\n")
			print("1.  Metro.\n2.  Centimetro.\n3.  Milimetro.")
			print("4.  Kilometro.\n5.  Pie.\n6.  Pulgada.")
			print("7.  Yarda.\n8.  Milla Terrestre.\n9.  Milla Marina.")
			print("10. Legua.\n11. Micron.\n12. Angstrom.")
			print("13. Año Luz.\n14. Parsec\n15.Atras...")
			b=int(input("Unidad= \n"))
			print("A que Unidad desea convertir.")
			print("1.  Metro.\n2.  Centimetro.\n3.  Milimetro.")
			print("4.  Kilometro.\n5.  Pie.\n6.  Pulgada.")
			print("7.  Yarda.\n8.  Milla Terrestre.\n9.  Milla Marina.")
			print("10. Legua.\n11. Micron.\n12. Angstrom.")
			print("13. Año Luz.\n14. Parsec\n15.Atras...")
			c=int(input("Unidad= \n"))
			if b==1 and c==1:
				print("De Metros a Metros.")
				print("1 Metro = 1 Metro")
				print(a," Metros.")
			else:
				if b==1 and c==2:
					print("De Metros a Centimetros.")
					print("1 Metro = 100 Centimetros.")
					z=a*100
					print(a," Metros equivalen a = ",z," Centimetros.")
				else:
					if b==1 and c==3:
						print("De Metros a Milimetros.")
						print("1 Metro = 1000 Milimetros.")
						z=a*1000
						print(a," Metros equivalen a= ",z," Milimetros.")
					else:
						if b==1 and c==4:
							print("De Metros a Kilometros.")
							print("1 Metro = 0.001 Kilometros.")
							z=a/1000
							print(a," Metros equivalen a= ",z," Kilometros.")
						else:
							if b==1 and c==5:
								print("De Metros a Pies.")
								print("1 Metro = 30.48 Pies.")
								z=a*30.48
								print(a," Metros equivalen a= ",z," Pies.")
							else:
								if b==1 and c==6:
									print("De Metros a Pulgadas.")
									print("1 Metro = 39.37 pulgadas.")
									z=a*39.37
									print(a," Metros equivalen a= ",z," Pulgadas.")
								else:
									if b==1 and c==7:
										print("De Metros a Yardas.")
										print("1 Metro = 1.0936 Yardas.") 
										z=a*1.0936
										print(a," Metros equivalen a= ",z," Yardas.")
									else:
										if b==1 and c==8:
											print("De Metros a Millas Terrestres.")
											print("1 Metro = 0.00022 Millas Terrestres.")
											z=a*0.000622
											print(a," Metros equivalen a= ",z," Millas Terrestres")
										else:
											if b==1 and c==9:
												print("De Metros a Millas Nauticas.")
												print("1 Metro = 0.00054 Millas Nauticas.")
												z=a*0.00054
												print(a," Metros equivalen a= ",z," Millas Nauticas.")
											else:
												if b==1 and c==10:
													print("De Metros a Leguas.")
													print("1 Metro = 0.0002 Leguas.")
													z=a*0.0002
													print(a," Metros equivalen a= ",z," Leguas.")
												else:
													if b==1 and c==11:
														print("De Metros a Micrones.")
														print("1 Metro =  1000000 Micrones.")
 														z=a*1000000
														print(a," Metros equivalen a= ",z," Micrones.")
													else:
														if b==1 and c==12:
															print("De Metros a Angstroms.")
															print("1 Metro = 10000000000 Angstroms.")
															z=a*10000000000
															print(a," Metros equivalen a= ",z," Angstroms.")
														else:
															if b==1 and c==13:
																print("De Metros a Años Luz.")
																print("1 Metro = 0.0000000000000001057 Años Luz.")
																z=a/0.0000000000000001057
																print(a," Metros equivalen a= ",z," Años Luz.")
															else:
																if b==1 and c==14:
																print("De Metros a Parsecs.")
																print("1 Metro = 0.0000000000000000324 Parsecs.")
																z=a/0.0000000000000000324
																print(a," Metros equivalen a= ",z," Parsecs.")
																else:
																	print("¿Seguro que deseas salir?")
																	a=int(input("1.Si\n2.no")
																	if a==1:
																		contador=contador-1
																	else:
																		if a==2:
																					contador=contador+1
																		else:
																			print("Perro")



					


				
				



