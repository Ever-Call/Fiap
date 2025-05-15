function pg(numero, razao) {
    let listaDeNumeros = []
    let numeroSeguinte = numero
    for (let i = 0; i < 5; i++) {
        numeroSeguinte = numeroSeguinte * razao
        listaDeNumeros[i] = numeroSeguinte
    }
    console.log(listaDeNumeros)
    return listaDeNumeros
}
function pa(numero, razao) {
    let listaDeNumeros = []
    let numeroSeguinte = numero
    for (let i = 0; i < 5; i++) {
        numeroSeguinte = numeroSeguinte + razao
        listaDeNumeros[i] = numeroSeguinte
    }
    console.log(listaDeNumeros)
    return listaDeNumeros
}
function personalizado(numeroAtual, numeroAnterior) {
    let listaDeNumeros = []
    let numeroSeguinte = 0
    let index_1 = numeroAtual
    let index_2 = numeroAnterior
    for (let i = 0; i < 5; i++) {
        numeroSeguinte = index_1 + index_2
        listaDeNumeros[i] = numeroSeguinte
        index_2 = index_1
        index_1 = numeroSeguinte
    }
    console.log(listaDeNumeros)
    return listaDeNumeros
}
function verificador(lista) {
    const ultimoNumero = lista[2]
    const razaoPA_1 = lista[1] - lista[0]
    const razaoPA_2 = lista[2] - lista[1]
    const razaoPG_1 = lista[1] / lista[0]
    const razaoPG_2 = lista[2] / lista[1]
    let tipo = ''
    let resultado = []
    if (razaoPA_1 == razaoPA_2) {
        resultado = pa(ultimoNumero, razaoPA_1)
        tipo = 'O Padrão identificado é uma Progressão Aritmética: '
    } else if (razaoPG_1 == razaoPG_2) {
        resultado = pg(ultimoNumero, razaoPG_1)
        tipo = 'O Padrão identificado é uma Progressão Geométrica: '
    } else {
        resultado = personalizado(lista[2], lista[1])
        tipo = 'O Padrão identificado é um Padrão Pesonalizado: '
    }
    resultado = `${tipo} ${lista},${resultado}`
    return resultado
}

function iniciar() {
    const num_1 = parseInt(document.getElementById('num_1').value)
    const num_2 = parseInt(document.getElementById('num_2').value)
    const num_3 = parseInt(document.getElementById('num_3').value)
    const p = document.getElementById('resultado')
    // console.log(num_1)
    // console.log(num_2)
    // console.log(num_3)
    // console.log(typeof (num_1))
    listaInicial = [num_1, num_2, num_3]
    p.textContent = verificador(listaInicial)

}