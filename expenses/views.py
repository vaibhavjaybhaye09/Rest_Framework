from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from .serializers import TransactionsSerializer

class TransactionAPI(APIView):
    def get(self, request):
        transactions = Transactions.objects.all().order_by('-id')
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transaction created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({'error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            transaction = Transactions.objects.get(pk=pk)
        except Transactions.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionsSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transaction updated', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': 'ID is required for delete'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            transaction = Transactions.objects.get(pk=pk)
            transaction.delete()
            return Response({'message': 'Transaction deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Transactions.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
