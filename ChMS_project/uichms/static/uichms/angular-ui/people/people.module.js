// People module

(function() {

  angular
    .module('PeopleModule', [
      'ui.router',
    ])

    .config(['$stateProvider', '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
          var staticDir = '/static/uichms/angular-ui/';
          var parentStateDir = staticDir.concat('people/states/');

          $stateProvider
            // Parent States in Admin
            .state('people.peopleList', {
              url : '/peoplelist',
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
            });

          // Set default state when entering People view
          $urlRouterProvider.when('/people', '/people/peoplelist');

        }
    ])
  
    .controller('PeopleController', ['$scope', '$http', '$state',
      PeopleController
    ]);

  function PeopleController($scope, $http, $state) {
    var peopleVm = this;
    peopleVm.PeopleModel = {};
      peopleVm.PeopleModel.peopleList = [];
      
      $http({url: app.people.url, method: 'GET'})
	 .success(function (data, status, headers, config) {
	     console.log(data); // Should log 'foo'
	     for (var i = 0; i < data.length; i++) {
		 var person = data[i];
		 peopleVm.PeopleModel.peopleList.push(
		     {
			 no : i,
			 lName : (person['last_name']).substring(0,10),
			 fName : (person['first_name']).substring(0,10),
			 mName : (person['middle_initial']).substring(0,10)
		     }
		 );
	     }
	 }
      );
      

  };

}());

