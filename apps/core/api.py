from rest_framework import generics

class GeneralListAPIView(generics.ListAPIView):
    serialize_class = None

    def get_queryset(self):
        model = self.get_serializer_class().Meta.model
        return model.objects.filter(state=True)