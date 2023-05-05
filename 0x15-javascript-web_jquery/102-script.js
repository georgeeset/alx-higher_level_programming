// a JavaScript script that fetches and prints how
// to say “Hello” depending on the language

$(document).ready(() => {
    $('input#btn_translate').click(() => {
      const code = $('input#language_code').val();
      $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${code}`, (data) => {
        $('div#hello').html(data.hello);
      });
    });
  });