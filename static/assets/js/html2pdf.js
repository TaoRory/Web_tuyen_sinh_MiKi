function downloadPDF() {
    var element = document.querySelector('#pdf-content');
    var opt = {
        margin: [0, 0, 0, 0],
        filename: 'two_pages.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
        pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }
    };

    // Wait for images to load
    Promise.all(Array.from(element.querySelectorAll('img')).map(img => {
        if (img.complete) {
            return Promise.resolve();
        }
        return new Promise(resolve => {
            img.onload = img.onerror = resolve;
        });
    })).then(() => {
        html2pdf().from(element).set(opt).save();
    });
}