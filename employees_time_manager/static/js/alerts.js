document.querySelectorAll('.close_message').forEach(close_btn => {
    close_btn.addEventListener('click', e => {
        let message_box = close_btn.parentNode
        message_box.remove()
    })
})