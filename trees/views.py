from .models import TreeNode
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TreeNodeSerializer


class NodeCreate(APIView):
    queryset = TreeNode.objects.all()
    serializer_class = TreeNodeSerializer

    def post(self, request, format=None):
        """
        Attach the root node to the serializer, then save it.
        :param request:
        :param format:
        :return:
        """
        serializer = TreeNodeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        root = TreeNode.objects.get(is_root=True)
        serializer.save(root=root, is_root=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreeNode.objects.all()
    serializer_class = TreeNodeSerializer
