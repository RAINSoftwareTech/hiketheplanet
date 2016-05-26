# -*- coding: utf-8 -*-


class FormsetViewMixin(object):
    formset_classes = []
    object = None

    def get_form_formsets(self, post_data=None):
        form_class = self.get_form_class()
        forms_dict = {'form': self.get_form(form_class)}
        formsets = []
        try:
            for formset_class in self.formset_classes:
                try:
                    prefix = formset_class.model.__name__.lower()
                    formsets.append(formset_class(post_data, prefix=prefix,
                                                  instance=self.object))
                except AttributeError:
                    raise ValueError('{} is not a formset '
                                     'class.'.format(formset_class))
            forms_dict['formsets'] = formsets
        except TypeError:
            raise TypeError('formset_classes must be an iterable. '
                            'Did you mean [{0}] or '
                            '({0},)?'.format(self.formset_classes))
        return forms_dict

    def get(self, request, *args, **kwargs):
        forms_dict = self.get_form_formsets()
        return self.render_to_response(
            self.get_context_data(**forms_dict))

    def post(self, request, *args, **kwargs):
        forms_dict = self.get_form_formsets(post_data=request.POST)
        form = forms_dict.get('form')
        formsets = forms_dict.get('formsets', [])
        if not form.is_valid():
            return self.form_invalid(forms_dict)
        else:
            for form in formsets:
                if not form.is_valid():
                    return self.form_invalid(forms_dict)
            else:
                return self.form_valid(form, formsets)

    def form_valid(self, form, formsets):
        form_instance = form.save(commit=True)
        for formset in formsets:
            formset.instance = form_instance
            formset.save(commit=True)
        return super(FormsetViewMixin, self).form_valid(form)

    def form_invalid(self, forms_dict):
        return self.render_to_response(
            self.get_context_data(forms_dict))
