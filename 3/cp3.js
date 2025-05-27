function buscarNoticias(inputContent) {
    const apiKey = '137e588eb59902c5590d77aaff33f746'
    const correcaoPesquisa = encodeURIComponent(inputContent)//parece que serve para prevenir problemas com caracteres especiais na hora da pesquisa
    const url = `https://gnews.io/api/v4/search?q=${correcaoPesquisa}&lang=pt&token=${apiKey}`
    //parece que por padrão a api retorna 10 links de noticias
    fetch(url).then(resposta => resposta.json()).then(respostaConvertida => {
            const resultadoDiv = document.getElementById('resultado');

            if (!respostaConvertida.articles || respostaConvertida.articles.length === 0) {
                const semNoticias = document.createElement('p')
                semNoticias.innerText = '🔍 Nenhuma notícia encontrada.'
                resultadoDiv.appendChild(semNoticias)
                return
            }

            const tituloNoticias = document.createElement('h3')
            tituloNoticias.innerText = '📰 Notícias relacionadas:'
            resultadoDiv.appendChild(tituloNoticias)

            const lista = document.createElement('ul')
            respostaConvertida.articles.forEach(article => {
                const item = document.createElement('li')
                const link = document.createElement('a')
                link.href = article.url
                link.target = '_blank'
                link.innerText = article.title
                item.appendChild(link)
                lista.appendChild(item)
            });

            resultadoDiv.appendChild(lista)
        })
}

function resultado(texto, status, justificativa){ 
    const resultadoDiv = document.getElementById('resultado')
    const p =document.createElement('p')
    resultadoDiv.appendChild(p)
    resultadoDiv.style.display = 'block'
    resultadoDiv.className = status // o emoji não atrapalha pois quando se coloca um espaço entre as palavras é como se tivessemos duas classes e o css executa normalmente
    p.innerText = `Frase: ${texto}\nStatus: ${status}\nJustificativa: ${justificativa}`

}
function limpar(){
    const resultadoDiv = document.getElementById('resultado')
    resultadoDiv.innerHTML = ''
    resultadoDiv.style.display = 'none'
}

function mostrarHistorico(){
    if (!localStorage.getItem('historico')){
        alert('Nenhum histórico encontrado')
        document.getElementById('container').style.display = 'flex'
    }else{
        const historicoTabela = document.getElementById('historicoTabela')
        const voltarHistorico = document.getElementById('voltarHistorico')
        const container = document.getElementById('container')
        const tbodyHistorico = document.getElementById('tbodyHistorico')
        voltarHistorico.style.display = 'block'
        historicoTabela.style.display = 'block'
        for(let item of JSON.parse(localStorage.getItem('historico'))){
            const tr = document.createElement('tr')
            const tdFrase = document.createElement('td')
            const tdData = document.createElement('td')
            tdFrase.textContent = item.frase
            tdData.textContent = item.data
            tr.appendChild(tdFrase)
            tr.appendChild(tdData)
            tbodyHistorico.appendChild(tr)
            }
        voltarHistorico.addEventListener('click', (evento)=>{
            evento.preventDefault()
            historicoTabela.style.display = 'none'
            document.getElementById('container').style.display = 'block'
            container.style.display = 'flex'
            voltarHistorico.style.display = 'none'
            tbodyHistorico.innerHTML = ''
        })
    }
}

//aqui pegamos os dados do arquivo cp3.json
let bancoDeDados = null
fetch('./cp3.json').then(resposta => resposta.json()).then(respostaConvertida => {
    bancoDeDados = respostaConvertida
    console.log(bancoDeDados)
})
//aqui pegamos o texto escrito no input e verificamos se ele existe no banco de dados e se existe ele mostra o resultado
const buttonBuscar = document.getElementById('buscar')
buttonBuscar.addEventListener('click', (evento)=>{
    evento.preventDefault()
    limpar()
    const inputContent = (document.querySelector('input').value).toLowerCase().trim()
    //guardar historico
    console.log(localStorage.getItem('historico'))
    if (!localStorage.getItem('historico')){
        let historico = [
            {
                frase: inputContent,
                data: new Date().toLocaleString('pt-BR')
            }
        ]
        localStorage.setItem('historico', JSON.stringify(historico))
    }else{
        let historico = JSON.parse(localStorage.getItem('historico'))
        historico.push({frase: inputContent, data: new Date().toLocaleString('pt-BR')})
        localStorage.setItem('historico', JSON.stringify(historico))
    }
    //resultado da pesquisa
    let encontrou = false
    for(let itemFrase of bancoDeDados){
        if(inputContent == (itemFrase.frase).toLowerCase().trim()){
            console.log(inputContent)
            console.log(itemFrase.frase)
            console.log('Achou')
            resultado(itemFrase.frase, itemFrase.status, itemFrase.justificativa)
            encontrou = true
            break
        }
    } 
    if (!encontrou){
        console.log('Não achou')
        resultado('Frase não encontrada', 'error')
    }
    document.querySelector('input').value = ''
    // Parte 3: desafio extra
    buscarNoticias(inputContent)
})
//historico
const buttonHistorico = document.getElementById('historico')
buttonHistorico.addEventListener('click', (evento)=>{
    evento.preventDefault()
    document.getElementById('container').style.display = 'none'
    mostrarHistorico()
})