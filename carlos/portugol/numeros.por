programa
{
	
	funcao inicio()
	{
		inteiro numero, total = 0, par = 0, impar = 0, menor_impar = 0
		cadeia resposta

		faca{
			escreva ("Digite o " + (total + 1) + "º numero: ")
			leia(numero)
			total++

			se(numero % 2 == 0){
				par++
			}senao{
				impar++
				se(impar == 1){
					menor_impar = numero
				}senao{
					se(numero < menor_impar){
						menor_impar = numero
						}
					}
				}
			escreva("Quer continuar? [S/N]: ")
			leia(resposta)
		}
		enquanto(resposta != "N" e resposta != "n")
		escreva("\n===Resultados===")
		escreva("\n\nAo todo vc digitou " + total + " numeros.")
		escreva("\nO total de numeros PARES foi: " + par)
		escreva("\nO menor número ÍMPAR digitado foi: " + menor_impar)
		escreva("\n==========")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 728; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */