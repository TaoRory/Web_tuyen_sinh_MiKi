$(document).ready(function () {

    const btnLoginPage = document.querySelector('.btn_login_page')
    const SBD = document.getElementById('sbd')
    const MHS = document.getElementById('mhs')
    btnLoginPage.addEventListener('click', async function (e) {
        e.preventDefault()
        console.log(SBD.value)
        console.log(MHS.value)

        const checkStudent = await $.ajax(
            {
                url: '/check-student',
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                data: JSON.stringify({
                    jsonrpc: "2.0",
                    params: {
                        'sbd': SBD.value,
                        'mhs': MHS.value
                    },
                }),
            }
        )

        console.log(checkStudent)

        if (!checkStudent.result.error)
        {

            document.querySelector('.info-box').style.display = 'block'
            document.querySelector('#result_name').innerHTML = checkStudent.result.student_name
            document.querySelector('#result_dob').innerHTML = checkStudent.result.day_of_birth
            btnLoginPage.style.display='none'
        }

    })
})