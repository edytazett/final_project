

function searchFunction(){
    const input = document.getElementById('search_input')
    const table = document.getElementById('order_list_table')
    const tr = document.getElementsByTagName('tr')

    for (let i = 0; i < tr.length; i++) {
        const td = tr[i].getElementsByTagName('td')[0]; //index [0] odnosi sie do pierwszego td w tr - a jak wyszukiwac we wszystkich?
        if (td) {
            let txtValue = td.textContent || td.innerText;
            if (txtValue.indexOf(input) > -1) {
                tr[i].style.display = "";

            } else {
                tr[i].style.display = "none";
            }
        }

    }


}


function searchFunctionClient(){
    const input = document.getElementById('search_input')
    const table = document.getElementById('client_list_table')
    const tr = document.getElementsByTagName('tr')

    for (let i = 0; i < tr.length; i++) {
        const td = tr[i].getElementsByTagName('td')[1]; //index [0] odnosi sie do pierwszego td w tr - a jak wyszukiwac we wszystkich?
        if (td) {
            let txtValue = td.textContent || td.innerText;
            if (txtValue.indexOf(input) > -1) {
                tr[i].style.display = "";

            } else {
                tr[i].style.display = "none";
            }
        }

    }


}
