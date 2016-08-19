from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'churches', views.ChurchViewSet, 'church')
router.register(r'people', views.PersonViewSet, 'person')
router.register(r'interests', views.InterestViewSet)
router.register(r'people_interests',
                views.PersonInterestViewSet, 'person_interest')
router.register(r'skills_and_professions',
                views.SkillAndProfessionViewSet, 'skill')
router.register(r'spiritual_milestones',
                views.SpiritualMilestoneViewSet, 'spiritual_milestone')
router.register(r'ministries', views.MinistryViewSet, 'ministry')
router.register(r'member_statuses', views.MemberStatusViewSet, 'member_status')
