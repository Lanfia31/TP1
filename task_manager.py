tasks = []

def add_task():
  task = input("Entrez une nouvelle tâche : ")
  tasks.append(task)
  print("Tâche ajoutée !")

def show_tasks():
  if not tasks:
    print("La liste des tâches est vide.")
  else:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")

def mark_task_as_done():
    print ("Marqué une tâche comme terminée")
    if not tasks:
      print("Aucune tâche")
      return
def sort_tasks():
  print("Les tâches sont affichees par odre alphabetique")
  if not tasks:
        print("Pas de tâches à afficher")
  
  else: 
    tasks.sort()
    print("Les tâches sont affichées dans l'ordre alphabetique")

while True:
  print("\nChoisissez une action :")
  print("1. Afficher les tâches")
  print("2. Ajouter une tâche")
  print("3. Marquer une tâche comme terminée")
  print("4.Trier par ordre alphabétique")
  print("5. Quitter")

  choice = input("> ")

  if choice == '1':
    show_tasks()
  elif choice == '2':
    add_task()
  elif choice == '3':
    mark_task_as_done()
  elif choice == '4':
    sort_tasks()
  elif choice == '5':
    break
  else:
    print("Choix invalide.")
