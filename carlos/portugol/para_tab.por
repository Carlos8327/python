programa
{
	inclua biblioteca Util -->u 
     funcao inicio()
    {
		inteiro tab,per
		escreva("Qual o numero ? ")
			leia(per)

		para (inteiro mutiplicador=1; mutiplicador<=10; mutiplicador++)
		{
			
			tab=mutiplicador*per
			escreva (per+" x ", mutiplicador, " = ", tab, "\n")
			u.aguarde(300)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 309; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */