function calc(alt,peso,sexo){

    let IMC = peso/(alt*alt)
    let result; 
    const IMCresult = document.querySelector('#IMCresult')
    IMCresult.classList.add("border","text-white")    
    

    if ((!sexo &&  IMC < 19.1) || (sexo && IMC < 20.7)){
        result = "Abaixo do Peso"
        IMCresult.classList.remove("border-sucess","bg-sucess","border-danger","bg-danger")
        IMCresult.classList.add("border-warning","bg-warning")
        return result;

    }
    else if ((!sexo && (IMC >= 19.1 && IMC < 25.8)) || (sexo && (IMC >= 20.7 && IMC < 26.4))){
        result = "Peso Normal"
        IMCresult.classList.remove("border-warning","bg-warning","border-danger","bg-danger")
        IMCresult.classList.add("border-sucess", "bg-success")
        return result;
    }
    else if ((!sexo && (IMC >= 25.8 && IMC < 27.3)) || (sexo && (IMC >= 26.4 && IMC < 27.8))){
        result = "Marginalmente Acima do Peso"
        IMCresult.classList.remove("border-warning","bg-warning","border-danger","bg-danger") 
        IMCresult.classList.add("border-sucess", "bg-success")     
        return result;
    }
    else if ((!sexo && (IMC >= 27.3 && IMC < 32.3)) || (sexo && (IMC >= 27.8 && IMC < 31.1))){
        result = "Acima do Peso Ideal"
        IMCresult.classList.remove("border-sucess","bg-sucess","border-danger","bg-danger")
        IMCresult.classList.add("border-warning","bg-warning")
        return result;
    }
    else if ((!sexo && IMC >= 32.3) || (sexo && IMC >= 31.1)){
        result = "Obeso"
        IMCresult.classList.remove("border-sucess","bg-sucess","border-warning","bg-warning")
        IMCresult.classList.add("border-danger", "bg-danger")
        return result;
    }
    else{
        return false;
    }
    
}

const button = document.querySelector('#calc-imc-btn')

button.onclick = () =>{
    
    const sexo = document.querySelector('#masculino').checked
    const peso = Number(document.querySelector('#peso').value)
    const altura = Number(document.querySelector('#altura').value)
    const IMCresult = document.querySelector('#IMCresult')
    let error = document.querySelector('#warning')

    if ((!calc(altura, peso, sexo))||(peso*altura == 0)){
       error.classList.remove("d-none")
       IMCresult.classList.remove("border","border-warning","bg-warning","text-white","border-sucess","bg-success","border-danger","bg-danger")
       IMCresult.value = ''
      }
    else{
        IMCresult.value = calc(altura, peso, sexo)
        error.classList.add("d-none")
    }
}

document.addEventListener('keyup', function(e){

let entradas = document.querySelectorAll('input[type=text]')

    if (e.code === 'Enter'){
        button.click()
    }
    else if (e.code === 'Escape'){
        entradas.forEach(entry => entry.value = '') 
        IMCresult.classList.remove("border","border-warning","bg-warning","text-white","border-sucess","bg-success","border-danger","bg-danger")
    }
})
