document.addEventListener('DOMContentLoaded', function () {

    const selectVariacao =
        document.getElementById('select-variacoes');

    const preco =
        document.getElementById('variation-preco');

    const precoPromocional =
        document.getElementById('variation-preco-promocional');

    if (!selectVariacao) return;

    selectVariacao.addEventListener('change', function () {

        const option =
            this.options[this.selectedIndex];

        const novoPreco =
            option.dataset.preco;

        const novoPrecoPromocional =
            option.dataset.precoPromocional;

        // tem promoção
        if (novoPrecoPromocional &&
            novoPrecoPromocional !== 'None') {

            if (precoPromocional) {
                precoPromocional.innerHTML =
                    novoPrecoPromocional;
            }

            if (preco) {
                preco.innerHTML = novoPreco;
            }

        } else {

            // sem promoção
            if (preco) {
                preco.innerHTML = novoPreco;
            }

            if (precoPromocional) {
                precoPromocional.innerHTML = '';
            }
        }

    });

});