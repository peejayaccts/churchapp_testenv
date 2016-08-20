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
            .state('people.peopleList', {
              url : '/peopleList',
              templateUrl : parentStateDir.concat('peopleList.template.html')
            })

            .state('people.userDetailsState', {
              url : '/userdetails',
              templateUrl : parentStateDir.concat('userDetails.template.html')
            })

            .state('people.personalInfoState', {
              url : '/personalinfo',
              templateUrl : parentStateDir.concat('personalInfo.template.html')
            })
            .state('people.contactInfoState', {
              url : '/contactinfo',
              templateUrl : parentStateDir.concat('contactInfo.template.html')
            })
            .state('people.familyState', {
              url : '/family',
              templateUrl : parentStateDir.concat('family.template.html')
            })
            .state('people.ministryInfoState', {
              url : '/ministryinfo',
              templateUrl : parentStateDir.concat('ministryInfo.template.html')
            })
            .state('people.professionSkillsInterestsState', {
              url : '/professionskillsinterests',
              templateUrl : parentStateDir.concat('professionSkillsInterests.template.html')
            })

        }
    ])
  
    .controller('PeopleController', ['$scope', '$http', '$state',
      PeopleController
    ]);

  function PeopleController($scope, $http, $state) {
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

    if ($state.current.name === 'people') {
      $state.go('people.peopleList');
    }
  };

}());

