add_employee_btn = document.querySelector('.add_employee')
let inputs = false

let add_cell_actions = function () {
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


    delete_row_btn.forEach(btn => {
        btn.addEventListener('click', (e) => {
            row = btn.closest('tr')
            row.remove()
        })
    })

}



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


add_employee_btn.addEventListener('click', (e) => {
    document.querySelector('.employees_table').innerHTML += `
    <tr>
    <td class='editable_cell'>Stanowisko</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='editable_cell'>0</td>
    <td class='delete_row'><button class='delete_row_btn'>Usuń</button></td>
  </tr>
    `


    table_cell = document.querySelectorAll('.editable_cell')
    delete_row_btn = document.querySelectorAll('.delete_row_btn')
    add_cell_actions()
})