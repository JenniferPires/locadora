$( document ).ready(function() {
    
    $("#conteudoInicial").removeClass("invisible");
		
    $("#link_listar_filmes").click(function(){
        
			$.ajax({
					url: 'http://127.0.0.1:5000/listar_filmes',
					method: 'GET',
					dataType: 'json',
					success: listar_filmes,
					error: function() {
							alert("Erro ao ler dados. Provável problema no backend");
					}
			});

			function listar_filmes(filmes) {
					
				linhas = ""
				
				for (var i in filmes) {

					linha = `<tr>
					<td>${filmes[i].titulo}</td>
					<td>${filmes[i].data_lancamento}</td>
					<td>${filmes[i].preco}</td>
					<th><a href="#" filme_id="${filmes[i].id}">Excluir</a><th>
					</tr>`;

					linhas = linhas + linha;
				}

				$("#corpoTabelaFilmes").html(linhas);

				$("#conteudoInicial").addClass("invisible");
				$("#tabelaFilmes").addClass("invisible");

				$("#tabelaFilmes").removeClass("invisible");
				
			}

		});

		$(document).on("click", "th a", function(){

			id = $(this).attr('filme_id');

			//console.log(id);

			if (confirm("Você deseja mesmo excluir este filme?")){
				
				$.ajax({
					url: 'http://127.0.0.1:5000/excluir_filme?id='+id,
					method: 'GET',
					success: sucessoExcluirFilme,
					error: erroExcluirFilme
				});

				function sucessoExcluirFilme(resposta) {

					if (resposta.resultado == "ok") {
						
						alert("Filme excluído com sucesso!");

					} else {

							console.log(resposta['detalhes'])
							alert(resposta['detalhes']);

					}

				}
				function erroExcluirFilme() {
					alert("Erro ao excluir filme no back-end!");
				}

			}

		});
		
    $("#btn_incluir_filme").click(function(){

        titulo_filme = $("#modal_titulo").val();
        data_lancamento_filme = $("#modal_data_lancamento").val();
        preco_filme = $("#modal_preco").val();

        dados = JSON.stringify({titulo : titulo_filme, data_lancamento: data_lancamento_filme, 
            preco: preco_filme});

        $.ajax({
            url : 'http://127.0.0.1:5000/incluir_filme',
            type : 'POST',
            contentType : 'application/json',
            dataType: 'json',
            data: dados,
            success: incluirFilme,
            error: erroIncluirFilme
        });
        function incluirFilme(resposta) {

            if (resposta.resultado == "ok") {

                alert('Filme incluído com sucesso');

                $("#modal_titulo").val("");
                $("#modal_data_lancamento").val("");
                $("#modal_preco").val("");

            } else {
                console.log(resposta["resultado"])
                alert(resposta["resultado"]);

            }

        }
        function erroIncluirFilme() {

            alert("Erro ao incluir filme no back-end!");

        }
    });
    
    $("#link_inicio").click(function(){
        
        $.ajax({
            url: 'http://127.0.0.1:5000/',
            method: 'GET',
            success: function(){
                $("#corpoTabelaFilmes").html("");

                $("#conteudoInicial").addClass("invisible");
                $("#conteudoInicial").removeClass("invisible");

                $("#tabelaFilmes").removeClass("invisible");
                $("#tabelaFilmes").addClass("invisible");
            },
            error: function(erro) {
                console.log(erro)
            }
        });

		});

  });