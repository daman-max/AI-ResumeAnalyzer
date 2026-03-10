import re 

def extract_skills(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9+ ]', ' ', text)

    with open("analyzer/data/skills.txt" ,"r") as file:
        skills = [skill.strip() for skill in file.readlines()] 

        found_skills = set()

        for skill in skills:
            if skill in text:
                found_skills.add(skill)


        return sorted(found_skills)        