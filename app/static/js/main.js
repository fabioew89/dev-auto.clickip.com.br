function selectOption(optionText, optionValue) {
    // Coloca o valor selecionado no campo oculto do formulário
    document.getElementById('selectedOption').value = optionValue;

    // Envia o formulário automaticamente
    document.getElementById('optionForm').submit();
  }


$(document).ready(function(){
  $("p").click(function(){
    $(this).hide();
  });
});  