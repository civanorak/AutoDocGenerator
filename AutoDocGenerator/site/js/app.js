// Gorgon Docs — Client-side interactivity

document.addEventListener('DOMContentLoaded', function() {
    // ─── Sidebar Search Filter ───
    const searchInput = document.getElementById('sidebar-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().trim();
            const groups = document.querySelectorAll('.sidebar-group');
            
            groups.forEach(group => {
                const links = group.querySelectorAll('.sidebar-links a');
                let hasVisible = false;
                
                links.forEach(link => {
                    const text = link.textContent.toLowerCase();
                    if (!query || text.includes(query)) {
                        link.style.display = '';
                        hasVisible = true;
                    } else {
                        link.style.display = 'none';
                    }
                });
                
                group.style.display = hasVisible ? '' : 'none';
                
                // Auto expand groups with matches
                if (query && hasVisible) {
                    group.classList.remove('collapsed');
                }
            });
        });
    }

    // ─── Sidebar Group Toggle ───
    document.querySelectorAll('.sidebar-group-title').forEach(title => {
        title.addEventListener('click', function() {
            this.parentElement.classList.toggle('collapsed');
        });
    });

    // ─── Mobile Menu Toggle ───
    const menuBtn = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    if (menuBtn && sidebar) {
        menuBtn.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });
        
        // Close sidebar on link click (mobile)
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                sidebar.classList.remove('open');
            });
        });
    }

    // ─── Highlight active sidebar link ───
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.sidebar-links a').forEach(link => {
        const href = link.getAttribute('href').split('/').pop();
        if (href === currentPage) {
            link.classList.add('active');
            // Expand parent group
            const group = link.closest('.sidebar-group');
            if (group) group.classList.remove('collapsed');
        }
    });
});
