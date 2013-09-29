# -*- coding: utf-8 -*-
from django.template.defaultfilters import striptags
from rest_framework.serializers import ModelSerializer


class TicketSerializer(ModelSerializer):

    def to_native(self, obj):
        """
        Serialize objects -> primitives.
        """
        ret = self._dict_class()
        ret.fields = self._dict_class()
        ret.empty = obj is None

        for field_name, field in self.fields.items():
            field.initialize(parent=self, field_name=field_name)
            key = self.get_field_key(field_name)
            value = field.field_to_native(obj, field_name)
            if field_name in ['subject', 'text']:
                value = striptags(value)
            ret[key] = value
            ret.fields[key] = field
        return ret


class MessageSerializer(ModelSerializer):

    def to_native(self, obj):
        """
        Serialize objects -> primitives.
        """
        ret = self._dict_class()
        ret.fields = self._dict_class()
        ret.empty = obj is None

        for field_name, field in self.fields.items():
            field.initialize(parent=self, field_name=field_name)
            key = self.get_field_key(field_name)
            value = field.field_to_native(obj, field_name)
            if field_name == 'text':
                value = striptags(value)
            ret[key] = value
            ret.fields[key] = field
        return ret


