# Criamos uma CLASSE chamada 'bicileta' (observação: por convenção, nomes de classes em Python 
# começam com letra maiúscula, então o ideal seria 'Bicicleta').
# Classes são moldes que definem ATRIBUTOS (características) e MÉTODOS (comportamentos) 
# que os objetos criados a partir delas terão.
class bicileta:
    
    # O método __init__ é chamado de CONSTRUTOR.
    # Ele é executado automaticamente quando criamos um objeto a partir dessa classe.
    # Serve para inicializar os atributos do objeto.
    # OBS: os parâmetros entre parênteses (cor, modelo, ano, valor, aro=18) precisam ser passados
    # quando criamos o objeto, exceto 'aro', que tem um valor padrão (18).
    def __init__(self, cor, modelo, ano, valor, aro=18):
        # 'self' representa a própria instância (o próprio objeto criado).
        # Assim, self.cor é o atributo do objeto, que recebe o valor passado pelo usuário.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1  # A bicicleta começa sempre na marcha 1.

    # O método __str__ é um método especial do Python que retorna uma representação textual do objeto.
    # Ele é chamado automaticamente quando usamos 'print(objeto)'.
    def __str__(self):
        # Aqui usamos 'self.__class__.__name__' para pegar o nome da classe (bicileta)
        # e 'self.__dict__' que contém todos os atributos do objeto em um dicionário {atributo: valor}.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    # Método 'buzinar': faz a bicicleta buzinar.
    def buzinar(self):
        print("plim, plim....")
    
    # Método 'parar': simula a bicicleta parando.
    def parar(self):
        print("A bicicleta parando...")
        print("A bicicleta está parada")

    # Método 'correr': simula a bicicleta andando.
    def correr(self):
        print("A bicicleta está correndo")
        print("Vrummm.....")

    # Método get_cor: retorna a cor da bicicleta.
    # Este método existe porque, em algumas situações, não queremos que o atributo seja acessado diretamente.
    # Podemos controlar o acesso criando métodos que retornam (get) ou alteram (set) valores.
    def get_cor(self):
        return self.cor
    
    # Método 'trocar_marcha': responsável por trocar a marcha da bicicleta.
    # Note que ele recebe um parâmetro 'nr_marcha' (número da nova marcha).
    def trocar_marcha(self, nr_marcha):
        print("Trocando marcha")

        # Aqui temos uma função interna chamada '_trocar_marcha' (perceba o underline no início).
        # Usar o underline em nomes de funções/métodos é uma convenção do Python para dizer:
        # "isso é um detalhe interno, não deve ser chamado diretamente fora da classe".
        def _trocar_marcha(nro_marcha):
            # Aqui comparamos a marcha solicitada (nro_marcha) com a marcha atual (self.marcha).
            if nro_marcha > self.marcha:
                # Se a nova marcha for maior que a atual, a troca é feita.
                print(f'Marcha trocada, agora estamos na marcha {nr_marcha}')
                self.marcha = nro_marcha
            else:
                # Se a nova marcha for menor ou igual à atual, a troca não será feita.
                print("Não foi possível a troca da marcha.")

        # Aqui chamamos a função interna passando a nova marcha.
        _trocar_marcha(nr_marcha)
    

# Criamos um objeto (ou instância) da classe 'bicileta' chamado 'bicileta1'.
# Estamos passando os valores necessários: cor, modelo, ano, valor e aro.
bicileta1 = bicileta("Azul", "Cross", 2020, 3000, 20 )

# Chamando os métodos do objeto:
bicileta1.buzinar()   # Faz a bicicleta buzinar
bicileta1.parar()     # Faz a bicicleta parar
bicileta1.correr()    # Faz a bicicleta correr

# Podemos acessar atributos diretamente (não é a melhor prática, mas é permitido)
print(bicileta1.cor, bicileta1.ano, bicileta1.modelo, bicileta1.valor)

# Chamando o método get_cor (boa prática para acessar atributos)
print(bicileta1.get_cor())

# Quando usamos 'print' no objeto, o método __str__ é chamado automaticamente.
print(bicileta1)

# Chamando o método trocar_marcha
print(bicileta1.trocar_marcha(3))