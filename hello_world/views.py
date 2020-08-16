import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from hello_world.models import World
from hello_world.serializers import WorldSerializer


class HelloWorld(APIView):
    """
    Example hello world view class
    """

    def get(self, request):
        """
        Basic Get that doesn't interact with the Database
        :param request: Necessary request parameter for APIView get method
        :return: Hello world message (I can't remember why safe=False)
        """
        return JsonResponse("Hello World!", safe=False)

    def post(self, request):
        """
        Basic Post receiving a JSON body that doesn't interact with the Database
        :param request: Request body containing a world string attribute
        :return: Hello world message specifying the sent world
                 Fails with a 400 error if anything happens
        """
        try:
            world = json.loads(request.body).get("world")
            return JsonResponse("Hello {} World!".format(world), safe=False)
        except Exception as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


class WorldView(APIView):
    """
    Example hello world view CRUD class
    """

    def get(self, request):
        """
        Basic Get taking all entities from the Database
        :param request: request object containing the galaxy param in the url
        :return: All world entities or all world entities matching the galaxy in the request
        """
        worlds = World.objects.all()
        galaxy = request.GET.get('galaxy', None)
        if galaxy is not None:
            worlds = worlds.filter(galaxy__icontains=galaxy)
        worlds_serializer = WorldSerializer(worlds, many=True)
        return JsonResponse(worlds_serializer.data, safe=False)  # 'safe=False' for objects serialization

    def delete(self, request):
        """
        Basic Delete removing all entities from the Database
        :param request: Necessary request parameter for APIView delete method
        :return: Message containing the info about the worlds removed
        """
        count = World.objects.all().delete()
        return JsonResponse({'message': '{} Worlds were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        """
        Basic Post creating an entity from the Database
        :param request: Request body containing all the inf of the new world entity
        :return: Created entity
        """
        world_data = JSONParser().parse(request)
        world_serializer = WorldSerializer(data=world_data)
        if world_serializer.is_valid():
            world_serializer.save()
            return JsonResponse(world_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(world_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorldDetailView(APIView):
    """
    Example hello world view detail CRUD class identifying the worlds by its name
    """

    def get(self, request, name):
        """
        Basic Get request
        :param request:
        :param name:
        :return:
        """
        world = World.objects.get(name=name)
        world_serializer = WorldSerializer(world)
        return JsonResponse(world_serializer.data)

    def delete(self, request, name):
        """

        :param request:
        :param name:
        :return:
        """
        world = World.objects.get(name=name)
        world.delete()
        return JsonResponse({'message': '{} World was deleted successfully!'.format(world.name)},
                            status=status.HTTP_204_NO_CONTENT)

    def put(self, request, name):
        """

        :param request:
        :param name:
        :return:
        """
        world = World.objects.get(name=name)
        world_data = JSONParser().parse(request)
        world_serializer = WorldSerializer(world, data=world_data)
        if world_serializer.is_valid():
            world_serializer.save()
            return JsonResponse(world_serializer.data)
        return JsonResponse(world_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, name):
        """

        :param request:
        :param name:
        :return:
        """
        world = World.objects.get(name=name)
        world_data = JSONParser().parse(request)
        world_serializer = WorldSerializer(world,
                                           data=world_data, partial=True)  # set partial=True to update a data partially
        if world_serializer.is_valid():
            world_serializer.save()
            return JsonResponse(world_serializer.data)
        return JsonResponse(world_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
