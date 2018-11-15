import setuptools

def configure():
# Initialize the setup kwargs
    kwargs = {
            'name': 'PhasePApy',
            'version': '1.1',
            'author': 'Chen Chen',
            'author_email': 'c.chen@ou.edu',
            'description': 'A robust pure python package for automatic '\
                    'identification of seismic phases',
            'packages': ['phasepapy']
            }
    return(kwargs)

if __name__ == '__main__':
    kwargs = configure()
    setuptools.setup(**kwargs)
