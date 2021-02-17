def analisador():
    arquivoEntrada = open("cep/lista.txt", "r", encoding='utf8')
    arquivoSaida = open("cep/listaFinal.txt", "w", encoding='utf8')
    for linha in arquivoEntrada:
        linha = list(linha)
        comecoLinha = linha[0:9]
        comecoLinha.append('|')
        
        fimLinha = linha[10:]
        try:     
            index = fimLinha.index('-') 
        except:
            print("Não foi")
        
        
        fimLinha = fimLinha[0:index-1] 

        linhaToda = comecoLinha + fimLinha

        linha = "".join(linhaToda)
        linha = linha + "\n"
        arquivoSaida.write(linha)
    arquivoEntrada.close()
    arquivoSaida.close()
analisador()