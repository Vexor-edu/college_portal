document.addEventListener("DOMContentLoaded", function () {
    // Look for a success flag in the URL
    const urlParams = new URLSearchParams(window.location.search);
    const submitted = urlParams.get("submitted");

    if (submitted === "true") {
        Swal.fire({
            title: '🎉 Application Submitted!',
            text: 'Thank you for applying. We will contact you shortly.',
            icon: 'success',
            confirmButtonColor: '#3b82f6'
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    console.log("Page loaded. JS active!");
});
