// Load GitHub projects and skills dynamically
const skillIcons = {
    'Python': '<i class="fab fa-python"></i>',
    'JavaScript': '<i class="fab fa-js"></i>',
    'TypeScript': '<i class="fab fa-js"></i>',
    'React': '<i class="fab fa-react"></i>',
    'Node.js': '<i class="fab fa-node"></i>',
    'HTML': '<i class="fab fa-html5"></i>',
    'CSS': '<i class="fab fa-css3-alt"></i>',
    'MongoDB': '<i class="fas fa-database"></i>',
    'PostgreSQL': '<i class="fas fa-database"></i>',
    'MySQL': '<i class="fas fa-database"></i>',
    'Docker': '<i class="fab fa-docker"></i>',
    'AWS': '<i class="fab fa-aws"></i>',
    'REST': '<i class="fas fa-network-wired"></i>',
    'API': '<i class="fas fa-plug"></i>',
    'Git': '<i class="fab fa-git"></i>',
    'Next.js': '<i class="fab fa-react"></i>',
    'Vue': '<i class="fab fa-vuejs"></i>',
    'Django': '<i class="fab fa-python"></i>',
    'Flask': '<i class="fab fa-python"></i>',
    'Machine Learning': '<i class="fas fa-brain"></i>',
    'AI': '<i class="fas fa-robot"></i>',
    'NumPy': '<i class="fab fa-python"></i>',
    'Pandas': '<i class="fab fa-python"></i>',
    'Verilog': '<i class="fas fa-microchip"></i>',
    'FPGA': '<i class="fas fa-microchip"></i>',
    'C++': '<i class="fas fa-code"></i>',
    'Java': '<i class="fab fa-java"></i>',
    'Jupyter Notebook': '<i class="fab fa-python"></i>',
};

// Initialize IntersectionObserver for animations FIRST
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Load GitHub data
async function loadGitHubData() {
    try {
        const response = await fetch('github_data.json');
        const data = await response.json();
        console.log('Data loaded:', data);
        console.log('Skills to populate:', data.skills);
        
        // Populate projects
        populateProjects(data.projects);
        
        // Populate skills from the skills array
        populateSkills(data.skills);
        
    } catch (error) {
        console.error('Error loading GitHub data:', error);
    }
}

function populateProjects(projects) {
    const projectsGrid = document.getElementById('projectsGrid');
    
    if (!projectsGrid) return;
    
    // Map of project names to image filenames
    const imageMap = {
        'Topic-Modelling-Efficacy': 'Topic Modelling Efficacy.png',
        'Society-Simulator': 'Society Simulator.png',
        'DermaConnect': 'Dermacare.png',
        'ML-Playground': 'ML Playground.jpeg',
        'Karger-Stein-K-Cut': 'Karger Stein K Cut.png',
        'DynamicTrees_NF': 'DynamicTrees_NF.png',
        'FPGA-Flappy-Bird-with-Q-Learning': 'FPGA Flappy Bird With Q Learning.png'
    };
    
    projectsGrid.innerHTML = projects.map(project => {
        const imageFileName = imageMap[project.name] || (project.name + '.png');
        const languages = project.languages.join(', ');
        return `
            <div class="project-card">
                <div class="project-image">
                    <img src="${imageFileName}" alt="${project.name}" onerror="this.style.display='none'">
                </div>
                <div class="project-info">
                    <h3>${project.name.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</h3>
                    <p>${project.description}</p>
                    <div class="project-tags">
                        ${project.languages.slice(0, 2).map(lang => `<span class="tag">${lang}</span>`).join('')}
                    </div>
                    <a href="${project.url}" target="_blank" class="view-more">View on GitHub →</a>
                </div>
            </div>
        `;
    }).join('');
    
    // Re-observe new cards for animations
    document.querySelectorAll('.project-card').forEach(el => {
        observer.observe(el);
    });
}

function populateSkills(skills) {
    const skillsGrid = document.getElementById('skillsGrid');
    
    console.log('populateSkills called with:', skills);
    console.log('skillsGrid element:', skillsGrid);
    
    if (!skillsGrid) {
        console.error('skillsGrid not found!');
        return;
    }
    
    // Get unique languages from projects
    const uniqueSkills = [...new Set(skills)].sort();
    
    console.log('Unique skills:', uniqueSkills);
    
    skillsGrid.innerHTML = uniqueSkills.map(skill => {
        const icon = skillIcons[skill] || '<i class="fas fa-code"></i>';
        return `
            <div class="skill-card">
                <div class="skill-icon">
                    ${icon}
                </div>
                <h3>${skill}</h3>
            </div>
        `;
    }).join('');
    
    // Re-observe new cards for animations
    document.querySelectorAll('.skill-card').forEach(el => {
        observer.observe(el);
    });
}

// Load data when DOM is ready
document.addEventListener('DOMContentLoaded', loadGitHubData);


if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
    });
}

// Close menu when clicking on a link
const navLinks = document.querySelectorAll('.nav-menu a');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (navMenu) {
            navMenu.style.display = 'none';
        }
    });
});

// Smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Contact Form Submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Show success message
        alert('Thank you for your message! I\'ll get back to you soon.');
        contactForm.reset();
    });
}

// Navbar scroll effect
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (navbar) {
        if (scrollTop > 50) {
            navbar.style.borderBottomColor = 'rgba(0, 212, 255, 0.2)';
        } else {
            navbar.style.borderBottomColor = 'rgba(255, 255, 255, 0.1)';
        }
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});

// Active navigation link on scroll
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.scrollY + 100;
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');
        
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
            });
            
            const activeLink = document.querySelector(`.nav-menu a[href="#${sectionId}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
        }
    });
});

// Add active class styling to CSS
const style = document.createElement('style');
style.textContent = `
    .nav-menu a.active {
        color: var(--accent-color);
        border-bottom: 2px solid var(--accent-color);
        padding-bottom: 5px;
    }
`;
document.head.appendChild(style);

// Parallax effect on hero section
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    if (hero) {
        const scrollTop = window.pageYOffset;
        hero.style.transform = `translateY(${scrollTop * 0.5}px)`;
    }
});

// Form input validation
const inputs = document.querySelectorAll('.form-group input, .form-group textarea');
inputs.forEach(input => {
    input.addEventListener('blur', () => {
        if (input.type === 'email' && input.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value)) {
                input.style.borderColor = '#ff6b6b';
            } else {
                input.style.borderColor = 'rgba(255, 255, 255, 0.1)';
            }
        } else if (input.value.trim() === '') {
            input.style.borderColor = '#ff6b6b';
        } else {
            input.style.borderColor = 'rgba(255, 255, 255, 0.1)';
        }
    });
});

// View All Projects click
const viewAllBtn = document.querySelector('.section-subtitle');
if (viewAllBtn) {
    viewAllBtn.addEventListener('click', () => {
        const projectCards = document.querySelectorAll('.project-card');
        projectCards.forEach(card => {
            card.style.display = card.style.display === 'none' ? 'block' : 'none';
        });
        viewAllBtn.textContent = viewAllBtn.textContent === 'View All' ? 'Hide' : 'View All';
    });
}
