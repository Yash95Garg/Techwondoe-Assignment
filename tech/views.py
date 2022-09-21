from distutils.log import error
from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
import jwt
from rest_framework.permissions import IsAdminUser
import datetime
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from uuid import UUID

@api_view(['POST'])
@csrf_exempt
def login(request):
    username = request.data['username']
    password = request.data['password']
    users = User.objects.filter(username=username).first()
    if users is None:
        return Response("User Not Found!")
    if not users.check_password(password):
        return Response("Incorrect password!")
    else:
        user = authenticate(username=username , password = password)
        if user is None:
            return Response("Error!!")
        else:
            payload = {
                'id' : users.id,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
                'iat' : datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt' : token
            }
            return response
    

def Check_token(token):
    token = token
    dic = {}
    dic.update({"ischeck" : False})
    dic.update({"issuper" : False})
    if not token:
        return dic
    try:
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return dic
    users = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(users)
    try:
        dic.update({"ischeck" : True})
        if users.is_superuser:
            dic.update({"issuper" : True})
    except error:
        print("error!")
    return dic

@api_view(['GET','POST'])
def company_data(request):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'GET':
        posts = Company.objects.all()
        serializer = CompanySerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Access Not allowed")

@api_view(['GET'])
def companyfromID_inpath(request,cid):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'GET':
        try: 
            val = UUID(cid, version=4)
        except ValueError:
            return Response("Company doesn't exists!!")
        comp = Company.objects.filter(CompanyID=cid).first()
        if comp is None:
            return Response("Company doesn't exists!!")
        posts = Company.objects.get(CompanyID=cid)
        serializer = CompanySerializer(posts)
        return Response(serializer.data)
    return Response("Enter Data!")

@api_view(['GET','POST'])
def companyfromID(request):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'POST':
        cid = request.data["ID"]
        try: 
            val = UUID(cid, version=4)
        except ValueError:
            return Response("Company doesn't exists!!")
        comp = Company.objects.filter(CompanyID=cid).first()
        if comp is None:
            return Response("Company doesn't exists!!")
        posts = Company.objects.get(CompanyID=cid)
        serializer = CompanySerializer(posts)
        return Response(serializer.data)
    return Response("Enter Data!")


@api_view(['GET','POST'])
def companyfromName(request):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'POST':
        cname = request.data["name"]
        comp = Company.objects.filter(CompanyName=cname).first()
        if comp is None:
            return Response("Company doesn't exists!!")
        posts = Company.objects.get(CompanyName=cname)
        serializer = CompanySerializer(posts)
        return Response(serializer.data)  
    return Response("Enter Data!")


@api_view(['GET'])
def team_data(request):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'GET':
        posts = Team.objects.all()
        serializer = TeamSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def team_creation(request, cid):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'POST':
        data = request.data
        data["CompanyID"] = cid
        try: 
            val = UUID(cid, version=4)
        except ValueError:
            return Response("Company doesn't exists!!")
        
        comp = Company.objects.filter(CompanyID=cid).first()
        if comp is None:
            return Response("Company doesn't exists!!")
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("Enter Data!")

@api_view(['GET'])
def team_data_grouped(request):
    token = request.COOKIES.get('jwt')
    ans = Check_token(token)
    isauth = ans['ischeck']
    issuper = ans['issuper']
    if not isauth:
        return Response("User Not Authenticated! Login via /api/login")
    elif not issuper:
        return Response("Access Denied!")
    if request.method == 'GET':
        data = []
        posts = Company.objects.all()
        serializer = CompanySerializer(posts,many=True)
        for post in serializer.data:
            teams = Team.objects.filter(CompanyID=post["CompanyID"])
            serializer2 = TeamSerializer(teams,many=True)
            post.update({"team":[]})
            for team in serializer2.data:
                dicteam = {}
                dicteam["TeamID"] = team["TeamID"]
                dicteam["TeamLead"] = team["TeamLead"]
                print(dicteam)
                post["team"].append(dicteam)
            data.append(post) 
        
        return Response(data)
