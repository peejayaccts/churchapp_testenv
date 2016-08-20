// Admin module

(function() {

  angular
    .module('AdminModule', [
      'ui.router',
    ])

    .config(['$stateProvider',
        function($stateProvider) {
          var staticDir = '/static/uichms/angular-ui/';
          var parentStateDir = staticDir.concat('admin/states/');
          var systemStatesDir = parentStateDir.concat('systemConfig/states/');

          $stateProvider
            // Parent States in Admin
            .state('account', {
              url : '#/account',
              templateUrl : parentStateDir.concat('accountManagement/accountManagement.template.html')
            })
            .state('church', {
              url : '#/churchsettings',
              templateUrl : parentStateDir.concat('churchSettings/churchSettings.template.html')
            })
            .state('system', {
              url : '#/systemconfig',
              controller : ['$scope', '$state', SystemConfigController],
              templateUrl : parentStateDir.concat('systemConfig/systemConfig.template.html')
            })
            
            // System Configuration States
            .state('system.interests', {
              url : '#/systemconfig/interests',
              templateUrl : systemStatesDir.concat('interests.template.html')
            })
            .state('system.skills', {
              url : '#/systemconfig/skills',
              templateUrl : systemStatesDir.concat('skills.template.html')
            })
            .state('system.spiritual', {
              url : '#/systemconfig/spiritual',
              templateUrl : systemStatesDir.concat('spiritual.template.html')
            })
            .state('system.member', {
              url : '#/systemconfig/member',
              templateUrl : systemStatesDir.concat('member.template.html')
            })
            .state('system.ministries', {
              url : '#/systemconfig/ministries',
              templateUrl : systemStatesDir.concat('ministries.template.html')
            })
            .state('system.churches', {
              url : '#/systemconfig/churches',
              templateUrl : systemStatesDir.concat('church.template.html')
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
      $state.go('account');
    }
  };

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  };

  function SystemConfigController($scope, $state){
    /* Sets the page's state */
    if ($state.current.name === "system") {
      $state.go('system.interests');
      console.log($state.current.name);
    }
  };

}());

