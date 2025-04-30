for (let i = 0; i < 5; i++) {
    console.log(`Número: ${i}`)

}
let contador = 0

while (contador < 3) {
    console.log(`Contador está em ${contador}`)
    contador++
}

const pessoa = {
    nome: 'Ana',
    idade: 30,
    cidade: 'São Paulo'
}
console.log(pessoa)
// visualização do objeto de forma mais limpa eu acho
for (const propriedade in pessoa) {
    console.log(`${propriedade}: ${pessoa[propriedade]}`)
}
const cores = ['vermelho', 'azul', 'preto']
// visualização do array cores
for (const cor of cores) {
    console.log(cor)
}

const resultadoDiv = document.getElementById('resultado')

// metodo é uma função dentro do meu objeto
const carro = {
    marca: 'Forda',
    modelo: 'Mustang',
    ano: '2007',
    cor: 'Azul',
    ligar: function () {
        console.log('O carro está ligado!!!')
        exibirMensagemNoNavegador('O carro está ligado');
    },
    obterDetalhes: function () {    //obterDetalhes é um metodo tbm
        return `${this.marca} ${this.modelo} ${this.ano}` // this se refere ao objeto 'carro' 
    }
}
console.log('---Objeto Literal---')
console.log(`Marca: ${carro.marca}`)// acessando a propriedade marca usando .
console.log(`Modelo: ${carro['modelo']}`)//acessando a propriedade modelo usando []
carro.ligar()// chamando o método ligar usando a notação usando .

const detalhesCarro = carro.obterDetalhes()// se não colocar o 
console.log(`Detalhes do carro: ${detalhesCarro}`)
exibirMensagemNoNavegador(`Detalhes do carro : ${detalhesCarro}`)

console.log('---Exibindo Objeto---')
for (const propriedade in carro) {
    console.log(`${propriedade}: ${carro[propriedade]}`)
}

// Outra forma de exibir um objeto (converte o objeto para uma String JSON)
const carroJSON = JSON.stringify(carro)
console.log(`Objeto carro no formato JSON: ${carroJSON}`)
exibirMensagemNoNavegador(`Objeto carro no formato JSON: ${carroJSON}`)

//Funções construtoras
//Uma função construtora é usada para criar multiplos objetos com uma única função
//Usamos a palavra chave "new" para invocar um construtor
function Pessoa(nome, idade, profissao) {
    this.nome = nome,
        this.idade = idade,
        this.profissao = profissao,
        this.saudar = function () {
            console.log(`Olá, meu nome é ${this.nome} e eu sou ${this.profissao}.`)
        }
}

//Criando instâncias (objetos) da função construtora Pessoa usando o 'new'
const pessoa1 = new Pessoa('Carlos', 32, 'engenheiro de software')
const pessoa2 = new Pessoa('Diego', 18, 'engenheiro de software')
console.log('---funções Construtoras----')
console.log(`Nome da pessoa 1: ${pessoa1.nome}`)
pessoa1.saudar()
console.log(`Nome da pessoa 1: ${pessoa2.nome}`)
pessoa2.saudar()


function exibirMensagemNoNavegador(mensagem) {
    const paragrafo = document.createElement('p')
    paragrafo.textContent = mensagem
    resultadoDiv.appendChild(paragrafo)
}
