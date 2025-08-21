document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('zoom-modal');
    const modalImg = document.getElementById('zoom-image');
    const closeBtn = document.querySelector('.zoom-close');

    function openModal(src) {
        modalImg.src = src;
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
    }

    function closeModal() {
        modal.classList.remove('open');
        modal.setAttribute('aria-hidden', 'true');
        modalImg.src = '';
    }

    document.body.addEventListener('click', function(e) {
        const target = e.target;
        if (target.classList && target.classList.contains('zoomable')) {
            const src = target.getAttribute('data-large') || target.src;
            openModal(src);
        }
        if (target === modal) {
            closeModal();
        }
    });

    closeBtn && closeBtn.addEventListener('click', closeModal);

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('open')) {
            closeModal();
        }
    });

    // PDF snapshot rendering using PDF.js (served from CDN)
    const resumeCanvas = document.getElementById('resume-canvas');
    if (resumeCanvas && resumeCanvas.dataset.url) {
        const pdfUrl = resumeCanvas.dataset.url;
        const scriptId = 'pdfjs-lib';
        if (!document.getElementById(scriptId)) {
            const s = document.createElement('script');
            s.id = scriptId;
            s.src = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.2.67/pdf.min.js';
            s.onload = () => renderPdfSnapshot(pdfUrl, resumeCanvas);
            document.head.appendChild(s);
        } else {
            renderPdfSnapshot(pdfUrl, resumeCanvas);
        }
    }
});

async function renderPdfSnapshot(url, canvas) {
    try {
        const pdfjsLib = window['pdfjsLib'];
        if (!pdfjsLib) return;
        pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.2.67/pdf.worker.min.js';
        const loadingTask = pdfjsLib.getDocument(url);
        const pdf = await loadingTask.promise;
        const page = await pdf.getPage(1);
        const viewport = page.getViewport({ scale: 1.5 });
        const context = canvas.getContext('2d');
        canvas.width = viewport.width;
        canvas.height = viewport.height;
        await page.render({ canvasContext: context, viewport }).promise;
    } catch (e) {
        console.error('PDF snapshot error', e);
    }
}