class FormFieldMixin:
    def __str__(self):
        return self.as_formfield()

    def as_formfield(self):
        """Return this form rendered as HTML <div class="formfield">s."""
        return self._html_output(
            normal_row='<div id="%(field_name)s" class="formfield" data-mdc-auto-init="FormField" '
                       '%(html_class_attr)s>%(label)s%(field)s%(errors)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html='<span class="helptext">%s</span>',
            errors_on_separate_row=False,
        )

    class Media:
        css = {
            'all': ('css/formfield.css',)
        }
        js = ('js/formfield.js',)
