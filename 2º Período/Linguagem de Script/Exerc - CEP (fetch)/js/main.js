const cepfield = document.querySelector('#cep')
const rua = document.querySelector('#street')
const bairro = document.querySelector('#neighborhood')
const estado = document.querySelector('#state')
const cidade = document.querySelector('#city')
const erro = document.querySelector('#cepError')
let temporizador

async function getCEP(cep) {
  if (cepfield.value!==''){
    try {
      const url = `https://viacep.com.br/ws/${cep}/json/`;
      const response = await fetch(url);
      const cepData = await response.json();
      if (cepData.erro){
        erro.classList.remove('hidden')
      }
      rua.value = cepData.logradouro
      bairro.value = cepData.bairro
      estado.value = cepData.uf
      cidade.value = cepData.localidade
      erro.className ='hidden'    

    } catch (error){
      erro.classList.remove('hidden') 
      clear();
      
    } 
  } 
  else{
    erro.className ='hidden'
    clear();
  }
}

function clear(){
  rua.value = ''
  bairro.value = ''
  estado.value = ''
  cidade.value = '' 
}




  cepfield.addEventListener('input', function(){
   clearTimeout(temporizador);
   temporizador = setTimeout(()=>getCEP(cepfield.value),500);
  //  Versão com onblur:
  // cepfield.onblur = function(){getCEP(cepfield.value)}
  })
  