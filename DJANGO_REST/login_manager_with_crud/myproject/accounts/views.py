from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserValidationSerializer
from .models import CustomUser
from rest_framework import status


# User registration API (users will be inactive until validated)
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful, please wait for admin validation.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Admin user validation API (only superusers or admins can validate)
class UserValidationAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Validate user (set is_validated to True)
        user.is_validated = True
        user.is_active = True
        user.save()

        return Response({'message': 'User validated successfully'}, status=status.HTTP_200_OK)


# User login API (returns JWT token after validation)
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = CustomUser.objects.filter(username=username).first()

        if user and user.check_password(password):
            if not user.is_validated:
                return Response({'error': 'User is not validated yet'}, status=status.HTTP_400_BAD_REQUEST)

            # Generate JWT token for the user
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)
