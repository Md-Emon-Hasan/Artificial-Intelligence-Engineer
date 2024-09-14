<script>
        // Custom JavaScript for form control animations
        document.addEventListener('DOMContentLoaded', function() {
            const formControls = document.querySelectorAll('.form-control');
    
            formControls.forEach(input => {
                input.addEventListener('focus', () => {
                    input.classList.add('animated');
                });
    
                input.addEventListener('blur', () => {
                    input.classList.remove('animated');
                });
            });
        });
</script>