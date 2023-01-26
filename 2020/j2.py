# Epidemiology - 15/15

population = int(input())
infected = newly_infected = int(input())
rate_of_infection = int(input())
days = 0


while infected <= population:
    days += 1
    newly_infected *= rate_of_infection
    infected += newly_infected


print(days)
