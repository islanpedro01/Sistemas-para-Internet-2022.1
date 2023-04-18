// TODO
const form = document.querySelector('form')

form.onsubmit = (event) => {
    event.preventDefault();

    const num = Number(document.querySelector('.quantity').value)
    const numplace = document.querySelector('.list');
    let result = '';

   for (let i = 0; i < num; i++) {
        result += `<li>Item ${i+1}</li>`
    }
    numplace.innerHTML = result;
};