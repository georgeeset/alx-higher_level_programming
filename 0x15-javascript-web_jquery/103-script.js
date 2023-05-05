// a JavaScript script that fetches and prints how to
// say “Hello” depending on the language

$(document).ready(() => {
    function update () {
      const code = $('input#language_code').val();
      $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${code}`, (data) => {
        $('div#hello').html(data.hello);
      });
    }
    $('input#btn_translate').click(update);
    $('input#language_code').keyup((e) => {
      if (e.keyCode === 13) update();
    });
  });