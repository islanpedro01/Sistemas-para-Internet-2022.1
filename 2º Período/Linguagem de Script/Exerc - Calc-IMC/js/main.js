const sexo = document.querySelector('#masculino')
const peso = document.querySelector('#peso')
const altura = document.querySelector('#altura')
const IMCresult = document.querySelector('#IMCresult')
const error = document.querySelector('#warning')
const button = document.querySelector('#calc-imc-btn')

function calc(alt,peso,sexo){
    let IMC = peso/(alt*alt)
    let result; 
    const IMCresult = document.querySelector('#IMCresult')    

    if ((!sexo &&  IMC < 19.1) || (sexo && IMC < 20.7)){
        result = "Abaixo do Peso"
        IMCresult.className = "form-control form-control-lg border border-warning bg-warning text-white"

        return result;
    }
    else if ((!sexo && (IMC >= 19.1 && IMC < 25.8)) || (sexo && (IMC >= 20.7 && IMC < 26.4))){
        result = "Peso Normal"
        IMCresult.className = "form-control form-control-lg border border-sucess bg-success text-white"

        return result;
    }
    else if ((!sexo && (IMC >= 25.8 && IMC < 27.3)) || (sexo && (IMC >= 26.4 && IMC < 27.8))){
        result = "Marginalmente Acima do Peso"
        IMCresult.className = "form-control form-control-lg border border-warning bg-warning text-white"
        
        return result;
    }
    else if ((!sexo && (IMC >= 27.3 && IMC < 32.3)) || (sexo && (IMC >= 27.8 && IMC < 31.1))){
        result = "Acima do Peso Ideal"
        IMCresult.className = "form-control form-control-lg border border-warning bg-warning text-white"        
        
        return result;
    }
    else if ((!sexo && IMC >= 32.3) || (sexo && IMC >= 31.1)){
        result = "Obeso"
        IMCresult.className = "form-control form-control-lg border border-danger bg-danger text-white"
        
        return result;
    }
    else{
        return false;
    }
    
}

button.addEventListener('click', function(e){ 
     let sexoCalc = sexo.checked
     let pesoNum = Number(peso.value)
     let alturaNum = Number(altura.value)

    if ((!calc(alturaNum, pesoNum, sexoCalc))||(pesoNum*alturaNum == 0)){
       error.classList.remove("d-none")
       IMCresult.className = "form-control form-control-lg"
       IMCresult.value = ''
      }
    else{
        IMCresult.value = calc(alturaNum, pesoNum, sexoCalc)
        error.classList.add("d-none")
        
    }
});

document.addEventListener('keyup', function(e){
    let entradas = document.querySelectorAll('input[type=text]')

    if (e.code === 'Enter'){
        button.click()
    }
    else if (e.code === 'Escape'){
        entradas.forEach(entry => entry.value = '') 
        IMCresult.className = "form-control form-control-lg"
    }
})
