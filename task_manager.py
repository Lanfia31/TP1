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

#def mark_task_as_done():
  # À compléter...

while True:
  print("\nChoisissez une action :")
  print("1. Afficher les tâches")
  print("2. Ajouter une tâche")
  print("3. Marquer une tâche comme terminée")
  print("4. Quitter")

  choice = input("> ")

  if choice == '1':
    show_tasks()
  elif choice == '2':
    add_task()
  #elif choice == '3':
    #mark_task_as_done()
  elif choice == '4':
    break
  else:
    print("Choix invalide.")
