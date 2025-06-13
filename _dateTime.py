from datetime import datetime, timedelta

now = datetime.now()
print("now:")
print(now)

# add 10 dias depois de agora
future = now + timedelta(days=10)
print("10 dias depois de agora:")
print(future)

# Subtract 5 dias de agora
past = now - timedelta(days=5)
print("5 dias atrás de agora:")
print(past)

#Diferença entre as datas
diff = future - past
print("Diferença entre as datas:")
print(diff)

date1 = datetime(2021, 10, 10)
date2 = datetime(2025, 6, 10) 

# Diferença em dias entre as datas




