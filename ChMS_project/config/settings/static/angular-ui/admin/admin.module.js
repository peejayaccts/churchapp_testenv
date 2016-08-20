// Admin module

(function() {

  angular
    .module('AdminModule', [
      'ui.router',
    ])

    .config(['$stateProvider',
        function($stateProvider) {

          $stateProvider
            .state('accountState', {
              url : '#/account',
              templateUrl : '/static/angular-ui/admin/states/accountManagement/accountManagement.template.html'
            })
            .state('churchSettingsState', {
              url : '#/churchsettings',
              templateUrl : '/static/angular-ui/admin/states/churchSettings/churchSettings.template.html'
            })
            .state('systemConfigState', {
              url : '#/systemconfig',
              template : '<p>System Configuration</p>'
            })

            //PEOPLE templates
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
            })

        }
    ])
  
    .controller('AdminController', ['$scope', '$http', '$state',
      AdminController
    ]);

  function AdminController($scope, $http, $state) {
    var adminVm = this;
    var roleList = ['Super User', 'Pastor', 'System'];
    adminVm.AdminModel = {};
    adminVm.AdminModel.usersList = [];
    for(var i = 0; i < 20; i++) {
      adminVm.AdminModel.usersList.push({
        no : i,
        username : 'Username ' + i,
        name : 'Name ' + i,
        role : roleList[getRandomInt(0,3)]
      });
    }

    /* Sets the page's state */
    if ($state.current.name === "") {
      /*$state.go('accountState');*/
      $state.go('familyState');
    }
  };

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  };

}());

