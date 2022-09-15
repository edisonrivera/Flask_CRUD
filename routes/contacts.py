from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contact', __name__)
@contacts.route('/')
def home():
    contacts_actual = Contact.query.all()
    return render_template('index.html', contacts = contacts_actual)

@contacts.route('/new', methods=['POST'])
def add_contact():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    new_contact = Contact(name, last_name, email, phone)
    db.session.add(new_contact)
    db.session.commit()
    flash("Contacto añadido")
    return redirect(url_for('contact.home'))

@contacts.route('/delete/<id>')
def delete_contact(id):
    contact_delete = Contact.query.get(id)
    db.session.delete(contact_delete)
    db.session.commit()
    flash("Contacto eliminado")
    return redirect(url_for('contact.home'))

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update_contact(id):
    contact_update = Contact.query.get(id)
    if request.method == 'POST':
        contact_update.name = request.form['name']
        contact_update.last_name = request.form['last_name']
        contact_update.email = request.form['email']
        contact_update.phone = request.form['phone']
        db.session.commit()
        flash("Contacto actualizado")
        return redirect(url_for('contact.home'))
        
    return render_template('update.html', contact=contact_update)

@contacts.route('/about')
def about():
    return "Acerca de mi"