$(document).ready(function () {
    var student_type_btn = document.querySelectorAll('.radio-student-type')
    student_type_btn.forEach(function (radioInput) {
        radioInput.addEventListener('change', function () {
            if (this.checked) {
                const departmentDiv = document.getElementsByClassName('department ' + this.value);
                if (departmentDiv.length > 0) {
                    // set hidden all
                    const departmentDivAll = document.getElementsByClassName('department');
                    for (let i = 0; i < departmentDivAll.length; i++) {
                        const departmentDiv1 = departmentDivAll[i];

                        departmentDiv1.setAttribute('hidden', 'hidden');
                        // Perform any custom logic here for each departmentDiv
                    }

                    // remove hidden
                    for (let i = 0; i < departmentDiv.length; i++) {
                        const departmentDiv1 = departmentDiv[i];

                        departmentDiv1.removeAttribute('hidden');
                        // Perform any custom logic here for each departmentDiv
                    }

                    const radioMajorAll = document.getElementsByClassName('radio-major');
                    for (let i = 0; i < radioMajorAll.length; i++) {
                        const radioMajor1 = radioMajorAll[i];

                        radioMajor1.removeAttribute('checked');
                        // Perform any custom logic here for each departmentDiv
                    }
                    // Perform any custom logic here
                }
                // Add your custom logic here
            }
        });
    });

})