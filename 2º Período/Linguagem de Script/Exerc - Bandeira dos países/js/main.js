import flags from '/js/flags.js';

function bandeiras(flags){
    return `<div class="flag col-2 my-2 text-center">
    <img src=${flags.image} alt=>
    <p>${flags.name}</p>
  </div>`;
}
const bandeirasGrid = document.querySelector('.row');
bandeirasGrid.innerHTML = flags
  .map((flag) => bandeiras(flag))
  .join('');