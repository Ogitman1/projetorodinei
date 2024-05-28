document.getElementById('btn-gerar-grafico').addEventListener('click', function() {
    fetch('/grafalunos', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('grafico').src = data.graph_url;
                document.getElementById('grafico').style.display = 'block';
            } else {
                alert('Ocorreu um erro ao gerar o gráfico.');
            }
        });
});
