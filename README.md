В файле lemmatizer.ipynb -- лемматизатор для языка эсперанто и обработка текстов на этом языке

Использованные ресурсы: 1175 художественных текстов (175 сохранены как отдельные файлы + 1000 текстов из датасета художественной литературы на 300к предложений), полностью выгруженная википедия, 300к предложений из новостных ресурсов, 300к предложений из веб-страниц
Три корпуса, состоящие из 300к предложений (художественная, newscrawl и веб-страницы), не были разделены на отдельные документы, поэтому я разбила данные на блоки из 300 предложений 
В файле result.txt -- обработанные художественные тексты, в файле result_newscrawl_and_web.txt -- обработанные газеты + веб-страницы, в файле result_wiki.txt -- обработанная википедия
В файле vectorized_texts.txt -- обработанные тексты из result.txt, превращенные в последовательности векторов размерности 8