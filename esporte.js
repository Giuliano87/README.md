// Menu Mobile// Dados da tabela (simulados - na prática, viriam de uma API)
const classificacao = {
    'serie-a': [
        { posicao: 1, time: 'Flamengo', pts: 65, pj: 30, vit: 20, e: 5, der: 5, sg: 32, escudo: 'flamengo.png' },
        { posicao: 2, time: 'Palmeiras', pts: 63, pj: 30, vit: 19, e: 6, der: 5, sg: 28, escudo: 'palmeiras.png' },
        // Adicione mais times...
    ],
    'serie-b': [
        { posicao: 1, time: 'Cruzeiro', pts: 58, pj: 28, vit: 17, e: 7, der: 4, sg: 25, escudo: 'cruzeiro.png' },
        // Adicione mais times...
    ]
};

function carregarTabela() {
    // Carrega Série A
    const tabelaA = document.getElementById('tabela-serie-a');
    classificacao['serie-a'].forEach(time => {
        tabelaA.innerHTML += `
            <tr>
                <td>${time.posicao}</td>
                <td class="time-cell">
                    <img src="images/escudos/${time.escudo}" alt="${time.time}" class="escudo">
                    ${time.time}
                </td>
                <td><strong>${time.pts}</strong></td>
                <td>${time.pj}</td>
                <td>${time.vit}</td>
                <td>${time.e}</td>
                <td>${time.der}</td>
                <td>${time.sg}</td>
            </tr>
        `;
    });

    // Carrega Série B
    const tabelaB = document.getElementById('tabela-serie-b');
    classificacao['serie-b'].forEach(time => {
        tabelaB.innerHTML += `
            <tr>
                <td>${time.posicao}</td>
                <td class="time-cell">
                    <img src="images/escudos/${time.escudo}" alt="${time.time}" class="escudo">
                    ${time.time}
                </td>
                <td><strong>${time.pts}</strong></td>
                <td>${time.pj}</td>
                <td>${time.vit}</td>
                <td>${time.e}</td>
                <td>${time.der}</td>
                <td>${time.sg}</td>
            </tr>
        `;
    });

    // Filtros
    document.querySelectorAll('.filtro-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.filtro-btn').forEach(b => b.classList.remove('ativo'));
            this.classList.add('ativo');
            
            document.querySelectorAll('.tabela-container').forEach(t => t.style.display = 'none');
            document.getElementById(this.dataset.tabela).style.display = 'block';
        });
    });
}

// Chamar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', carregarTabela);

// Exemplo: Adicionar mais jogadores
santosData.players.push(
    { id: 5, name: "Lucas Lima", position: "Meia", number: 10, photo: "url_da_foto" }
);