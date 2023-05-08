programa
{
	
	inclua biblioteca Util
	
	funcao inicio()
	{
		inteiro inicio_sorteio = 0, fim_sorteio = 0, numeros_sorteio
		escreva("\nQuantos números serão sorteados? ")
		leia(numeros_sorteio)
		escreva("\nInicio do Sorteio: ")
		leia(inicio_sorteio)
		escreva("\nFim do Sorteio: ")
		leia(fim_sorteio)
		escreva("-------------")
		escreva("Sorteando os " + numeros_sorteio + " números\n")
		escreva("-------------")
		inteiro contador2 = 1, numeros, soma_numeros
		
		enquanto (contador2 <= numeros_sorteio){
			numeros = sorteia(inicio_sorteio,fim_sorteio)
			soma_numeros =+ numeros
			escreva("\t" + numeros + " - ")
			Util.aguarde(500)
			contador2 ++
			
			}

		escreva("\nEncerrado Sorteio!\n")
		escreva("Somando, aguarde ...\n")
		escreva("O resultado da soma dos números sorteados !")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 798; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */