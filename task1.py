import pulp
#створюємо модель
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

#змінні які потрібно визначити
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')  
juice = pulp.LpVariable('juice', lowBound=0, cat='Integer') 

#задаємо обмеження
model += 2 * lemonade + juice <= 100
model += 1 * lemonade <= 50
model += 1 * lemonade <= 30
model += 2 * juice <= 40

#задаємо цільову функцію
model += lemonade + juice, "Maximize_Production"

#розв'язання
model.solve()

print("Виробляти лимонадів:", lemonade.varValue)
print("Виробляти соків:", juice.varValue)
print("Максимум напоїв:", lemonade.varValue + juice.varValue)

