def vim_faker(provider, **kwargs):
    try:
        from faker import Faker, Factory
        fake = Factory.create(kwargs.pop('l10n')) if kwargs.get('l10n') else Faker()
        return fake.__getattribute__(provider)(**kwargs)
    except Exception as e:
        return e.args[0]
