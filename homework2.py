import random;

phrases = [
	"Если для женщин все мужики одинаковы, то почему они еще выбирают?!",
	"Жизнь грустная, зато зарплата смешная",
	"В споре с круглым дураком и зацепиться-то не за что",
	"Честного судью ищите по заштопанной мантии",
	"Кто в армии служил, тот в цирке не смеется"		
];


while True:
	i = input("-> ");
	if(i == "Скажи мудрость"):
		print(phrases[random.randint(0, len(phrases) - 1)]);
	elif(i == "Знать ничего не хочу"):
		print("Ok(((");
	elif(i == "Выйти"):
		break;
	else:
		print("Неверный ввод");
