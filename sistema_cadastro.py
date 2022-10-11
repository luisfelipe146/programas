#charset utf-8
import os

#print("\033[32;1m Bright Green")


id_=[0,1,2,3,4]
nome=["Luis","Felipe","Lima","Da","Silva"]
cpf=[123456780,123456781,123456782,123456783,123456784]
email=["luisfelipe146@hotmail.com","luisfelipe146@hotmail.com","luisfelipe146@hotmail.com","luisfelipe146@hotmail.com","luisfelipe146@hotmail.com"]
senha=[0,1,2,3,4]

id_b=[0,1,2,3,4]
n_bebida=["Coca","Cola","Fanta","Uva","Laranja"]
vlr_bebida=[5.50,5.60,5.30,4.10,3.21]

id_c=[0,1,2,3,4]
n_comida=["Frango","Limão","Pizza","Bolo","Lasanha"]
vlr_comida=[2,2.50,3.10,10.20,10]

while (1):
	print("--------------------------------------------")
	print("\t/\033[34;1mMenu Principal\033[37;40;0m/\n")
	print("\t1-Venda\n\t2-Funções\n\t3-Sair\n\t4-Limpar tela\n\t5-Comprar")
	print("--------------------------------------------")
	resp_0=int(input("Opção:"))
	if resp_0 == 1:
		os.system('clear')
		print("--------------------------------------------")
		print("\t/\033[34;1mMenu Principal\033[37;1m/\033[32;1mVenda\033[37;40;0m/\n")
		print("\t1-Bebidas\n\t2-Cardápio\n\t3-Voltar p/ o menu")
		print("--------------------------------------------")
		resp_1=int(input("Opção:"))
		if resp_1 == 1:
			while (1):
				print("--------------------------------------------")
				print("\t/\033[34;1mMenu Principal\033[37;1m/\033[32;1mVenda\033[37;1m/\033[36;1mBebida\033[37;40;0m/\n")
				print("\t1-Cadastrar\n\t2-Listar\n\t3-Excluir\n\t4-Voltar p/ menu\n\t5-Limpar tela")
				print("--------------------------------------------")
				resp_2=int(input("Opção:"))
				if resp_2 == 1:
					qntd_cadastro_b=int(input("Digite a quantidade de cadastros que ira fazer:"))
					for i in range(qntd_cadastro_b):
						id_b.append(i)
						n_bebida.append(input("Digite o nome da bebida:"))
						vlr_bebida.append(float(input("Digite o valor da bebida:")))
				elif resp_2 == 2:
					a=0
					print("--------------------------------------------")
					print("\t/\033[34;1mMenu Principal\033[37;1m/\033[32;1mVenda\033[37;1m/\033[36;1mBebida\033[37;1m/\033[36;1mBebidas Cadastradas\033[37;40;0m/\n")
					for p in n_bebida:
						print("\tID:{}\n\tNOME DA BEBIDA:{}\n\tVALOR DA BEBIDA:{}\n".format(id_b[a],n_bebida[a],vlr_bebida[a]))
						a = a+1
				elif resp_2 == 3:
					resp_ex_b=int(input("Digite o ID da bebida que você quer excluir:"))
					id_b.remove(id_b[resp_ex_b])
					n_bebida.remove(n_bebida[resp_ex_b])
					vlr_bebida.remove(vlr_bebida[resp_ex_b])
				elif resp_2 == 4:
					break
				elif resp_2 == 5:
					os.system('clear')
		elif resp_1 == 2:
			while (1):
				print("--------------------------------------------")
				print("\t/\033[34;1mMenu Principal\033[37;1m/\033[32;1mVenda\033[37;1m/\033[31;1mCardápio\033[37;40;0m/\n")
				print("\t1-Cadastrar\n\t2-Listar\n\t3-Excluir\n\t4-Voltar p/ menu\n\t5-Limpar tela")
				print("--------------------------------------------")
				resp_3=int(input("Opção:"))
				if resp_3 == 1:
					qntd_cadastro_c=int(input("Digite a quantidade de cadastros que ira fazer:"))
					for i in range(qntd_cadastro_c):
						id_c.append(i)
						n_comida.append(input("Digite o nome da comida:"))
						vlr_comida.append(input("Digite o valor da comida:"))
				elif resp_3 == 2:
					a=0
					print("--------------------------------------------")
					print("\t/\033[34;1mMenu Principal\033[37;1m/\033[32;1mVenda\033[37;1m/\033[31;1mCardápio\033[37;1m/\033[31;1mComidas Cadastradas\033[37;40;0m/\n")
					for p in n_comida:
						print("\tID:{}\n\tNOME COMIDA:{}\n\tVALOR COMIDA:{}\n".format(id_c[a],n_comida[a],vlr_comida[a]))
						a = a+1
				elif resp_3 == 3:
					resp_ex=int(input("Digite o ID da comida que você quer excluir:"))
					id_c.remove(id_[resp_ex])
					n_comida.remove(nome[resp_ex])
					vlr_comida.remove(cpf[resp_ex])
					print("Id {} removido com sucesso!".format(resp_ex))
				elif resp_3 == 4:
					break
					os.system('clear')
				elif resp_3 == 5:
					os.system('clear')
				else:
					print("Opção Inválida!\n")
		elif resp_1 == 3:
			os.system('clear')
	elif resp_0 == 2:
		while (1):
			print("--------------------------------------------")
			print("\t/\033[34;1mMenu Principal\033[37;1m/\033[33;1mFunções\033[37;40;0m/\n")
			print("\t1-Cadastrar\n\t2-Listar\n\t3-Excluir\n\t4-Voltar p/ o Menu\n\t5-Limpar tela")
			print("--------------------------------------------")
			resp_2=int(input("Opção:"))
			os.system('clear')
			if resp_2 == 1:
				qntd_cadastro=int(input("Digite a quantidade de cadastros que ira fazer:"))
				for i in range(qntd_cadastro):
					id_.append(i)
					nome.append(input("Digite o nome:"))
					cpf.append(input("Digite o CPF:"))
					email.append(input("Digite o email:"))
					senha.append(input("Digite o senha:"))
			elif resp_2 == 2:
				a=0
				print("--------------------------------------------")
				print("\t/\033[34;1mMenu Principal\033[37;1m/\033[33;1mFunções\033[37;1m/\033[33;1mPessoas Cadastradas\033[37;40;0m/\n")
				for p in nome:
					print("\tID:{}\n\tNOME:{}\n\tCPF:{}\n\tEMAIL:{}\n\tSENHA:{}\n".format(id_[a],nome[a],cpf[a],email[a],senha[a]))
					a = a+1
			elif resp_2 == 3:
				resp_ex=int(input("Digite o ID do usuário que você quer excluir:"))
				id_.remove(id_[resp_ex])
				nome.remove(nome[resp_ex])
				cpf.remove(cpf[resp_ex])
				email.remove(email[resp_ex])
				senha.remove(senha[resp_ex])
				print("Id {} removido com sucesso!".format(resp_ex))
			elif resp_2 == 4:
				break
				os.system('clear')
			elif resp_2 == 5:
				os.system('clear')
			else:
				print("Opção Inválida!\n")
	elif resp_0 == 3:
		print("Saindo..")
		os.system('sleep 2')
		break
	elif resp_0 == 4:
		os.system('clear')
	elif resp_0 == 5:
		hora = os.popen('date "+%d/%m/%Y %H:%M:%S"').read()
		os.system('clear')
		print("--------------------------------------------")
		print("\t/\033[34;1mMenu Principal\033[37;1m/\033[32;1mComprar\033[37;40;0m/\n")
		resposta_n=int(input("Id do usuario p/ comprar:"))
		resposta_b=int(input("Id da bebiba p/ comprar:"))
		resposta_c=int(input("Id da comida p/ comprar:"))
		cpf_=str(input("\nCPF na nota SR? s/n\n"))
		os.system('clear')
		print("Gerando seu cupom fiscal, aguarde...")
		os.system('sleep 5')
		print("\033[36;1m")
		os.system('clear')
		print("------------------------------------------")
		os.system('sleep 0.2')
		print("\tBUTIQUIN DO SEU LUÍS\t")
		os.system('sleep 0.2')
		print(" Rua Major Facundo, 500 - Centro\t")
		os.system('sleep 0.2')
		print("CEP:60025-100 Fortaleza - CE\t")
		os.system('sleep 0.2')
		print("------------------------------------------\n")
		os.system('sleep 0.2')
		print(hora)
		os.system('sleep 0.2')
		print("------------------------------------------")
		os.system('sleep 0.2')
		if cpf_ == 's' or cpf_ == 'S':
			print("CNPJ/CPF do consumidor:{}".format(cpf[resposta_n]))		
		print("NOME:{}".format(nome[resposta_n]))
		os.system('sleep 0.2')
		print("EMAIL:\033[36;4m{}\033[36;1m".format(email[resposta_n]))
		os.system('sleep 0.2')
		print("------------------------------------------")
		os.system('sleep 0.2')
		print("\t\033[36;6mCUPOM FISCAL\033[33;40;0m\033[36;1m")
		print("ID\tNOME\t\t\tVALOR(R$)")
		print("------------------------------------------")
		os.system('sleep 2')
		for i in id_b:
			print("{}\t{}\t\t\t{}".format(id_b[i],n_bebida[i],vlr_bebida[i]))
		for i in id_c:
			print("{}\t{}\t\t\t{}".format(id_c[i],n_comida[i],vlr_comida[i]))
		total=sum(vlr_comida+vlr_bebida)
		print("\nTOTAL R$\t\t\t{}".format(total))
		print("------------------------------------------")
		os.system('sleep 0.2')
		print("versão:1.0")
		print(" \033[32;1mU\033[33;1mT\033[34;1mD\033[37;1m\033[37;40m_\033[32;1mC\033[34;1mE\033[36;1m\t\t",hora)
		print("DEUS É FIEL , AMÉM IRMÃO")
		print("------------------------------------------\033[37;40;0m")
		break

	else:
		print("Opção Inválida!\n")
