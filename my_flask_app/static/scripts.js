document.getElementById('btn-gerar-grafico-notas').addEventListener('click', function() {
    fetch('/grafalunos', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('grafico-notas').src = data.graph_url;
                document.getElementById('grafico-container-notas').style.display = 'block';
                alert('Gráfico de notas gerado com sucesso!')
            } else {
                alert('Ocorreu um erro ao gerar o gráfico de notas.');
            }
        })
        .catch(error => {
            console.error('Erro ao gerar o gráfico de notas:', error);
            alert('Ocorreu um erro ao gerar o gráfico de notas.');
        });
});




document.getElementById('btn-gerar-grafico-satisfacao').addEventListener('click', function() {
    fetch('/grafnotas', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('grafico-satisfacao').src = data.graph_url;
                document.getElementById('grafico-container-satisfacao').style.display = 'block';
                alert('Gráfico de satisfação gerado com sucesso!');
            } else {
                alert('Ocorreu um erro ao gerar o gráfico de satisfação.');
            }
        })
        .catch(error => {
            console.error('Erro ao gerar o gráfico de satisfação:', error);
            alert('Ocorreu um erro ao gerar o gráfico de satisfação.');
        });
});
