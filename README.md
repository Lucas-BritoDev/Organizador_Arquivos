# 🚀 Organizador Automático de Downloads com Python 📂✨

Você já se perdeu no meio de tantos arquivos na pasta Downloads? PDFs misturados com imagens, planilhas ao lado de executáveis... A bagunça digital é real e pode consumir um tempo precioso! 😅

Este projeto apresenta um script em Python simples, mas poderoso, projetado para trazer ordem ao caos da sua pasta de Downloads, categorizando automaticamente os arquivos e movendo-os para subpastas organizadas por tipo de extensão.

## 🎯 O Problema Resolvido

A pasta "Downloads" frequentemente se torna um repositório desorganizado de arquivos de todos os tipos, dificultando a localização de itens específicos e ocupando espaço de forma ineficiente. Este script visa automatizar o processo de organização, economizando seu tempo e melhorando sua produtividade.

## ⚙️ Funcionalidades Principais

O script realiza as seguintes ações:

✅ **Escaneia a pasta Downloads:** Identifica todos os arquivos presentes no diretório especificado.
✅ **Cria diretórios por tipo:** Automaticamente cria subpastas nomeadas de acordo com as extensões dos arquivos encontrados (ex: "PDFs", "Imagens_PNG", "Planilhas_XLSX", etc.).
✅ **Move os arquivos:** Transfere cada arquivo para a subpasta correspondente à sua extensão.
✅ **Trata arquivos sem extensão:** Arquivos sem uma extensão definida também são movidos para uma pasta específica (ex: "Sem_Extensao"), garantindo que nada fique para trás.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* Módulos padrão do Python:
    * `os` (para interações com o sistema de arquivos, como listar arquivos e criar diretórios)
    * `shutil` (para mover arquivos)


## ⚠️ Atenção

* **Faça um backup:** Antes de executar o script pela primeira vez em uma pasta de Downloads importante, é sempre uma boa prática fazer um backup dos seus arquivos, por precaução.
* **Teste em uma pasta de exemplo:** Considere testar o script em uma pasta com alguns arquivos de teste para ver seu funcionamento antes de aplicá-lo à sua pasta principal de Downloads.

## 💡 Potenciais Melhorias Futuras

* Adicionar um arquivo de configuração para o caminho da pasta Downloads e outras preferências.
* Permitir que o usuário defina mapeamentos de extensão personalizados (ex: mover `.jpg` e `.jpeg` para uma pasta "Imagens_JPG").
* Interface gráfica (GUI) para facilitar o uso.
* Opção para agendar a execução do script (ex: diariamente).
* Log de operações realizadas.

## 🤝 Contribuindo

Sinta-se à vontade para abrir *issues* com sugestões, reportar bugs ou enviar *pull requests* com melhorias!

---

*Pequenos scripts podem salvar nosso tempo e aumentar a produtividade! Se você já automatizou algo no seu dia a dia com Python, compartilhe suas ideias!*
