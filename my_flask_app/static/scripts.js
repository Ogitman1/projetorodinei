document.getElementById('btn-gerar-grafico-notas').addEventListener('click', function() {
    document.getElementById('loading-screen').style.display = 'flex'
    fetch('/grafalunos', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('loading-screen').style.display = 'none'
            if (data.success) {
                document.getElementById('grafico-notas').src = data.graph_url;
                document.getElementById('grafico-container-notas').style.display = 'block';
                document.getElementById('popup').style.display = 'flex' //aparecer o popup
                alert('Gráfico de notas gerado com sucesso!')
            } else {
                alert('Ocorreu um erro ao gerar o gráfico de notas.');
                document.getElementById('loading-screen').style.display = 'none'
            }
            setTimeout( function(){ //popup some depois de 3 segundos
                document.getElementById('popup').style.display = 'none'
            },3000)
        })
        .catch(error => {
            console.error('Erro ao gerar o gráfico de notas:', error);
            alert('Ocorreu um erro ao gerar o gráfico de notas.');
            document.getElementById('loading-screen').style.display = 'none'
        });
});




document.getElementById('btn-gerar-grafico-satisfacao').addEventListener('click', function() {
    document.getElementById('loading-screen').style.display = 'flex'
    fetch('/grafnotas', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('loading-screen').style.display = 'none'
            if (data.success) {
                document.getElementById('grafico-satisfacao').src = data.graph_url;
                document.getElementById('grafico-container-satisfacao').style.display = 'block';
                document.getElementById('popup').style.display = 'flex' //aparecer o popup
                alert('Gráfico de satisfação gerado com sucesso!');
            } else {
                alert('Ocorreu um erro ao gerar o gráfico de satisfação.');
                document.getElementById('loading-screen').style.display = 'none'
            }
            setTimeout( function(){ //popup some depois de 3 segundos
                document.getElementById('popup').style.display = 'none'
            },3000)
        })
        .catch(error => {
            console.error('Erro ao gerar o gráfico de satisfação:', error);
            alert('Ocorreu um erro ao gerar o gráfico de satisfação.');
            document.getElementById('loading-screen').style.display = 'none'
        });
});

function verificarStatusBancoDados() { //código de verificação dos status do servidor/banco de dados
    fetch('/status-banco-dados')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const statusBancoDadosElement = document.getElementById('status-banco-dados');
                statusBancoDadosElement.textContent = data.status_banco_dados;
                
                
                if (data.status_banco_dados === 'Online') {
                    statusBancoDadosElement.classList.remove('offline');
                    statusBancoDadosElement.classList.add('online');
                } else {
                    statusBancoDadosElement.classList.remove('online');
                    statusBancoDadosElement.classList.add('offline');
                }
                
            } else {
                console.error('Erro ao verificar status do banco de dados.');
            }
        })
        .catch(error => {
            console.error('Erro ao verificar status do banco de dados:', error);
        });
}

// Chamar a função para verificar o status do banco de dados quando a página for carregada
window.onload = verificarStatusBancoDados;