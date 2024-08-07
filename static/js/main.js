////////////////////
// МОДАЛЬНЫЕ ОКНА //
////////////////////

let open_modal_btns = document.querySelectorAll('.btn_open-modal')

for (let open_modal_btn of open_modal_btns) {
    open_modal_btn.addEventListener('click', function() {
        let modal = document.querySelector(`#${this.dataset.target}`)
        open_modal(modal)
    })
}


document.addEventListener('click', async function(e) {
    console.log(e.target)
   if (e.target.classList.contains('btn_close-modal')) {
        
        //////////////////////////////
        // ЗАКРЫТИЕ МОДАЛЬНОГО ОКНА //
        //////////////////////////////

        close_modal(document.querySelector(`#${e.target.dataset.target}`))
    } else if (e.target.classList.contains('modal__overlay')) {
        
        ////////////////////////////////////////////////////
        // ЗАКРЫТИЕ МОДАЛЬНОГО ОКНА, НАЖАТИЕМ НА ОВЕРЛЕЙ  //
        ////////////////////////////////////////////////////

        let modal = e.target.closest('.modal')
        close_modal(modal)
    } else if (e.target.classList.contains('tabs-switcher__btn')) {
        
        ///////////////////////////////////////////
        // ПЕРЕКЛЮЧЕНИЕ РАЗДЕЛОВ МОДАЛЬНОГО ОКНА //
        ///////////////////////////////////////////

        let current_switcher = e.target.closest('.tabs-switcher__item')
        current_switcher.classList.toggle('tabs-switcher__item_hidden')
        if (e.target.classList.contains('tabs-switcher__btn_open')) {
            var back_switcher = current_switcher.nextElementSibling
        } else if (e.target.classList.contains('tabs-switcher__btn_close')) {
            var back_switcher = current_switcher.previousElementSibling
        }
        
        back_switcher.classList.toggle('tabs-switcher__item_hidden')

        let open_tab = document.querySelector(`#${e.target.dataset.open}`)
        
        change_tabs(open_tab)
    } else if (e.target.classList.contains('task__link')) {

        //////////
        // AJAX //
        //////////

        e.preventDefault()

        let url = e.target.getAttribute('href')
        
        let response = await fetch(url)

        if (response.ok) {
            let json_data = await response.json()

            let container = document.querySelector('.main')
            let modal = document.querySelector(`#read_task`)
            if (container.contains(modal)) {
                modal.remove()
                modal = document.querySelector(`#read_task`)
            } 
            container.insertAdjacentHTML('beforeend', json_data['html'])
            modal = document.querySelector(`#read_task`)
            open_modal(modal)
            
        }
    }
})


document.addEventListener('keyup', function(e) {
    if (e.key == 'Escape') {
        let modals = document.querySelectorAll('.modal')
        for (const modal of modals) {
            close_modal(modal)
        }
    }
})

function open_modal(target) {
    target.style.display = 'block'
    let tab_to_open = target.querySelector('.tab')

    change_tabs(tab_to_open)

    let tab_switchers = target.querySelectorAll('.tabs-switcher__item')

    for (const tab_switcher of tab_switchers) {
        tab_switcher.classList.add('tabs-switcher__item_hidden')
    }

    tab_switchers[0].classList.remove('tabs-switcher__item_hidden')
}

function close_modal(target) {
    target.style.display = 'none'
}

///////////////////////////
// ФУНКЦИЯ СМЕНЫ ВКЛАДОК //
///////////////////////////

function change_tabs(tab_to_open) {   
    var tabs = document.querySelectorAll('.tab')

    for (const tab of tabs) {
        tab.classList.remove('active')
    }

    tab_to_open.classList.add('active')

}

////////////////////////
// СВОРАЧИВАНИЕ ЯЧЕЕК //
////////////////////////


let cell_btns = document.querySelectorAll('.cell__btn')

for (let cell_btn of cell_btns) {
    cell_btn.addEventListener('click', function() {
        // hide_or_open_cell_body()
        this.classList.toggle('cell__btn_rotated')
        let cell_body = this.closest('.cell__header').nextElementSibling
        cell_body.classList.toggle('cell__body_hidden')
    }
    
    )
}

function hide_or_open_cell_body(e) {
    let cell_body = e.closest('.cell__body')

    cell_body.classList.toggle('.cell__body_hidden')
}

///////////////////
// ОТКРЫТИЕ МЕНЮ //
///////////////////

function open_menu(target) {
    if (target.classList.contains('navigation_hidden')) {
        target.classList.replace('navigation_hidden', 'navigation_active')
    } else {
        target.classList.add('navigation_active')
    }
}

function close_menu(target) {
    target.classList.replace('navigation_active', 'navigation_hidden')
}

let menu_btns = document.querySelectorAll('.btn_menu')

for (const menu_btn of menu_btns) {
    menu_btn.addEventListener('click', function(e) {

        let menu = document.querySelector('.navigation')

        if (menu.classList.contains('navigation_active')) {
            close_menu(menu)
        } else {
            open_menu(menu)
        }
    })
}

let navigation_overlay = document.querySelector('.navigation__overlay')

navigation_overlay.addEventListener('click', function() {
    let menu = this.closest('.navigation')

    close_menu(menu)
})
