### ansible-roles
Collection of ansible roles that I find useful

### Setup

Create a local virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python requirements:

```bash
pip install -r requirements.txt
```

Install the Ansible Galaxy collections:

```bash
ansible-galaxy collection install -r requirements.yml
```

