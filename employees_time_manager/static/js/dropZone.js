dragHandlere = function (event) {
    event.preventDefault()
}

dropHandler = function (event) {
    event.preventDefault()
    // upload droped data to input
    let uploaded_file_name = event.dataTransfer.files[0]['name']
    if (uploaded_file_name.split('.').pop() == 'csv') {
        document.getElementById('upload_file').files = event.dataTransfer.files
        // display uploaded file name
        document.querySelector('.uploaded_file').innerHTML = uploaded_file_name
    }
}

uploadFile = function (event) {
    let uploaded_file_name = event.target.files[0]['name'];
    document.querySelector('.uploaded_file').innerHTML = uploaded_file_name
};

document.querySelector('.drop_file').addEventListener('click', (e) => {
    if (event.target.id !== 'choose_file') {
        e.preventDefault()
    }
})