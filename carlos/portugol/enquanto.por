programa
{
	inclua biblioteca Util-->u  
	funcao inicio()
	{
		inteiro sorteado, inicio ,  fim,num,contador = 1,soma=0
		escreva("Quantos numeros , você vai querer sortear: ")
		leia(sorteado)
		escreva("\nInicio do sorteio: ")
		leia(inicio)
		escreva("\nfim do sorteio: ")
		leia(fim)
		escreva("\n--------------------------------")
		escreva("\nSorteando os "+sorteado+" números")
		escreva("\n--------------------------------\n")
		num = u.sorteia(inicio, fim)
		enquanto (contador <=sorteado){
			num = u.sorteia(inicio, fim)
			escreva(num, " - " )
			Util.aguarde(2000)
			contador++ 
			soma +=num
			}

		escreva("\nacabou")
		escreva("\nsomando aguade..... ")
		escreva("\n--------------------------------")

		escreva("\nA soma do sorteio foi: ",soma)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 671; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */