class FormField {
  constructor(root) {
    this.root = root;
    this.label = this.root.querySelector('label');
    this.input = this.root.querySelector('input, textarea, select');
    this.errorlist = this.root.querySelector('.errorlist');
    this.initialize();
  }

  static attachTo(root) {
    return new FormField(root);
  }

  initialize() {
    if (this.label && ['text', 'number', 'email', 'tel', 'password', 'textarea', 'select-one'].includes(this.input.type)) {
      if (this.input.placeholder === '') {
        this.label.style = '' +
          'position: absolute;\n' +
          'top: 13px;\n' +
          'left: 20px;\n' +
          'transition: .2s linear;\n' +
          'z-index: 3;\n' +
          'line-height: 22px;\n' +
          'color: #969696;\n' +
          'font-size: 15px;';

        if (this.input.value !== '' || document.activeElement === this.input) {
          this.label.style.display = 'None';
        }

        this.input.addEventListener('focus', () => {
          this.label.style.display = 'None';
        });

        this.input.addEventListener('blur', (event) => {
          if (event.target.value === '') {
            this.label.style.display = 'unset';
          }
        })
      } else {
        this.label.hidden = true;
      }
    }
    if (this.errorlist) {
      this.root.classList.add('formfield--error');
      this.errorlist.style.display = 'block';
      let value = this.input.value;
      this.input[this.input.tagName === 'SELECT' ? 'onchange' : 'onkeyup'] = () => {
        if (value && this.input.value === value) {
          this.root.classList.add('formfield--error');
          this.errorlist.style.display = 'block'
        } else {
          this.root.classList.remove('formfield--error');
          this.errorlist.style.display = 'none'
        }
      }
    } else {
      this.root.classList.remove('formfield--error');
    }
  }

  updateErrorList(errors = []) {
    if (errors.length) {
      if (!this.errorlist) {
        this.errorlist = document.createElement('ul');
        this.errorlist.classList.add('errorlist');
        this.input.after(this.errorlist);
      } else {
        this.errorlist.innerHTML = '';
      }
      for (let error of errors) {
        let listItem = document.createElement('li');
        listItem.innerText = error;
        this.errorlist.appendChild(listItem);
      }
    } else {
      if (this.errorlist) {
        this.errorlist.remove();
        this.errorlist = false;
      }
    }
    this.initialize();
  }
}

mdc.autoInit.mdcAutoInit.register('FormField', FormField);
