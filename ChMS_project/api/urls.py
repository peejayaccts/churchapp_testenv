from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'churches', views.ChurchViewSet)
router.register(r'people', views.PersonViewSet)
router.register(r'interests', views.InterestViewSet)
router.register(r'skills_and_professions',
                views.SkillAndProfessionViewSet, 'skill')
router.register(r'spiritual_milestones',
                views.SpiritualMilestoneViewSet, 'spiritual_milestone')
