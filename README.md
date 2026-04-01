# Validador de CPF (Formato) com Pytest 🧪

Projeto prático para validação de padrão de string (Regex) e implementação de testes unitários automatizados.

### 📋 Cenários Testados:
* **CPF Válido**: Formato `000.000.000-00`.
* **Sem Pontuação**: Rejeição de strings apenas numéricas.
* **Caracteres Inválidos**: Falha ao detectar letras.
* **Entradas Nulas/Vazias**: Tratamento de erro para `None` e `""`.

### 🛠️ Tecnologias:
* **Python**
* **Pytest** (Framework de Testes)
* **Regex** (Expressões Regulares)

### ⚙️ Como rodar:
```bash
pip install pytest
pytest test_meu_primeiro.py -v


Desenvolvido por Josicleide Rodrigues! Com foco em QA e automação.

### Como subir rápido pelo terminal:
1. Digite: `notepad README.md`
2. Cole o código acima, salve e feche.
3. No terminal, rode estes 3 comandos:
   ```bash
   git add README.md
   git commit -m "Add README"
   git push origin master
