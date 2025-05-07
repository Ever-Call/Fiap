const frutas = ['maça', 'melancia', 'banana']
console.log(frutas[2])
const misturado = [1, 'dois', 3, 'quatro', true, null, undefined, { chave: 'valor' }]
console.log(misturado[5])
const cores = new Array('vermelho', 'preto', 'branco')//criando uma array usando construtor
console.log(cores)
const vazio = []
console.log(vazio)
const linguagens = ['javascript', 'java', 'python', 'c#']
const primeiraLinguagem = linguagens[0]
console.log(`A primeira linguagem é: ${primeiraLinguagem}`)
const ultimaLinguagem = linguagens[linguagens.length - 1]
console.log(`A ultima linguagem é: ${ultimaLinguagem}`)
let coresMutaveis = ['branco', 'azul', 'rosa']
coresMutaveis[1] = 'amarelo'
console.log(`Array após a alteração: ${coresMutaveis}`)
coresMutaveis[coresMutaveis.length] = 'roxo' // aqui ele criou uma nova posição e elemento no array
console.log(coresMutaveis.length)

let planetas = ['Terra', 'Marte']
// push() --> adciona um ou mais elementos ao final do array e retorna o novo comprimento da array
const novoComprimentoPush = planetas.push('Saturno', 'Urano');
console.log(planetas)
console.log(novoComprimentoPush)

//pop() --> remove o ultimo elemnto do meu array e retorna o elemento que foi removido
const ultimoPlanetaRemovido = planetas.pop()
console.log(ultimoPlanetaRemovido)
console.log(planetas)

//indexOf() --> retorna o primeiro índice em que um elemento pode ser encontrado
const indiceTerra = planetas.indexOf('Terra')
console.log(indiceTerra)

//join = juntar, agrupar... em jogos seria juntar-se?
//join() --> cria e retorna uma nova string concatenando todos os elementos do Array
const stringPlanetas = planetas.join('-')
console.log(stringPlanetas)

const coresInteracao = ['laranja', 'ciano', 'magenta']
for (let i = 0; i < coresInteracao.length; i++) {
    console.log(`Cor no índice ${i}: ${coresInteracao[i]}`)
}

// laço 'for...of' (mais moderno e legível para iterar sobre os valorse)
for (const cor of coresInteracao) {
    console.log(`Cor: ${cor}`)
}
coresInteracao.forEach(function (cor, indice) {
    console.log(`Cor: ${cor} no índice: ${indice}`)
})

//Este trecho é o codigo de input pelo terminal usado o node
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

//Cria uma array vazio para armazenar os itens da lista de compras do usuário  
const listaCompras = []

//Cria uma função para adicionar um item na lista de compra 
function adicionarItem() {
    readline.question('Digite um item para adicionar a lista de compras (ou "fim" para sair): ', (item) => {
        const itemFormatado = item.trim() //remove os espaços em branco extras do parametro item
        //Veririfica se o úsuario digitou 'fim' (ignorando caixa alta/baixa)
        if (itemFormatado.toLowerCase() === 'fim') {
            //se o usuário digitou 'fim', encerra a interação com o terminal 
            console.log('\nSua lista de compra completa:')
            //itera sobre cada item no array 'listaCompras'
            listaCompras.forEach((produto, indice) => {
                console.log(`${indice + 1}. ${produto}`)
                readline.close();
            })
        } else if (itemFormatado !== '') {
            listaCompras.push(itemFormatado)
            console.log(`"${itemFormatado}" foi adicionado à sua lista.`)
            adicionarItem()
        } else {
            //se o usuário digitos espaços ou nada 
            console.log('Por favor, digite um item válido.')
            adicionarItem()
        }
    });
}
//Inicia o processo de adicionar itens à lista de compras chamando a função 
adicionarItem()