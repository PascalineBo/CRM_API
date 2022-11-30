from rest_framework import status, exceptions
from rest_framework.response import Response

class DestroyMixin:
    """
    Behaviour of the destroy method.
    """

    def destroy(self, request, model_name, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": f"{model_name} successfully deleted"
        },
            status=status.HTTP_200_OK)