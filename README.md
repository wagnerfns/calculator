# Calculator
[![Build Status](https://travis-ci.org/wagnerfns/calculator.svg?branch=master)](https://travis-ci.org/wagnerfns/calculator)

Este é um repositório para estudo e prática de integração contínua(CI) em Python utilizando Travis como ferramenta de CI.

### Pré-requisitos

Para utilizar o [Travis CI](https://travis-ci.org/) é necessário possuir uma conta e sincronizar ela ao GitHub, para aprender configurar acesse [Como usar o Travis em 15 passos](https://imasters.com.br/back-end/como-usar-o-travis-em-15-passos) 

Para executar o teste localmente você precisa ter instalado ```pip install -U pytest``` e ```pip install unittest2```.

### Como executar o teste local
Acesse o diretório calculator, para executar o teste localmente use o comando ```pytest```. 

Resultado esperado:
```
====================================== test session starts =======================================
platform linux -- Python 3.6.5, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
rootdir: /home/user/calculator, inifile:
plugins: remotedata-0.2.1, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
collected 6 items                                                                                

tdd/test_core.py ......                                                                    [100%]

==================================== 6 passed in 0.02 seconds ====================================
