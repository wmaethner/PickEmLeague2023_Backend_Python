def update_model(model, data, keys, db):
    for key in keys:
        setattr(model, key, data[key])
    db.session.commit()
