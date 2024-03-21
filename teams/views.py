from rest_framework.views import APIView, Response, Request
from django.forms.models import model_to_dict
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from teams.models import Team
from utils import data_processing

# Create your views here.
class TeamView(APIView):
    def post(self, request: Request):
        new_team = (request.data)
        try:
            data_processing(new_team)  
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({'error': str(e)}, status=400)

        team = Team.objects.create(**new_team)
        return Response(model_to_dict(team), 201)
        
    def get(self, request):
        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            teams_dict.append(model_to_dict(team))

        return Response(teams_dict, 200)

class TeamDetailView(APIView):
    def get(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, 404
            )

        converted_team = model_to_dict(found_team)
        return Response(converted_team, 200)
    
    def delete(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, 404
            )
        found_team.delete()
        return Response(status=204)

    def patch(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, 404
            )
        for k, v in req.data.items():
            setattr(found_team, k, v)

        found_team.save()
        converted_team = model_to_dict(found_team)
        return Response(converted_team)
