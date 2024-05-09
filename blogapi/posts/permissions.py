from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #faqat ko'rish uchun ruxsat
        if request.mathod in permissions.SAFE_METHODS:
            return True
        #o'zgartirish(yozish) uchun ruxsatnoma faqatgina post muallifiga beriladi
        return obj.author==request.user

