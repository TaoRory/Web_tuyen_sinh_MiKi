function updateDistricts(a) {
    const citySelect = document.getElementById(a + '_province_id');
    const wardSelect = document.getElementById(a + '_ward_id');
    const districtSelect = document.getElementById(a + '_district_id');

    const selectedCity = citySelect.value;

    // Clear existing options
    wardSelect.innerHTML = '<option value="">Select Ward</option>';
    districtSelect.innerHTML = '<option value="">Select District</option>';

    if (selectedCity) {
        const data = $.ajax(
            {
                url: '/district',
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                data: JSON.stringify({
                    jsonrpc: "2.0",
                    params: {
                        'province_id': selectedCity,
                    },
                }),
            }
        ).then(data => {
            console.log(data)
            data.result.districts.forEach(district => {
                const option = document.createElement('option');
                option.value = district.id;
                option.textContent = district.name;
                districtSelect.appendChild(option);
            });
        })
    }
}

function updateWards(a) {
    const wardSelect = document.getElementById(a + '_ward_id');
    const districtSelect = document.getElementById(a + '_district_id');

    const selectedDistrict = districtSelect.value;

    // Clear existing options
    wardSelect.innerHTML = '<option value="">Select Ward</option>';

    if (selectedDistrict) {
        const data = $.ajax(
            {
                url: '/ward',
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                data: JSON.stringify({
                    jsonrpc: "2.0",
                    params: {
                        'district_id': selectedDistrict,
                    },
                }),
            }
        ).then(data => {
            console.log(data)
            data.result.wards.forEach(ward => {
                const option = document.createElement('option');
                option.value = ward.id;
                option.textContent = ward.name;
                wardSelect.appendChild(option);
            });
        })
    }
}


$('document').ready(function() {
    // updateDistricts('permanent');
    //
    // updateWards('permanent');
})