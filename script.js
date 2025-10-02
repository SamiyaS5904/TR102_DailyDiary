// ======================================================================
// TR-102 INDUSTRIAL TRAINING DIARY - COMPLETE JAVASCRIPT
// ======================================================================

document.addEventListener('DOMContentLoaded', function() {
    // Define main scrolling area (ID must match your HTML: <div id="content">)
    const contentArea = document.getElementById('content');
    
    // Core Initializations
    initThemeToggle();
    initSidebarCollapsible(); // Handles the new collapsible sidebar logic
    initSidebarNavigation(contentArea); 
    initBackToTopButton(contentArea); 
    
    // UI Effects (Keeping features from your original code that enhance UI)
    initAnimations(contentArea);
    initSkillBars(contentArea); 
});

// ----------------------------------------------------------------------
// 1. THEME TOGGLE
// ----------------------------------------------------------------------

function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    
    // Check for saved theme preference or default to 'light'
    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        body.classList.add('dark-theme');
    }
    
    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-theme');
        
        const newTheme = body.classList.contains('dark-theme') ? 'dark' : 'light';
        localStorage.setItem('theme', newTheme);
        
        // Brief transition reset for smooth color change
        body.style.transition = 'all 0.3s ease';
        setTimeout(() => {
            body.style.transition = '';
        }, 300);
    });
}

// ----------------------------------------------------------------------
// 2. SIDEBAR COLLAPSIBLE LOGIC (NEW REQUEST)
// ----------------------------------------------------------------------

function initSidebarCollapsible() {
    const sidebar = document.getElementById('sidebar');
    const toggleButton = document.getElementById('sidebar-toggle-btn');
    
    // The sidebar starts collapsed by default via CSS class (sidebar-collapsed)
    
    toggleButton.addEventListener('click', function() {
        sidebar.classList.toggle('sidebar-collapsed');
    });
}


// ----------------------------------------------------------------------
// 3. SIDEBAR NAVIGATION & ACTIVE LINK TRACKING
// ----------------------------------------------------------------------

function initSidebarNavigation(contentArea) {
    const sidebarLinks = document.querySelectorAll('.sidebar-menu a');
    const sections = document.querySelectorAll('.section');
    
    // Smooth Scrolling for Sidebar links
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const targetScrollTop = targetElement.offsetTop - 30; // 30px buffer
                contentArea.scrollTo({
                    top: targetScrollTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Update Active Sidebar Link based on content scroll position
    contentArea.addEventListener('scroll', updateActiveNavLink);

    function updateActiveNavLink() {
        const scrollPosition = contentArea.scrollTop;
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop - 50;
            
            if (scrollPosition >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        
        sidebarLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }

    // Set the initial active link on load
    updateActiveNavLink();
}

// ----------------------------------------------------------------------
// 4. BACK TO TOP BUTTON (CHATGPT/GEMINI STYLE)
// ----------------------------------------------------------------------

function initBackToTopButton(contentArea) {
    const backToTopButton = document.getElementById('back-to-top');
    
    // Hide/Show the button based on scroll position in the content area
    contentArea.addEventListener('scroll', function() {
        if (contentArea.scrollTop > 300) {
             backToTopButton.style.opacity = 1;
             backToTopButton.style.visibility = 'visible';
        } else {
             backToTopButton.style.opacity = 0;
             backToTopButton.style.visibility = 'hidden';
        }
    });

    backToTopButton.addEventListener('click', function(e) {
        e.preventDefault();
        contentArea.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Set initial state (hidden)
    backToTopButton.style.opacity = 0;
    backToTopButton.style.visibility = 'hidden';
}

// ----------------------------------------------------------------------
// 5. UI ENHANCEMENTS (Animations/Skill Bars)
// ----------------------------------------------------------------------

// Animation on Scroll (using Intersection Observer on the #content area)
function initAnimations(contentArea) {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px',
        root: contentArea 
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);
    
    const animateElements = document.querySelectorAll(
        '.week-card-formal, .project-card-formal, .timeline-item, .highlight-item, .formal-mentor-card, .skill-card-formal'
    );
    
    animateElements.forEach(el => {
        observer.observe(el);
    });
}

// Skill Bar Animations (Triggered by Intersection Observer on the #content area)
function initSkillBars(contentArea) {
    // Note: Since we are not using progress bars, this function is mostly a placeholder 
    // but retained for structure if you add progress bars later.
    const skillCards = document.querySelectorAll('.skill-card'); 
    
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target.querySelector('.progress-bar');
                if (progressBar) { 
                    const progress = progressBar.getAttribute('data-progress');
                    setTimeout(() => {
                        progressBar.style.width = progress + '%';
                        progressBar.style.transition = 'width 1s ease-in-out';
                    }, 300);
                }
                skillObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.3,
        root: contentArea
    });
    
    skillCards.forEach(card => {
        skillObserver.observe(card);
    });
}