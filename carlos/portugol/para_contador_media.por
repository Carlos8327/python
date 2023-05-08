programa
{	
	inclua biblioteca Matematica --> Mat
	inclua biblioteca Util
	
	funcao inicio()
	{
		real soma = 0.0, numero, media
		inteiro contador1
		para(contador1 = 0; contador1 <5; contador1 ++){
			escreva("Digite um número para somar: ")
			leia(numero)
			soma += numero
		}

		media = soma / contador1
		escreva("Somando e Calculando a média...")
		Util.aguarde(1000)
		escreva("\nA média foi: " + Mat.arredondar(media, 2))
	}

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 436; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */