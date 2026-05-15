import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-open-synergy-opnsynid-crm-subscription",
    description="Meta package for open-synergy-opnsynid-crm-subscription Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-subscription_crm',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
