

from escola import Escola
from aluno import Aluno

from tkinter import*
from tkinter import  ttk, messagebox


class App:
    def __init__(self, nome:str, endereco: str) -> str:

        self.escola = Escola(nome, endereco)
        self.janela = Tk()
        self.janela.title(f'Sistema - {self.escola.nome}')
        self.janela.geometry('600x500')

        # label
        self.label_matricula = Label(self.janela, text='matricula', font='tahoma 14 bold', fg='red')
        self.label_matricula.grid(row=0, column=0)

        # entry
        self.text_matricula = Entry(self.janela, font='tahoma 14 bold', width=27, state=DISABLED)
        self.text_matricula.grid(row=0, column=1)

        # nome
        self.label_nome = Label(self.janela, text='nome', font='tahoma 14 bold', fg='red')
        self.label_nome.grid(row=1, column=0)

        
        self.text_nome = Entry(self.janela, font='tahoma 14 bold', width=27)
        self.text_nome.grid(row=1, column=1)

        # idade
        self.label_idade = Label(self.janela, text='idade', font='tahoma 14 bold', fg='red')
        self.label_idade.grid(row=2, column=0)

        # entry
        self.text_idade = Entry(self.janela, font='tahoma 14 bold', width=27)
        self.text_idade.grid(row=2, column=1)

        # curso
        self.label_curso = Label(self.janela, text='curso', font='tahoma 14 bold', fg='red')
        self.label_curso.grid(row=3, column=0)

        self.combo_curso = ttk.Combobox(self.janela, font='tahoma 14 bold', values=['Java', 'Python','Javascript', 'Node'], width=26, state='readonly')
        self.combo_curso.grid(row=3,column=1)

        # nota
        self.label_nota = Label(self.janela, text='nota', font='tahoma 14 bold', fg='red')
        self.label_nota.grid(row=4, column=0)

     
        self.text_nota = Entry(self.janela, font='tahoma 14 bold', width=27)
        self.text_nota.grid(row=4, column=1)


        # button

        self.btn_adicionar = Button(self.janela, text='Adicionar', font='tahoma 14 bold' , width=7, fg='red', command=self.addAluno)
        self.btn_adicionar.grid(row=5, column=0, padx=20, pady=25)

        self.btn_editar = Button(self.janela, text='editar', font='tahoma 14 bold' , width=7, fg='red', command=self.editarAluno)
        self.btn_editar.grid(row=5, column=1,padx=20, pady=25)

        self.btn_excluir = Button(self.janela, text='excluir', font='tahoma 14 bold' , width=7, fg='red', command=self.excluirAluno)
        self.btn_excluir.grid(row=5, column=2,padx=20, pady=25)


        # frame

        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)
        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas,
                                   show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)


        


        #bind
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)
        self.tabela.pack()



        self.atualizarTabela()
        self.janela.mainloop()

    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        
        for aluno in self.escola.alunos:
            self.tabela.insert('', END, values=(aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota))




    def limparCampos(self):

        self.text_matricula.config(state=NORMAL)
        self.text_matricula.delete(0, END)
        self.text_matricula.config(state=DISABLED)
        self.text_nome.delete(0, END)
        self.text_idade.delete(0, END)
        self.combo_curso.set('')
        self.text_nota.delete(0, END)


    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        item = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()

        #inserir valores
        self.text_matricula.config(state=NORMAL)
        self.text_matricula.insert(0, item[0])
        self.text_matricula.config(state=DISABLED)
        self.text_nome.insert(0, item[1])
        self.text_idade.insert(0, item[2])
        self.combo_curso.set(item[3])
        self.text_nota.insert(0, item[4])
        
        
    
    def criarAlunos(self):
        nome = self.text_nome.get()
        idade = int(self.text_idade.get())
        curso = self.combo_curso.get()
        nota = float(self.text_nota.get())
        aluno = Aluno(nome, idade, curso, nota)

        return aluno
    
    def addAluno(self):
        aluno = self.criarAlunos()
        self.escola.cadastrarAluno(aluno)
        self.atualizarTabela()
        self.limparCampos()
        messagebox.showinfo('Sucesso, aluno cadastrado!')
        
        print(self.escola.alunos)

    def editarAluno(self):
        aluno = self.criarAlunos()
        aluno.matricula = self.text_matricula.get()
        self.escola.editarAluno(aluno)
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo('Sucesso, dados alterados!')


    def excluirAluno(self):
        matricula = self.text_matricula.get()
        self.escola.deletarAluno(matricula)
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo('Sucesso, aluno excluido!')
        pass
        



App('Escola de Tecnologia', 'Av. Dom Luis')