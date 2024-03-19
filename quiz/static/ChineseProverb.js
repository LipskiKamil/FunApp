        document.addEventListener('DOMContentLoaded', function () {
            fetchProverb();
        });

        function fetchProverb() {
            $.ajax({
                type: 'GET',
                url: '/DailyChineseProverb/',
                headers: {'X-Requested-With': 'XMLHttpRequest'},
                success: function (data) {
                    var proverbText = data.random_proverb;
                    displayProverb(proverbText);
                },
                error: function () {
                    console.error('Failed to fetch Chinese proverb.');
                }
            });
        }
function displayProverb(proverbText) {
    var proverbContainer = $('#proverb-container');
    var proverbTextElement = $('#proverb-text');

    // Ukrywamy kontener z przysłowiem
    proverbContainer.hide();

    // Ustawiamy tekst przysłowia
    proverbTextElement.text(proverbText);

    // Animacja pojawiania się tekstu
    proverbContainer.fadeIn(550); // 1000ms = 1 sekunda
}

        function goToHomePage() {
            window.location.href = '/';
        }