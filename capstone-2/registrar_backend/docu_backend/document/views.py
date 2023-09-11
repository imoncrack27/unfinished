from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from .forms import DocumentForm
from .models import Document, Category
from .serializers import DocumentSerializer, DocumentDetailSerializer, CategorySerializer
# Create your views here.

class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class NewestDocumentsView(APIView):
    def get(self, request, format=None):
        documents = Document.objects.all()[0:4]
        serializer = DocumentSerializer(documents, many=True)

        return Response(serializer.data)


class MyDocuView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        documents = Document.objects.filter(created_by=request.user)
        serializer = DocumentSerializer(documents, many=True)

        return Response(serializer.data)

class RequestDocumentView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = DocumentForm(request.data)

        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.save()

            return Response({'status': 'Document created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})

    def put(self, request, pk):
        document = Document.objects.get(pk=pk, created_by=request.user)
        form = DocumentForm(request.data, instance=document)
        form.save()

        return Response({'status': 'Document updated'})


    def delete(self, request, pk):
        document = Document.objects.get(pk=pk, created_by=request.user)
        document.delete()

        return Response({'status': 'Document deleted'})


class BrowseDocumentsView(APIView):
    def get(self, request, format=None):
        documents = Document.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')

        if query:
            documents = documents.filter(title__icontains=query)


        if categories:
            documents = documents.filter(category_id__in=categories.split(','))
    
        serializer = DocumentSerializer(documents, many=True)

        return Response(serializer.data)

class DocumentsDetailView(APIView):
    def get(self, request, pk, format=None):
        document = Document.objects.get(pk=pk)
        serializer = DocumentDetailSerializer(document)

        return Response(serializer.data)

