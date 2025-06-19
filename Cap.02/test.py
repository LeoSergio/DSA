import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("? Anaconda estل funcionando no VS Code!")

# Criando um pequeno DataFrame
df = pd.DataFrame({
    'Aluno': ['Ana', 'Bruno', 'Carlos'],
    'Nota': [7.5, 4.2, 9.0]
})

print("\n?? DataFrame:")
print(df)

# Grلfico simples para testar o matplotlib
plt.bar(df['Aluno'], df['Nota'], color='skyblue')
plt.title('Notas dos Alunos')
plt.ylabel('Nota')
plt.ylim(0, 10)
plt.grid(True)
plt.show()