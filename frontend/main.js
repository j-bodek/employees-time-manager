table_cell = document.querySelectorAll('.editable_cell')
let inputs = false

table_cell.forEach(element => {
    element.addEventListener('click', (e) => {


        if (element.innerHTML == '1' || element.innerHTML == '0') {
            element.classList.toggle("active_cell");
            element.innerHTML = element.innerHTML == 0 ? 1 : 0

        }


        if (element.innerHTML != '1' && element.innerHTML != '0' && element.getElementsByTagName('input').length == 0) {
            let input = document.createElement('input')
            input.setAttribute('type', 'text')
            input.setAttribute('value', element.innerHTML)

            element.innerHTML = ''

            element.appendChild(input);
            input.focus()
            input_focusout()
        }
    })
});


let input_focusout = function () {
    document.querySelectorAll('input').forEach(input => {
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                input.parentNode.innerHTML = input.value
            }
        })
        input.addEventListener('focusout', (e) => {
            input.parentNode.innerHTML = input.value
        })
    })
}