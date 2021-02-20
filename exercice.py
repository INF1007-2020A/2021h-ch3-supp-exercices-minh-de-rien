#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2 / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	if v1[0]*v2[0] + v1[1]*v2[1] == 0:
		return True

	return False

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	total, nbr_de_valeurs = 0, 0

	for v in values: # La variable v contient une valeur de la liste.
		if v >= 0:
			total += v
			nbr_de_valeurs += 1

	return total / nbr_de_valeurs

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties, tens, fives, twos, ones = 0, 0, 0, 0, 0

	while value != 0:
		if value >= 20:
			twenties = value // 20
			value %= 20
		elif value >= 10:
			tens = value // 10
			value %= 10
		elif value >= 5:
			fives = value // 5
			value %= 5
		elif value >= 1:
			ones = value // 1
			value %= 1

	return (twenties, tens, fives, twos, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))