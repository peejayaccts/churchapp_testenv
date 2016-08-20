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

            .state('userDetailsState', {
              url : '#/userdetails',
              templateUrl : parentStateDir.concat('userDetails.template.html')
            })

            // .state('userDetailsState', {
            //   url : '#/userdetails',
            //   templateUrl : '/static/angular-ui/admin/states/people/userDetails.template.html'
            // })
            .state('personalInfoState', {
              url : '#/personalinfo',
              templateUrl : parentStateDir.concat('personalInfo.template.html')
            })
            .state('contactInfoState', {
              url : '#/contactinfo',
              templateUrl : parentStateDir.concat('contactInfo.template.html')
            })
            .state('familyState', {
              url : '#/family',
              templateUrl : parentStateDir.concat('family.template.html')
            })
            .state('ministryInfoState', {
              url : '#/ministryinfo',
              templateUrl : parentStateDir.concat('ministryInfo.template.html')
            })
            .state('professionSkillsInterestsState', {
              url : '#/professionskillsinterests',
              emplateUrl : parentStateDir.concat('professionSkillsInterests.template.html')
            })

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

