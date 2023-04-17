function calc(alt,peso,sexo){

    let IMC = peso/(alt*alt)
    let result;
    const IMCresult = document.querySelector('#IMCresult')
    
    if ((!sexo &&  IMC < 19.1) || (sexo && IMC < 20.7)){
        result = "Abaixo do Peso"
        IMCresult.classList.add("border","border-warning","bg-warning","text-white")
        return result;

    }
    else if ((!sexo && (IMC >= 19.1 && IMC < 25.8)) || (sexo && (IMC >= 20.7 && IMC < 26.4))){
        result = "Peso Normal"
        IMCresult.classList.add("border", "border-sucess", "bg-success", "text-white")
        return result;
    }
    else if ((!sexo && (IMC >= 25.8 && IMC < 27.3)) || (sexo && (IMC >= 26.4 && IMC < 27.8))){
        result = "Marginalmente Acima do Peso"
        IMCresult.classList.add("border", "border-sucess", "bg-success", "text-white")
        return result;
    }
    else if ((!sexo && (IMC >= 27.3 && IMC < 32.3)) || (sexo && (IMC >= 27.8 && IMC < 31.1))){
        result = "Acima do Peso Ideal"
        IMCresult.classList.add("border","border-warning","bg-warning","text-white")

        return result;
    }
    else if ((!sexo && IMC >= 32.3) || (sexo && IMC >= 31.1)){
        result = "Obeso"
        IMCresult.classList.add("border", "border-danger", "bg-danger", "text-white")
        return result;
    }
    
}

const button = document.querySelector('#calc-imc-btn')

button.onclick = () =>{
    
    const sexo = document.querySelector('#masculino').checked
    const peso = Number(document.querySelector('#peso').value)
    const altura = Number(document.querySelector('#altura').value)
    const IMCresult = document.querySelector('#IMCresult')
    if (peso == 0 || altura == 0){
      IMCresult.value = 'Preencha os campos de Altura e Peso!'
    }
    else {
        IMCresult.value = calc(altura, peso, sexo)
    }

}

document.addEventListener('keyup', function(e){


    if (e.code === 'Enter'){
        button.click()
    }
    else if (e.code === 'Escape'){
        peso.value = ''
        altura.value = ''
        IMCresult.value = ''
    }
})