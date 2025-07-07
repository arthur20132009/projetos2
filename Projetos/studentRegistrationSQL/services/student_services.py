import dao.student_dao as dao
from models.student import Student

def create_record(name: str,email: str,age: int):
    Student = Student(name,email,age)
    #Validação dos dados e regras negocio
    #usuario informou  @ no e-mail
    #informou idade > 130
    if age >= 130:
        print("Erro Idade Incorreta")
        return

    if age < 18:
        print("Aceitamos matriculas apenas para alunos maiores de idade")
        return    
    
    # chamada para a camada 3  
    dao.inser_student(Student)