import requests
import json
import re
from pathlib import Path

# GitHub configuration
GITHUB_USERNAME = "rameezw16"
GITHUB_API_URL = "https://api.github.com"

def fetch_user_repos():
    """Fetch all repositories for the user"""
    url = f"{GITHUB_API_URL}/users/{GITHUB_USERNAME}/repos"
    params = {
        'sort': 'updated',
        'per_page': 100,
        'type': 'owner'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        repos = response.json()
        print(f"✓ Found {len(repos)} repositories")
        return repos
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching repositories: {e}")
        return []

def fetch_readme(repo_name):
    """Fetch README content for a repository"""
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{repo_name}/readme"
    headers = {'Accept': 'application/vnd.github.v3.raw'}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None

def extract_description_from_readme(readme_content):
    """Extract a brief description from README"""
    if not readme_content:
        return "Project repository"
    
    # Remove markdown formatting and get first non-empty line
    lines = readme_content.split('\n')
    for line in lines:
        # Skip headers and empty lines
        if line.strip() and not line.startswith('#'):
            # Remove markdown formatting
            description = line.strip()
            # Remove markdown links
            description = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', description)
            # Remove markdown bold/italic
            description = re.sub(r'[*_`]', '', description)
            # Truncate to reasonable length
            if len(description) > 150:
                description = description[:150] + "..."
            return description
    
    return "Project repository"

def extract_languages(repo_data):
    """Extract programming languages from repo"""
    languages = []
    if repo_data.get('language'):
        languages.append(repo_data['language'])
    return languages

def extract_skills_from_readme(readme_content):
    """Extract technologies/skills mentioned in README"""
    skills = set()
    
    if not readme_content:
        return []
    
    readme_lower = readme_content.lower()
    
    # Common tech keywords to look for
    tech_keywords = {
        'python': 'Python',
        'javascript': 'JavaScript',
        'typescript': 'TypeScript',
        'react': 'React',
        'vue': 'Vue',
        'angular': 'Angular',
        'node': 'Node.js',
        'nodejs': 'Node.js',
        'express': 'Express',
        'django': 'Django',
        'flask': 'Flask',
        'fastapi': 'FastAPI',
        'html': 'HTML',
        'css': 'CSS',
        'scss': 'SCSS',
        'sass': 'Sass',
        'tailwind': 'Tailwind',
        'bootstrap': 'Bootstrap',
        'mongodb': 'MongoDB',
        'postgres': 'PostgreSQL',
        'mysql': 'MySQL',
        'sql': 'SQL',
        'firebase': 'Firebase',
        'aws': 'AWS',
        'docker': 'Docker',
        'kubernetes': 'Kubernetes',
        'git': 'Git',
        'api': 'API',
        'rest': 'REST',
        'graphql': 'GraphQL',
        'nextjs': 'Next.js',
        'next.js': 'Next.js',
        'webpack': 'Webpack',
        'vite': 'Vite',
        'jest': 'Jest',
        'testing': 'Testing',
        'selenium': 'Selenium',
        'beautifulsoup': 'BeautifulSoup',
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'tensorflow': 'TensorFlow',
        'pytorch': 'PyTorch',
        'machine learning': 'Machine Learning',
        'ai': 'AI',
        'nlp': 'NLP',
        'web design': 'Web Design',
        'ui/ux': 'UI/UX',
        'figma': 'Figma',
    }
    
    for keyword, skill_name in tech_keywords.items():
        if keyword in readme_lower:
            skills.add(skill_name)
    
    return list(skills)

def create_project_data(repos):
    """Create project data from repositories"""
    projects = []
    all_skills = set()
    
    for repo in repos:  # Get ALL repositories including forks
        # Include all repositories
            
        print(f"Processing: {repo['name']}")
        
        readme = fetch_readme(repo['name'])
        description = extract_description_from_readme(readme)
        languages = extract_languages(repo)
        skills = extract_skills_from_readme(readme)
        
        project = {
            'name': repo['name'],
            'description': description,
            'url': repo['html_url'],
            'languages': languages,
            'skills': skills,
            'stars': repo['stargazers_count'],
            'updated': repo['updated_at'],
            'topics': repo.get('topics', [])
        }
        
        projects.append(project)
        all_skills.update(skills)
    
    return projects, list(all_skills)

def generate_html_projects(projects):
    """Generate HTML for project cards"""
    html = ""
    for project in projects:
        languages = ", ".join(project['languages']) if project['languages'] else "Repository"
        html += f"""
            <div class="project-card">
                <div class="project-image">
                    <div class="project-placeholder">
                        <i class="fab fa-github"></i>
                    </div>
                </div>
                <div class="project-info">
                    <h3>{project['name'].replace('-', ' ').title()}</h3>
                    <p>{project['description']}</p>
                    <div class="project-tags">
                        {' '.join([f'<span class="tag">{lang}</span>' for lang in project['languages'][:2]])}
                    </div>
                    <a href="{project['url']}" target="_blank" class="view-more">View on GitHub →</a>
                </div>
            </div>
"""
    return html

def generate_skill_cards(skills):
    """Generate HTML for skill cards"""
    skill_info = {
        'Python': '<i class="fab fa-python"></i>',
        'JavaScript': '<i class="fab fa-js"></i>',
        'TypeScript': '<i class="fab fa-js"></i>',
        'React': '<i class="fab fa-react"></i>',
        'Node.js': '<i class="fab fa-node"></i>',
        'HTML': '<i class="fab fa-html5"></i>',
        'CSS': '<i class="fab fa-css3-alt"></i>',
        'MongoDB': '<i class="fas fa-database"></i>',
        'PostgreSQL': '<i class="fas fa-database"></i>',
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
    }
    
    html = ""
    for skill in sorted(set(skills))[:9]:  # Limit to 9 skills
        icon = skill_info.get(skill, '<i class="fas fa-code"></i>')
        description = f"Expertise in {skill}"
        html += f"""
            <div class="skill-card">
                <div class="skill-icon">
                    {icon}
                </div>
                <h3>{skill}</h3>
                <p>{description}</p>
            </div>
"""
    return html

def main():
    print(f"\n🔍 Fetching repositories for {GITHUB_USERNAME}...\n")
    
    repos = fetch_user_repos()
    if not repos:
        print("No repositories found or error occurred")
        return
    
    print("\n📚 Processing repositories and extracting information...\n")
    projects, skills = create_project_data(repos)
    
    if not projects:
        print("No suitable projects found")
        return
    
    print(f"✓ Extracted {len(projects)} projects")
    print(f"✓ Identified {len(skills)} skills\n")
    
    # Generate HTML
    projects_html = generate_html_projects(projects)
    skills_html = generate_skill_cards(skills)
    
    # Save to JSON for easy access
    data = {
        'projects': projects,
        'skills': skills
    }
    
    with open('github_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("✓ Saved data to github_data.json")
    print(f"\nProject data extracted:")
    for project in projects:
        print(f"  - {project['name']}: {project['description'][:60]}...")
    
    print(f"\nSkills identified: {', '.join(sorted(set(skills))[:10])}")

if __name__ == "__main__":
    main()
