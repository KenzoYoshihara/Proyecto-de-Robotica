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
			print("1. Metro.\n2. Centimetro.\n3. Pie.\n4. Pulgada.\n5.Atras...")
			b=int(input("Unidad= \n"))
			print("A que Unidad desea convertir.")
			print("1.  Metro.\n2.  Centimetro.\n3.  Pie.\n4. Pulgada.\n5. Atras...")
			c=int(input("Unidad= \n"))
			if b==1 and c==1:
				print("De Metros a Metros.")
				print("1 Metro = 1 Metro")
				print(a," Metros equivalen a= ",a," Metros.")
			else:
				if b==1 and c==2:
					print("De Metros a Centimetros.")
					print("1 Metro = 100 Centimetros.")
					z=a*100
					print(a," Metros equivalen a = ",z," Centimetros.")
				else:
					if b==1 and c==3:
						print("De Metros a Pies.")
						print("1 Metro = 0.3048 Pies.")
						z=a*0.3048
						print(a," Metros equivalen a= ",z," Pies.")
					else:
						if b==1 and c==4:
							print("De Metros a Pulgadas.")
							print("1 Metro = 39.37 Pulgadas.")
							z=a/39.37
							print(a," Metros equivalen a= ",z," Pulgadas.")
						else:
							if b==2 and c==1:
								print("De Centimetros a Metros.")
								print("1 Centimetro = 0.01 Metros.")
								z=a*0.01
								print(a," Centimetros equivalen a= ",z," Metros.")
							else:
								if b==2 and c==2:
									print("De Centimetros a Centimetros.")
									print("1 Centimetro = 1 Centimetro.")
									print(a," Metros equivalen a= ",a," Centimetros.")
								else:
									if b==2 and c==3:
										print("De Centimetros a Pies.")
										print("1 Centimetro = 0.03281 Pies.") 
										z=a*0.03281
										print(a," Centimetros equivalen a= ",z," Pies.")
									else:
										if b==2 and c==4:
											print("De Centimetros a Pulgadas.")
											print("1 Centimetro = 0.3937 Pulgadas.")
											z=a*0.3937
											print(a," Centimetros equivalen a= ",z," Pulgadas.")
										else:
											if b==3 and c==1:
												print("De Pies a Metros.")
												print("1 Pie = 3.28084 Metros")
												z=a*3.28084
												print(a," Pies equivalen a= ",z," Metros.")
											else:
												if b==3 and c==2:
													print("De Pies a Centimetros.")
													print("1 Pie = 0.3048 Centimetros.")
													z=a*0.3048
													print(a," Pies equivalen a= ",z," Centimetros.")
												else:												
													if b==3 and c==4:
														print("De Pies a Pulgadas.")
														print("1 Pie =  12 Pulgadas.")
 														z=a*12
														print(a," Pies equivalen a= ",z," Pulgadas.")
													else:
														if b==4 and c==1:
															print("De Pulgadas a Metros.")
															print("1 Pulgada = 0.0254 Metros.")
															z=a*0.0254
															print(a," Pulgadas equivalen a= ",z," Metros.")
														else:
															if b==4 and c==2:
																print("De Pulgadas a Centimetros.")
																print("1 Pulgada = 2.54 Centimetros .")
																z=a*2.54
																print(a," Metros equivalen a= ",z," Años Luz.")
															else:
																if b==4 and c==3:
																print("De Pulgadas a Pies.")
																print("1 Pulgada = 0.0833 Pies.")
																z=a*0.0833
																print(a," Pulgadas equivalen a= ",z," Pies.")
																else:
																	if b==4 and c==4:
																		print("De pulgadas a Pulgadas.")
																		print("1 Pulgada = 1 Pulgada.")
																		print(a,"Pulgadas equivalen a= ",a," Pulgadas.")
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
