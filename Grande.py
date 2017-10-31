print("Bienvenido al Sistema de Factores de Conversion.")
var=0
while var>=0:	
	print("Seleccione los Factores de Conversion que desea convertir.\n1.  Factores de Conversion de Longitud.")
	print("2.  Factores de Conversion de Masa.\n3.  Factores de Conversion de Tiempo.\n4.  Factores de Conversion de Area.\n5.  Factores de Conversion de Volumen.")
	print("6.  Factores de Conversion de Fuerza.\n7.  Factores de Conversion de Energia.\n8.  Factores de Conversion de Potencia.\n9.  Factores de Conversion de Presion.")
	print("10. Factores de Conversion de Temperatura.\n11. Sistemas de Numeros.\n12. Salir.\n")
	a=int(input("Numero=\n"))
	contador=0
	if a==1:
		contador=0
		while contador>=0:
			print("Factores de Conversion de Longitud.")
			a=float(input("Introduzca el numero que desea convertir.\n"))
			print("Seleccione la unidad.\n1. Metro.\n2. Centimetro.\n3. Pie.\n4. Pulgada.")
			b=int(input("Unidad=\n"))
			print("¿A que unidad desea convertir?\n1. Metro.\n2. Centimetro.\n3. Pie.\n4. Pulgada.\n5. Atras...")
			c=int(input("Unidad=\n"))
			if b==1 and c==1:
				print("De Metros a Metros.\n1 Metro = 1 Metro.\n",a," Metros equivalen a = ",a," Metros.")
			else:
				if b==1 and c==2:
					print("De Metros a Centimetros.\n1 Metro = 100 Centimetros.")
					z=a*100
					print(a," Metros equivalen a = ",z," Centimetros.")
				else:
					if b==1 and c==3:
						print("De Metros a Pies.\n1 Metro = 3.281 Pies.")
						z=a*3.281
						print(a," Metros equicalen a = ",z," Pies.")
					else:
						if b==1 and c==4:
							print("De Metros a Pulgadas.\n1 Metro = 39.37 Pulgadas.")
							z=a*39.37
							print(a," Metros equivalen a = ",z," Pulgadas.")
						else:
							if b==2 and c==1:
								print("De Centimetros a Metros.\n1 Centimetro = 0.01 Metros.")
								z=a*0.01
								print(a," Centimetros equivalen a = ",z," Metros.")
							else:
								if b==2 and c==2:
									print("De Centimetros a Centimetros.\n1 Centimetro = 1 Centimetro.")
									print(a," Centimetros equivalen a = ",a," Centimetros.")
								else:
									if b==2 and c==3:
										print("De Centimetros a Pies.\n1 Centimetro = 0.0328 Pies.")
										z=a*0.0328
										print(a," Centimetros equivalen a = ",z," Pies")
									else:
										if b==2 and c==4:
											print("De Centimetros a Pulgadas.\n1 Centimetro = 0.3937 Pulgadas.")
											z=a*0.3937
											print(a," Centimetros equivalen a = ",z," Pulgadas.")
										else:
											if b==3 and c==1:
												print("De Pies a Metros.\n1 Pie = 0.3048 Metros.")
												z=a*0.3048
												print(a," Pies equivalen a = ",z," Metros.")
											else:
												if b==3 and c==2:
													print("De Pies a Centimetros.\n1 Pie = 30.48 Centimetros.")
													z=a*30.48
													print(a," Pies equivalen a = ",z," Centimetros.")
												else:
													if b==3 and c==3:
														print("De Pies a Pies.\n1 Pie = 1 Pie.\n",a," Pies equivalen a = ",a," Pies.")
													else:
														if b==3 and c==4:
															print("De Pies a Pulgadas.\n1 Pie = 12 Pulgadas.")
															z=a*12
															print(a," Pies equivalen a = ",z," Pulgadas.")
														else:
															if b==4 and c==1:
																print("De Pulgadas a Metros.\n1 Pulgada = 0.0254 Metros.")
																z=a*0.0254
																print(a," Pulgadas equivalen a = ",z," Metros.")
															else:
																if b==4 and c==2:
																	print("De Pulgadas a Centimetros.\n1 Pulgada = 2.54 Centimetros.")
																	z=a*2.54
																	print(a," Pulgadas equivalen a = ",z," Centimetros.")
																else:
																	if b==4 and c==3:
																		print("De Pulgadas a Pies.\n1 Pulgada = 0.0833 Pies")
																		z=a*0.083333333
																		print(a," Pulgadas equivalen a = ",z," Pies.")
																	else:
																		if b==4 and c==4:
																			print("De Pulgadas a Pulgadas.\n1 Pulgada = 1 Pulgada.")
																			print(a," Pulgadas equivalen a = ",a," Pulgadas.")
																		else:
																			if c==5:
																				print("¿Estas seguro de salir de Factores de Conversion de Longitud?")
																				a=int(input("1. Si.\n2. No.\n"))
																				if a==1:
																					contador-=1
																				else:
																					if a==2:
																						contador+=1
																					else:
																						print("Solo puedes escoger entre 1 - 2.")
																			else:
																				print("Solo puedes escoger entre 1 - 5.")
	else:
		if a==2:
			contador1=0
			while contador1>=0:
				print("Factores de Conversion de Masa.")
				a=float(input("Introduzca el numero que desea convertir.\n"))
				print("Seleccione la unidad.\n1. Gramo.\n2. Kilogramo.\n3. Libra.\n4. Onza.")
				b=int(input("Unidad=\n"))
				print("¿A que unidad desea convertir?\n1. Gramo.\n2. Kilogramo.\n3. Libra.\n4. Onza.\n5. Atras...")
				c=int(input("Unidad=\n"))
				if b==1 and c==1:
					print("De Gramos a Gramos.\n1 Gramo = 1 Gramo.\n",a," Gramos equivalen a = ",a," Gramos.")
				else:
					if b==1 and c==2:
						print("De Gramos a Kilogramos.\n1 Gramo = 0.001 Kilogramos.")
						z=a/1000
						print(a," Gramos equivalen a = ",z," Kilogramos.")
					else:
						if b==1 and c==3:
							print("De Gramos a Libras.\n1 Gramo = 0.0022046 Libras.")
							z=a/453.6
							print(a," Gramos equivalen a = ",z," Libras.")
						else:
							if b==1 and c==4:
								print("De Gramos a Onzas.\n1 Gramo = 0.03531 Onzas.")
								z=a/28.32
								print(a," Gramos equivalen a = ",z," Onzas.")
							else:
								if b==2 and c==1:
									print("De Kilogramos a Gramos.\n1 Kilogramo = 1000 Gramos.")
									z=a*1000
									print(a," Kilogramos equivalen a = ",z," Gramos.")
								else:
									if b==2 and c==2:
										print("De Kilogramos a Kilogramos.\n1 Kilogramo = 1 Kilogramo.\n",a," Kilogramos equivalen a = ",a," Kilogramos.")
									else:
										if b==2 and c==3:
											print("De Kilogramos a Libras.\n1 Kilogramo = 2.205 Libras.")
											z=a*2.205
											print(a," Kilogramos equivalen a = ",z," Libras")
										else:
											if b==2 and c==4:
												print("De Kilogramos a Onzas.\n1 Kilogramo = 35.28 Onzas.")
												z=a*35.28
												print(a," Kilogramos equivalen a = ",z," Onzas.")
											else:
												if b==3 and c==1:
													print("De Libras a Gramos.\n1 Libra = 453.6 Gramos.")
													z=a*453.6
													print(a," Libras equivalen a = ",z," Gramos.")
												else:
													if b==3 and c==2:
														print("De Libras a Kilogramos.\n1 Libra = 0.4535 Kilogramos.")
														z=a*0.453515
														print(a," Libras equivalen a = ",z," Kilogramos.")
													else:
														if b==3 and c==3:
															print("De Libras a Libras.\n1 Libra = 1 Libra.\n",a," Libras equivalen a = ",a," Libras.")
														else:
															if b==3 and c==4:
																print("De Libras a Onzas.\n1 Libra = 16 Onzas.")
																z=a*16
																print(a," Libras equivalen a = ",z," Onzas.")
															else:
																if b==4 and c==1:
																	print("De Onzas a Gramos.\n1 Onza = 28.32 Gramos.")
																	z=a*28.32
																	print(a," Onzas equivalen a = ",z," Gramos.")
																else:
																	if b==4 and c==2:
																		print("De Onzas a Kilogramos.\n1 Onza = 0.0283 Kilogramos.")
																		z=a*0.0283
																		print(a," Onzas equivalen a = ",z," Kilogramos.")
																	else:
																		if b==4 and c==3:
																			print("De Onzas a Libras.\n1 Onza = 0.0625 Libras")
																			z=a*0.0625
																			print(a," Onzas equivalen a = ",z," Libras.")
																		else:
																			if b==4 and c==4:
																				print("De Onzas a Onzas.\n1 Onza = 1 Onza.")
																				print(a," Onzas equivalen a = ",a," Onzas.")
																			else:
																				if c==5:
																					print("¿Estas seguro de salir de Factores de Conversion de Masa?")
																					a=int(input("1. Si.\n2. No.\n"))
																					if a==1:
																						contador1-=1
																					else:
																						if a==2:
																							contador1+=1
																						else:
																							print("Solo puedes escoger entre 1 - 2.")
																				else:
																					print("Solo puedes escoger entre 1 - 5.")
		else:
			if a==3:
				contador2=0
				while contador2>=0:
					print("Factores de Conversion de Tiempo.")
					a=float(input("Introduzca el numero que desea convertir.\n"))
					print("Seleccione la unidad.\n1. Segundo.\n2. Milisegundo.\n3. Minuto.\n4. Hora.")
					b=int(input("Unidad=\n"))
					print("¿A que unidad desea convertir?\n1. Segundo.\n2. Milisegundo.\n3. Minuto.\n4. Hora.\n5. Atras...")
					c=int(input("Unidad=\n"))
					if b==1 and c==1:
						print("De Segundos a Segundos.\n1 Segundo = 1 Segundo.\n",a," Segundos equivalen a = ",a," Segundos.")
					else:
						if b==1 and c==2:
							print("De Segundos a Milisegundos.\n1 Segundo = 1000 Milisegundos.")
							z=a*1000
							print(a," Segundos equivalen a = ",z," Milisegundos.")
						else:
							if b==1 and c==3:
								print("De Segundos a Minutos.\n1 Segundo = 0.01667 Minutos.")
								z=a/60
								print(a," Segundos equivalen a = ",z," Minutos.")
							else:
								if b==1 and c==4:
									print("De Segundos a Horas.\n1 Segundo = 0.0002778 Horas.")
									z=a/3600
									print(a," Segundos equivalen a = ",z," Horas.")
								else:
									if b==2 and c==1:
										print("De Milisegundos a Segundos.\n1 Milisegundo = 0.001 Segundos.")
										z=a/1000
										print(a," Milisegundos equivalen a = ",z," Segundos.")
									else:
										if b==2 and c==2:
											print("De Milisegundos a Milisegundos.\n1 Milisegundo = 1 Milisegundo.\n",a," Milisegundos equivalen a = ",a," Milisegundos.")
										else:
											if b==2 and c==3:
												print("De Milisegundos a Minutos.\n1 Milisegundo = 0.0000167 Minutos.")
												z=a/60000
												print(a," Milisegundos equivalen a = ",z," Minutos")
											else:
												if b==2 and c==4:
													print("De Milisegundos a Horas.\n1 Milisegundo = 0.000000278 Horas.")
													z=a/3600000
													print(a," Milisegundos equivalen a = ",z," Pulgadas.")
												else:
													if b==3 and c==1:
														print("De Minutos a Segundos.\n1 Minuto = 60 Segundos.")
														z=a*60
														print(a," Minutos equivalen a = ",z," Segundos.")
													else:
														if b==3 and c==2:
															print("De Minutos a Milisegundos.\n1 Minuto = 60000 Milisegundos.")
															z=a*60000
															print(a," Minutos equivalen a = ",z," Milisegundos.")
														else:
															if b==3 and c==3:
																print("De Minutos a Minutos.\n1 Minuto = 1 Minuto.\n",a," Minutos equivalen a = ",a," Minutos.")
															else:
																if b==3 and c==4:
																	print("De Minutos a Horas.\n1 Minuto = 0.01667 Horas.")
																	z=a/60
																	print(a," Minutos equivalen a = ",z," Horas.")
																else:
																	if b==4 and c==1:
																		print("De Horas a Segundos.\n1 Hora = 3600 Segundos.")
																		z=a*3600
																		print(a," Horas equivalen a = ",z," Segundos.")
																	else:
																		if b==4 and c==2:
																			print("De Horas a Milisegundos.\n1 Hora = 3600000 Milisegundos.")
																			z=a*3600000
																			print(a," Horas equivalen a = ",z," Milisegundos.")
																		else:
																			if b==4 and c==3:
																				print("De Horas a Minutos.\n1 Hora = 60 Minutos")
																				z=a*60
																				print(a," Horas equivalen a = ",z," Minutos.")
																			else:
																				if b==4 and c==4:
																					print("De Horas a Horas.\n1 Hora = 1 Hora.")
																					print(a," Horas equivalen a = ",a," Horas.")
																				else:
																					if b==5 or c==5:
																						print("¿Estas seguro de salir de Factores de Conversion de Tiempo?")
																						a=int(input("1. Si.\n2. No.\n"))
																						if a==1:
																							contador2-=1
																						else:
																							if a==2:
																								contador2+=1
																							else:
																								print("Solo puedes escoger entre 1 - 2.")
																					else:
																						print("Solo puedes escoger entre 1 - 5.")
			else:
				if a==4:
					contador3=0
					while contador3>=0:
						print("Factores de Conversion de Area.")
						a=float(input("Introduzca el numero que desea convertir.\n"))
						print("Seleccione la unidad.\n1. Metro Cuadrado.\n2. Centimetro Cuadrado.\n3. Pie Cuadrado.\n4. Pulgada Cuadrada.")
						b=int(input("Unidad=\n"))
						print("¿A que unidad desea convertir?\n1. Metro Cuadrado.\n2. Centimetro Cuadrado.\n3. Pie Cuadrado.\n4. Pulgada Cuadrada.\n5. Atras...")
						c=int(input("Unidad=\n"))
						if b==1 and c==1:
							print("De Metros Cuadrados a Metros Cuadrados.\n1 Metro Cuadrado = 1 Metro Cuadrado.\n",a," Metros Cuadrados equivalen a = ",a," Metros Cuadrados.")
						else:
							if b==1 and c==2:
								print("De Metros Cuadrados a Centimetros Cuadrados.\n1 Metro Cuadrado = 10000 Centimetros Cuadrados.")
								z=a*10000
								print(a," Metros Cuadrados equivalen a = ",z," Centimetros Cuadrados.")
							else:
								if b==1 and c==3:
									print("De Metros Cuadrados a Pies Cuadrados.\n1 Metro Cuadrado = 10.76 Pies Cuadrados.")
									z=a*10.76
									print(a," Metros Cuadrados equivalen a = ",z," Pies Cuadrados.")
								else:
									if b==1 and c==4:
										print("De Metros Cuadrados a Pulgadas Cuadradas.\n1 Metro Cuadrado = 1550 Pulgadas Cuadradas.")
										z=a*1550
										print(a," Metros Cuadrados equivalen a = ",z," Pulgadas Cuadradas.")
									else:
										if b==2 and c==1:
											print("De Centimetros Cuadrados a Metros Cuadrados.\n1 Centimetro Cuadrado = 0.0001 Metros Cuadrados.")
											z=a*0.0001
											print(a," Centimetros Cuadrados equivalen a = ",z," Metros Cuadrados.")
										else:
											if b==2 and c==2:
												print("De Centimetros Cuadrados a Centimetros Cuadrados.\n1 Centimetro Cuadrado = 1 Centimetro Cuadrado.\n",a," Centimetros Cuadrados equivalen a = ",a," Centimetros Cuadrados.")
											else:
												if b==2 and c==3:
													print("De Centimetros Cuadrados a Pies Cuadrados.\n1 Centimetro Cuadrado = 0.001076 Pies Cuadrados.")
													z=a*0.001076
													print(a," Centimetros Cuadrados equivalen a = ",z," Pies Cuadrados")
												else:
													if b==2 and c==4:
														print("De Centimetros Cuadrados a Pulgadas Cuadradas.\n1 Centimetro Cuadrado = 0.115 Pulgadas Cuadradas.")
														z=a*0.115
														print(a," Centimetros Cuadrados equivalen a = ",z," Pulgadas Cuadradas.")
													else:
														if b==3 and c==1:
															print("De Pies Cuadrados a Metros Cuadrados.\n1 Pie Cuadrado = 0.0929 Metros Cuadrados.")
															z=a*0.0929
															print(a," Pies Cuadrados equivalen a = ",z," Metros Cuadrados.")
														else:
															if b==3 and c==2:
																print("De Pies Cuadrados a Centimetros Cuadrados.\n1 Pie Cuadrado = 929 Centimetros Cuadrados.")
																z=a*929
																print(a," Pies Cuadrados equivalen a = ",z," Centimetros Cuadrados.")
															else:
																if b==3 and c==3:
																	print("De Pies Cuadrados a Pies Cuadrados.\n1 Pie Cuadrado = 1 Pie Cuadrado.\n",a," Pies Cuadrados equivalen a = ",a," Pies Cuadrados.")
																else:
																	if b==3 and c==4:
																		print("De Pies Cuadrados a Pulgadas Cuadradas.\n1 Pie Cuadrado = 144 Pulgadas Cuadradas.")
																		z=a*144
																		print(a," Pies Cuadrados equivalen a = ",z," Pulgadas Cuadradas.")
																	else:
																		if b==4 and c==1:
																			print("De Pulgadas Cuadradas a Metros Cuadrados.\n1 Pulgada Cuadrada = 0.0006452 Metros Cuadrados.")
																			z=a*0.0006452
																			print(a," Pulgadas Cuadradas equivalen a = ",z," Metros Cuadrados.")
																		else:
																			if b==4 and c==2:
																				print("De Pulgadas Cuadradas a Centimetros Cuadrados.\n1 Pulgada Cuadrada = 6.252 Centimetros Cuadrados.")
																				z=a*6.452
																				print(a," Pulgadas Cuadradas equivalen a = ",z," Centimetros Cuadrados.")
																			else:
																				if b==4 and c==3:
																					print("De Pulgadas Cuadradas a Pies Cuadrados.\n1 Pulgada Cuadrada = 0.006994 Pies Cuadrados")
																					z=a*0.006994
																					print(a," Pulgadas Cuadradas equivalen a = ",z," Pies Cuadrados.")
																				else:
																					if b==4 and c==4:
																						print("De Pulgadas Cuadradas a Pulgadas Cuadradas.\n1 Pulgada Cuadrada = 1 Pulgada Cuadrada.")
																						print(a," Pulgadas Cuadradas equivalen a = ",a," Pulgadas Cuadradas.")
																					else:
																						if b==5 or c==5:
																							print("¿Estas seguro de salir de Factores de Conversion de Area?")
																							a=int(input("1. Si.\n2. No.\n"))
																							if a==1:
																								contador3-=1
																							else:
																								if a==2:
																									contador3+=1
																								else:
																									print("Solo puedes escoger entre 1 - 2.")
																						else:
																							print("Solo puedes escoger entre 1 - 5.")
				else:
					if a==5:
						contador4=0
						while contador4>=0:
							print("Factores de Conversion de Volumen.")
							a=float(input("Introduzca el numero que desea convertir.\n"))
							print("Seleccione la unidad.\n1. Metro Cubico.\n2. Centimetro Cubico.\n3. Pie Cubico.\n4. Pulgada Cubica.")
							b=int(input("Unidad=\n"))
							print("¿A que unidad desea convertir?\n1. Metro Cubico.\n2. Centimetro Cubico.\n3. Pie Cubico.\n4. Pulgada Cubica.\n5. Atras...")
							c=int(input("Unidad=\n"))
							if b==1 and c==1:
								print("De Metros Cubicos a Metros Cubicos.\n1 Metro Cubico = 1 Metro Cubico.\n",a," Metros Cubicos equivalen a = ",a," Metros Cubicos.")
							else:
								if b==1 and c==2:
									print("De Metros Cubicos a Centimetros Cubicos.\n1 Metro Cubico = 1000000 Centimetros Cubicos.")
									z=a*1000000
									print(a," Metros Cubicos equivalen a = ",z," Centimetros Cubicos.")
								else:
									if b==1 and c==3:
										print("De Metros Cubicos a Pies Cubicos.\n1 Metro Cubico = 35.315 Pies Cubicos.")
										z=a*35.315
										print(a," Metros Cubicos equivalen a = ",z," Pies Cubicos.")
									else:
										if b==1 and c==4:
											print("De Metros Cubicos a Pulgadas Cubicas.\n1 Metro Cubico = 61023.74 Pulgadas Cubicas.")
											z=a*61023.74
											print(a," Metros Cubicos equivalen a = ",z," Pulgadas Cubicas.")
										else:
											if b==2 and c==1:
												print("De Centimetros Cubicos a Metros Cubicos.\n1 Centimetro Cubico = 0.000001 Metros Cubicos.")
												z=a*0.000001
												print(a," Centimetros Cubicos equivalen a = ",z," Metros Cubicos.")
											else:
												if b==2 and c==2:
													print("De Centimetros Cubicos a Centimetros Cubicos.\n1 Centimetro Cubico = 1 Centimetro Cubico.\n",a," Centimetros Cubicos equivalen a = ",a," Centimetros Cubicos.")
												else:
													if b==2 and c==3:
														print("De Centimetros Cubicos a Pies Cubicos.\n1 Centimetro Cubico = 0.00003351 Pies Cubicos.")
														z=a*0.00003351
														print(a," Centimetros Cubicos equivalen a = ",z," Pies Cubicos.")
													else:
														if b==2 and c==4:
															print("De Centimetros Cubicos a Pulgadas Cubicas.\n1 Centimetro Cubico = 0.06102 Pulgadas Cubicas.")
															z=a*0.06102
															print(a," Centimetros Cubicos equivalen a = ",z," Pulgadas Cubicas.")
														else:
															if b==3 and c==1:
																print("De Pies Cubicos a Metros Cubicos.\n1 Pie Cubico = 0.02832 Metros Cubicos.")
																z=a*0.02832
																print(a," Pies Cubicos equivalen a = ",z," Metros Cubicos.")
															else:
																if b==3 and c==2:
																	print("De Pies Cubicos a Centimetros Cubicos.\n1 Pie Cubico = 0.0002832 Centimetros Cubicos.")
																	z=a*0.0002832
																	print(a," Pies Cubicos equivalen a = ",z," Centimetros Cubicos.")
																else:
																	if b==3 and c==3:
																		print("De Pies Cubicos a Pies Cubicos.\n1 Pie Cubico = 1 Pie Cubico.\n",a," Pies Cubicos equivalen a = ",a," Pies Cubicos.")
																	else:
																		if b==3 and c==4:
																			print("De Pies Cubicos a Pulgadas Cubicas.\n1 Pie Cubico = 1728 Pulgadas Cubicas.")
																			z=a*1728
																			print(a," Pies Cubicos equivalen a = ",z," Pulgadas Cubicas.")
																		else:
																			if b==4 and c==1:
																				print("De Pulgadas Cubicas a Metros Cubicos.\n1 Pulgada Cubica = 0.00001639 Metros Cubicos.")
																				z=a*0.00001639
																				print(a," Pulgadas Cubicas equivalen a = ",z," Metros Cubicos.")
																			else:
																				if b==4 and c==2:
																					print("De Pulgadas Cubicas a Centimetros Cubicos.\n1 Pulgada Cubica = 16.387 Centimetros Cubicos.")
																					z=a*16.387
																					print(a," Pulgadas Cubicas equivalen a = ",z," Centimetros Cubicos.")
																				else:
																					if b==4 and c==3:
																						print("De Pulgadas Cubicas a Pies Cubicos.\n1 Pulgada Cubica = 0.0005787 Pies Cubicos")
																						z=a*0.0005787
																						print(a," Pulgadas Cubicas equivalen a = ",z," Pies Cubicos.")
																					else:
																						if b==4 and c==4:
																							print("De Pulgadas Cubicas a Pulgadas Cubicas.\n1 Pulgada Cubica = 1 Pulgada Cubica.")
																							print(a," Pulgadas Cubicas equivalen a = ",a," Pulgadas Cubicas.")
																						else:
																							if b==5 or c==5:
																								print("¿Estas seguro de salir de Factores de Conversion de Volumen?")
																								a=int(input("1. Si.\n2. No.\n"))
																								if a==1:
																									contador4-=1
																								else:
																									if a==2:
																										contador4+=1
																									else:
																										print("Solo puedes escoger entre 1 - 2.")
																							else:
																								print("Solo puedes escoger entre 1 - 5.")
					else:
						if a==6:
							contador5=0
							while contador5>=0:
								print("Factores de Conversion de Fuerza.")
								a=float(input("Introduzca el numero que desea convertir.\n"))
								print("Seleccione la unidad.\n1. Newton.\n2. Dina.\n3. Libra.\n4. Kilogramo-Fuerza.")
								b=int(input("Unidad=\n"))
								print("¿A que unidad desea convertir?\n1. Newton.\n2. Dina.\n3. Libra.\n4. Kilogramo-Fuerza.\n5. Atras...")
								c=int(input("Unidad=\n"))
								if b==1 and c==1:
									print("De Newtons a Newtons.\n1 Newton = 1 Newton.\n",a," Newtons equivalen a = ",a," Newtons.")
								else:
									if b==1 and c==2:
										print("De Newtons a Dinas.\n1 Newton = 100000 Dinas.")
										z=a*100000
										print(a," Newtons equivalen a = ",z," Dinas.")
									else:
										if b==1 and c==3:
											print("De Newtons a Libras.\n1 Newton = 0.2248 Libras.")
											z=a*0.2248
											print(a," Newtons equivalen a = ",z," Libras.")
										else:
											if b==1 and c==4:
												print("De Newtons a Kilogramos-fuerza.\n1 Newton = 0.1020 Kilogramos-fuerza.")
												z=a*0.1020
												print(a," Newtons equivalen a = ",z," Kilogramos-fuerza.")
											else:
												if b==2 and c==1:
													print("De Dinas a Newtons.\n1 Dina = 0.00001 Newtons.")
													z=a*0.00001
													print(a," Dinas equivalen a = ",z," Newtons.")
												else:
													if b==2 and c==2:
														print("De Dinas a Dinas.\n1 Dina = 1 Dina.\n",a," Dinas equivalen a = ",a," Dinas.")
													else:
														if b==2 and c==3:
															print("De Dinas a Libras.\n1 Dina = 0.000002248 Libras.")
															z=a*0.000002248
															print(a," Dinas equivalen a = ",z," Libras")
														else:
															if b==2 and c==4:
																print("De Dinas a Kilogramos-fuerza.\n1 Dina = 0.00000102 Kilogramos-fuerza.")
																z=a*0.00000102
																print(a," Dinas equivalen a = ",z," Kilogramos-fuerza.")
															else:
																if b==3 and c==1:
																	print("De Libras a Newtons.\n1 Libra = 4.448 Newtons.")
																	z=a*4.448
																	print(a," Libras equivalen a = ",z," Newtons.")
																else:
																	if b==3 and c==2:
																		print("De Libras a Dinas.\n1 Libra = 444800 Dinas.")
																		z=a*444800
																		print(a," Libras equivalen a = ",z," Dinas.")
																	else:
																		if b==3 and c==3:
																			print("De Libras a Libras.\n1 Libra = 1 Libra.\n",a," Libras equivalen a = ",a," Libras.")
																		else:
																			if b==3 and c==4:
																				print("De Libras a Kilogramos-fuerza.\n1 Libra = 0.4536 Kilogramos-fuerza.")
																				z=a*0.4536
																				print(a," Libras equivalen a = ",z," Kilogramos-fuerza.")
																			else:
																				if b==4 and c==1:
																					print("De Kilogramos-fuerza a Newtons.\n1 Kilogramo-fuerza = 9.807 Newtons.")
																					z=a*9.807
																					print(a," Kilogramos-fuerza equivalen a = ",z," Newtons.")
																				else:
																					if b==4 and c==2:
																						print("De Kilogramos-fuerza a Dinas.\n1 Kilogramo-fuerza = 980700 Dinas.")
																						z=a*980700
																						print(a," Kilogramos-fuerza equivalen a = ",z," Dinas.")
																					else:
																						if b==4 and c==3:
																							print("De Kilogramos-fuerza a Libras.\n1 Kilogramo-fuerza = 2.205 Libras")
																							z=a*2.205
																							print(a," Kilogramos-fuerza equivalen a = ",z," Libras.")
																						else:
																							if b==4 and c==4:
																								print("De Kilogramos-fuerza a Kilogramos-fuerza.\n1 Kilogramo-fuerza = 1 Kilogramo-fuerza.")
																								print(a," Kilogramos-fuerza equivalen a = ",a," Kilogramos-fuerza.")
																							else:
																								if b==5 or c==5:
																									print("¿Estas seguro de salir de Factores de Conversion de Fuerza?")
																									a=int(input("1. Si.\n2. No.\n"))
																									if a==1:
																										contador5-=1
																									else:
																										if a==2:
																											contador5+=1
																										else:
																											print("Solo puedes escoger entre 1 - 2.")
																								else:
																									print("Solo puedes escoger entre 1 - 5.")
						else:
							if a==7:
								contador6=0
								while contador6>=0:
									print("Factores de Conversion de Energia.")
									a=float(input("Introduzca el numero que desea convertir.\n"))
									print("Seleccione la unidad.\n1. Joule.\n2. BTU.\n3. KCal.\n4. KW-h.")
									b=int(input("Unidad=\n"))
									print("¿A que unidad desea convertir?\n1. Joule.\n2. BTU.\n3. KCal.\n4. KW-h.\n5. Atras...")
									c=int(input("Unidad=\n"))
									if b==1 and c==1:
										print("De Joules a Joules.\n1 Joule = 1 Joule.\n",a," Joules equivalen a = ",a," Joules.")
									else:
										if b==1 and c==2:
											print("De Joules a BTU.\n1 Joule = 0.000947 BTU.")
											z=a*0.000947
											print(a," Joules equivalen a = ",z," BTU.")
										else:
											if b==1 and c==3:
												print("De Joules a KCal.\n1 Joule = 0.0002389 KCal.")
												z=a*0.0002389
												print(a," Joules equivalen a = ",z," KCal.")
											else:
												if b==1 and c==4:
													print("De Joules a KW-h.\n1 Joule = 0.0000000277 KW-h.")
													z=a*0.0000000277
													print(a," Joules equivalen a = ",z," KW-h.")
												else:
													if b==2 and c==1:
														print("De BTU a Joules.\n1 BTU = 1054.98 Joules.")
														z=a*1054.98
														print(a," BTU equivalen a = ",z," Joules.")
													else:
														if b==2 and c==2:
															print("De BTU a BTU.\n1 BTU = 1 BTU.\n",a," BTU equivalen a = ",a," BTU.")
														else:
															if b==2 and c==3:
																print("De BTU a KCal.\n1 BTU = 0.25201 KCal.")
																z=a*0.25201
																print(a," BTU equivalen a = ",z," KCal")
															else:
																if b==2 and c==4:
																	print("De BTU a KW-h.\n1 BTU = 0.00029 KW-h.")
																	z=a*0.00029
																	print(a," BTU equivalen a = ",z," KW-h.")
																else:
																	if b==3 and c==1:
																		print("De KCal a Joules.\n1 KCal = 4186.17 Joules.")
																		z=a*4186.17
																		print(a," KCal equivalen a = ",z," Joules.")
																	else:
																		if b==3 and c==2:
																			print("De KCal a BTU.\n1 KCal = 3.968 BTU.")
																			z=a*3.968
																			print(a," KCal equivalen a = ",z," BTU.")
																		else:
																			if b==3 and c==3:
																				print("De KCal a KCal.\n1 KCal = 1 KCal.\n",a," KCal equivalen a = ",a," KCal.")
																			else:
																				if b==3 and c==4:
																					print("De KCal a KW-h.\n1 KCal = 0.001161 KW-h.")
																					z=a*0.001161
																					print(a," KCal equivalen a = ",z," KW-h.")
																				else:
																					if b==4 and c==1:
																						print("De KW-h a Joules.\n1 KW-h = 3600000 Joules.")
																						z=a*3600000
																						print(a," KW-h equivalen a = ",z," Joules.")
																					else:
																						if b==4 and c==2:
																							print("De KW-h a BTU.\n1 KW-h = 3417.74 BTU.")
																							z=a*3417.74
																							print(a," KW-h equivalen a = ",z," BTU.")
																						else:
																							if b==4 and c==3:
																								print("De KW-h a KCal.\n1 KW-h = 861.326 KCal")
																								z=a*0.083333333
																								print(a," KW-h equivalen a = ",z," KCal.")
																							else:
																								if b==4 and c==4:
																									print("De KW-h a KW-h.\n1 KW-h = 1 KW-h.")
																									print(a," KW-h equivalen a = ",a," KW-h.")
																								else:
																									if b==5 or c==5:
																										print("¿Estas seguro de salir de Factores de Conversion de Energia?")
																										a=int(input("1. Si.\n2. No.\n"))
																										if a==1:
																											contador6-=1
																										else:
																											if a==2:
																												contador6+=1
																											else:
																												print("Solo puedes escoger entre 1 - 2.")
																									else:
																										print("Solo puedes escoger entre 1 - 5.")
							else:
								if a==8:
									contador=7
									while contador7>=0:
										print("Factores de Conversion de Potencia.")
										a=float(input("Introduzca el numero que desea convertir.\n"))
										print("Seleccione la unidad.\n1. Watt.\n2. Kilowatt.\n3. Hp.\n4. BTU/hr.")
										b=int(input("Unidad=\n"))
										print("¿A que unidad desea convertir?\n1. Watt.\n2. KiloWatt.\n3. Hp.\n4. BTU/hr.\n5. Atras...")
										c=int(input("Unidad=\n"))
										if b==1 and c==1:
											print("De Watts a Watts.\n1 Watt = 1 Watt.\n",a," Watts equivalen a = ",a," Watts.")
										else:
											if b==1 and c==2:
												print("De Watts a KiloWatts.\n1 Watt = 0.001 KiloWatts.")
												z=a*0.001
												print(a," Watts equivalen a = ",z," KiloWatts.")
											else:
												if b==1 and c==3:
													print("De Watts a Hp.\n1 Watt = 0.001341 Hp.")
													z=a*0.001341
													print(a," Watts equivalen a = ",z," Hp.")
												else:
													if b==1 and c==4:
														print("De Watts a BTU/hr.\n1 Watt = 3.4121 BTU/hr.")
														z=a*3.4121
														print(a," Watts equivalen a = ",z," BTU/hr.")
													else:
														if b==2 and c==1:
															print("De KiloWatts a Watts.\n1 KiloWatt = 1000 Watts.")
															z=a*1000
															print(a," KiloWatts equivalen a = ",z," Watts.")
														else:
															if b==2 and c==2:
																print("De KiloWatts a KiloWatts.\n1 KiloWatt = 1 KiloWatt.\n",a," KiloWatts equivalen a = ",a," KiloWatts.")
															else:
																if b==2 and c==3:
																	print("De KiloWatts a Hp.\n1 KiloWatt = 1.341 Hp.")
																	z=a*1.341
																	print(a," KiloWatts equivalen a = ",z," Hp")
																else:
																	if b==2 and c==4:
																		print("De KiloWatts a BTU/hr.\n1 KiloWatt = 3412.1 BTU/hr.")
																		z=a*3412.1
																		print(a," KiloWatts equivalen a = ",z," BTU/hr.")
																	else:
																		if b==3 and c==1:
																			print("De Hp a Watts.\n1 Hp = 745.7 Watts.")
																			z=a*745.7
																			print(a," Hp equivalen a = ",z," Watts.")
																		else:
																			if b==3 and c==2:
																				print("De Hp a KiloWatts.\n1 Hp = 0.7457 KiloWatts.")
																				z=a*0.7457
																				print(a," Hp equivalen a = ",z," KiloWatts.")
																			else:
																				if b==3 and c==3:
																					print("De Hp a Hp.\n1 Hp = 1 Hp.\n",a," Hp equivalen a = ",a," Hp.")
																				else:
																					if b==3 and c==4:
																						print("De Hp a BTU/hr.\n1 Hp = 2544.4 BTU/hr.")
																						z=a*2544.4
																						print(a," Hp equivalen a = ",z," BTU/hr.")
																					else:
																						if b==4 and c==1:
																							print("De BTU/hr a Watts.\n1 BTU/hr = 0.29307 Watts.")
																							z=a*0.029307
																							print(a," BTU/hr equivalen a = ",z," Watts.")
																						else:
																							if b==4 and c==2:
																								print("De BTU/hr a KiloWatts.\n1 BTU/hr = 0.00029307 KiloWatts.")
																								z=a*0.00029307
																								print(a," BTU/hr equivalen a = ",z," KiloWatts.")
																							else:
																								if b==4 and c==3:
																									print("De BTU/hr a Hp.\n1 BTU/hr = 3.9301 Hp")
																									z=a*3.9301
																									print(a," BTU/hr equivalen a = ",z," Hp.")
																								else:
																									if b==4 and c==4:
																										print("De BTU/hr a BTU/hr.\n1 BTU/hr = 1 BTU/hr.")
																										print(a," BTU/hr equivalen a = ",a," BTU/hr.")
																									else:
																										if b==5 or c==5:
																											print("¿Estas seguro de salir de Factores de Conversion de Potencia?")
																											a=int(input("1. Si.\n2. No.\n"))
																											if a==1:
																												contador7-=1
																											else:
																												if a==2:
																													contador7+=1
																												else:
																													print("Solo puedes escoger entre 1 - 2.")
																										else:
																											print("Solo puedes escoger entre 1 - 5.")
								else:
									if a==9:
										contador8=0
										while contador8>=0:
											print("Factores de Conversion de Presion.")
											a=float(input("Introduzca el numero que desea convertir.\n"))
											print("Seleccione la unidad.\n1. Pascal.\n2. Atm.\n3. Bar\n4. Torr.")
											b=int(input("Unidad=\n"))
											print("¿A que unidad desea convertir?\n1. Pascal.\n2. Atm.\n3. Bar.\n4. Torr.\n5. Atras...")
											c=int(input("Unidad=\n"))
											if b==1 and c==1:
												print("De Pascales a Pascales.\n1 Pascal = 1 Pascal.\n",a," Pascales equivalen a = ",a," Pascales.")
											else:
												if b==1 and c==2:
													print("De Pascales a Atm.\n1 Pascal = 0.00000987 Atm.")
													z=a*0.00000987
													print(a," Pascales equivalen a = ",z," Atm.")
												else:
													if b==1 and c==3:
														print("De Pascales a Bar.\n1 Pascal = 3.281 Bar.")
														z=a*0.00001
														print(a," Pascales equivalen a = ",z," Bar.")
													else:
														if b==1 and c==4:
															print("De Pascales a Torr.\n1 Pascal = 0.0075 Torr.")
															z=a*0.0075
															print(a," Pascales equivalen a = ",z," Torr.")
														else:
															if b==2 and c==1:
																print("De Atm a Pascales.\n1 Atm = 101325 Pascales.")
																z=a*101325
																print(a," Atm equivalen a = ",z," Pascales.")
															else:
																if b==2 and c==2:
																	print("De Atm a Atm.\n1 Atm = 1 Atm.\n",a," Atm equivalen a = ",a," Atm.")
																else:
																	if b==2 and c==3:
																		print("De Atm a Bar.\n1 Atm = 1.01325 Bar.")
																		z=a*1.01325
																		print(a," Atm equivalen a = ",z," Bar")
																	else:
																		if b==2 and c==4:
																			print("De Atm a Torr.\n1 Atm = 760 Torr.")
																			z=a*760
																			print(a," Atm equivalen a = ",z," Torr.")
																		else:
																			if b==3 and c==1:
																				print("De Bar a Pascales.\n1 Bar = 100000 Pascales.")
																				z=a*100000
																				print(a," Bar equivalen a = ",z," Pascales.")
																			else:
																				if b==3 and c==2:
																					print("De Bar a Atm.\n1 Bar = 0.987 Atm.")
																					z=a*0.987
																					print(a," Bar equivalen a = ",z," Atm.")
																				else:
																					if b==3 and c==3:
																						print("De Bar a Bar.\n1 Bar = 1 Bar.\n",a," Bar equivalen a = ",a," Bar.")
																					else:
																						if b==3 and c==4:
																							print("De Bar a Torr.\n1 Bar = 750 Torr.")
																							z=a*750
																							print(a," Bar equivalen a = ",z," Torr.")
																						else:
																							if b==4 and c==1:
																								print("De Torr a Pascales.\n1 Torr = 101325 Pascales.")
																								z=a*101325
																								print(a," Torr equivalen a = ",z," Pascales.")
																							else:
																								if b==4 and c==2:
																									print("De Torr a Atm.\n1 Torr = 0.00132 Atm.")
																									z=a*0.00132
																									print(a," Torr equivalen a = ",z," Atm.")
																								else:
																									if b==4 and c==3:
																										print("De Torr a Bar.\n1 Torr = 0.0013332 Bar")
																										z=a*.0013332
																										print(a," Torr equivalen a = ",z," Bar.")
																									else:
																										if b==4 and c==4:
																											print("De Torr a Torr.\n1 Torr = 1 Torr.")
																											print(a," Torr equivalen a = ",a," Torr.")
																										else:
																											if b==5 or c==5:
																												print("¿Estas seguro de salir de Factores de Conversion de Presion?")
																												a=int(input("1. Si.\n2. No.\n"))
																												if a==1:
																													contador8-=1
																												else:
																													if a==2:
																														contador8+=1
																													else:
																														print("Solo puedes escoger entre 1 - 2.")
																											else:
																												print("Solo puedes escoger entre 1 - 5.")
									else:
										if a==10:
											contador9=0
											while contador9>=0:
												print("Factores de Conversion de Temperatura.")
												a=float(input("Introduzca el numero que desea convertir.\n"))
												print("Seleccione la unidad.\n1. Celsius.\n2. Farenheit.\n3. Kelvin.\n4. Ranking.")
												b=int(input("Unidad=\n"))
												print("¿A que unidad desea convertir?\n1. Celsius.\n2. Fahrenheit.\n3. Kelvin.\n4. Ranking.\n5. Atras...")
												c=int(input("Unidad=\n"))
												if b==1 and c==1:
													print("De Celsius a Celsius.\n",a,"° Celsius equivalen a = ",a,"° Celsius.")
												else:
													if b==1 and c==2:
														print("De Celsius a Fahrenheit.")
														z=a*1.8+32
														print(a,"° Celsius equivalen a = ",z,"° Fahrenheit.")
													else:
														if b==1 and c==3:
															print("De Celsius a Kelvin.")
															z=a+273
															print(a,"° Celsius equivalen a = ",z,"° Kelvin.")
														else:
															if b==1 and c==4:
																print("De Celsius a Ranking.")
																z=(a*1.8+32)+459.67
																print(a,"° Celsius equivalen a = ",z,"° Ranking.")
															else:
																if b==2 and c==1:
																	print("De Fahrenheit a Celsius.")
																	z=(a-32)/1.8
																	print(a,"° Fahrenheit equivalen a = ",z,"° Celsius.")
																else:
																	if b==2 and c==2:
																		print("De Fahrenheit a Fahrenheit.\n",a,"° Fahrenheit equivalen a = ",a,"° Fahrenheit.")
																	else:
																		if b==2 and c==3:
																			print("De Fahrenheit a Kelvin.")
																			z=(a+459.67)/1.8
																			print(a,"° Fahrenheit equivalen a = ",z,"° Kelvin")
																		else:
																			if b==2 and c==4:
																				print("De Fahrenheit a Ranking.")
																				z=a+459.67
																				print(a,"° Fahrenheit equivalen a = ",z,"° Ranking.")
																			else:
																				if b==3 and c==1:
																					print("De Kelvin a Celsius.\n")
																					z=a-273
																					print(a,"° Kelvin equivalen a = ",z,"° Celsius.")
																				else:
																					if b==3 and c==2:
																						print("De Kelvin a Fahrenheit.")
																						z=a*1.8-459.67
																						print(a,"° Kelvin equivalen a = ",z,"° Fahrenheit.")
																					else:
																						if b==3 and c==3:
																							print("De Kelvin a Kelvin.\n",a," Kelvin equivalen a = ",a," Kelvin.")
																						else:
																							if b==3 and c==4:
																								print("De Kelvin a Ranking.")
																								z=(a*1.8)
																								print(a,"° Kelvin equivalen a = ",z,"° Ranking.")
																							else:
																								if b==4 and c==1:
																									print("De Ranking a Celsius.")
																									z=((a-459.67)-32)/1.8
																									print(a,"° Ranking equivalen a = ",z,"° Celsius.")
																								else:
																									if b==4 and c==2:
																										print("De Ranking a Fahrenheit.")
																										z=a-459.67
																										print(a,"° Ranking equivalen a = ",z,"° Fahrenheit.")
																									else:
																										if b==4 and c==3:
																											print("De Ranking a Kelvin.")
																											z=a/1.8
																											print(a,"° Ranking equivalen a = ",z,"° Kelvin.")
																										else:
																											if b==4 and c==4:
																												print("De Ranking a Ranking.")
																												print(a,"° Ranking equivalen a = ",a,"° Ranking.")
																											else:
																												if b==5 or c==5:
																													print("¿Estas seguro de salir de Factores de Conversion de Temperatura?")
																													a=int(input("1. Si.\n2. No.\n"))
																													if a==1:
																														contador9-=1
																													else:
																														if a==2:
																															contador9+=1
																														else:
																															print("Solo puedes escoger entre 1 - 2.")
																												else:
																													print("Solo puedes escoger entre 1 - 5.")
										else:
											if a==11:
												contador10=0
												while contador10>=0:
													print("Sistemas de Numeros.\n1. De Decimal a Binario.\n2. De Decimal a Octal\n3. De Binario a Decimal.\n4. De Octal a Decimal.\n5. De Decimal a n base m.\n6. Atras...")
													a=int(input("Numero= "))
													if a==1:
														print("De Decimal a Binario.")
														def binario(decimal):
															binario=""
															while decimal// 2 !=0:
																binario=str(decimal%2)+binario
																decimal=decimal//2
															return str(decimal)+binario
														num= int(input("Numero Decimal= "))
														print(binario(num))
													else:
														if a==2:
															print("De Decimal a Octal.")
															def octal(decimal):
																octal=""
																while decimal// 8 !=0:
																	octal=str(decimal%8)+octal
																	decimal=decimal//8
																return str(decimal)+octal
															num1= int(input("Numero Decimal= "))
															print(octal(num1))

														else:
															if a==3:
																print("De Binario a Decimal.")
																def conversor(a):
																	conv=0
																	for i in range(100):
																		conv+=(int(a)%10*(2**i))
																		a/=10
																	return conv
																z=int(input("Numero Binario= \n"))
																print(conversor(z))
															else:
																if a==4:
																	print("De Octal a Decimal.")
																	def conversor1(a):
																		con=0
																		for i in range(100):
																			conv+=(int(a)%10*(8**i))
																			a/=10
																		return con
																	y=int(input("Numero Octal= \n"))
																	print(conversor1(y))
																else:
																	if a==5:
																		print("De Decimal a n base m.")
																		def Cambiobase(decimal, base):
																			conversion=""
																			while decimal//base !=0:
																				conversion =str(decimal%base)+conversion
																				decimal=decimal//base
																			return str(decimal)+conversion
																		numero=int(input("Numero= \n"))
																		base=int(input("Introduce la base= "))
																		print(Cambiobase(numero, base))
																	else:
																		if a==6:
																			print("¿Seguro que deseas salir de sistemas de numeros?")
																			a=int(input("1. Si.\n2. No.\n"))
																			if a==1:
																				contador10-=1
																			else:
																				if a==2:
																					contador10+=1
																				else:
																					print("Solo puedes escoger entre 1 - 2.")
																		else:
																			print("Solo puedes escoger entre 1 - 6.")




											else:
												if a==12:
													print("¿Seguro que deseas salir del Sistema de Factores de Conversion?")
													a=int(input("1. Si.\n2. No.\n"))
													if a==1:
														print("Hasta Luego :D")
														var-=1
													else:
														if a==2:
															var+=1
														else:
															print("Solo puedes escoger entre 1 - 2.")
												else:
													print("Solo puedes escoger entre 1 - 11.")
												
												
												






