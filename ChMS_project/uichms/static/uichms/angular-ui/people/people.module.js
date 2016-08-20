// People module

(function() {

  angular
    .module('PeopleModule', [
      'ui.router',
    ])

    .config(['$stateProvider',
        function($stateProvider) {
          var staticDir = '/static/uichms/angular-ui/';
          var parentStateDir = staticDir.concat('people/states/');

          $stateProvider
            // Parent States in Admin

            /*.state('userDetailsState', {
              url : '#/userdetails',
              templateUrl : '/static/uichms/angular-ui/people/states/userDetails.template.html'
            })

            .state('userDetailsState', {
              url : '#/userdetails',
              templateUrl : '/static/angular-ui/admin/states/people/userDetails.template.html'
            })
            .state('personalInfoState', {
              url : '#/personalinfo',
              templateUrl : '/static/angular-ui/admin/states/people/personalInfo.template.html'
            })
            .state('contactInfoState', {
              url : '#/contactinfo',
              templateUrl : '/static/angular-ui/admin/states/people/contactInfo.template.html'
            })
            .state('familyState', {
              url : '#/family',
              templateUrl : '/static/angular-ui/admin/states/people/family.template.html'
            })
            .state('ministryInfoState', {
              url : '#/ministryinfo',
              templateUrl : '/static/angular-ui/admin/states/people/ministryInfo.template.html'
            })
            .state('professionSkillsInterestsState', {
              url : '#/professionskillsinterests',
              templateUrl : '/static/angular-ui/admin/states/people/professionSkillsInterests.template.html'
            })*/

        }
    ])
  
    .controller('PeopleController', ['$scope', '$http',
      PeopleController
    ]);

  function PeopleController($scope, $http) {
    var peopleVm = this;
    peopleVm.PeopleModel = {};

    peopleVm.PeopleModel.peopleList = [];
    for (var i = 0; i < 20; i++) {
      peopleVm.PeopleModel.peopleList.push(
          {
            no : i,
            lName : 'lName ' + i,
            fName : 'fName ' + i,
            mName : 'mName ' + i
          }
      );
    }
  };

}());

