// Admin module

(function() {

  angular
    .module('AdminModule', [
      'ui.router',
    ])

    .config(['$stateProvider', '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
          var staticDir = '/static/uichms/angular-ui/';
          var parentStateDir = staticDir.concat('admin/states/');
          var accountStatesDir = parentStateDir.concat('accountManagement/states/');
          var systemStatesDir = parentStateDir.concat('systemConfig/states/');

          $stateProvider
            // Parent States in Admin
            .state('admin.account', {
              url : '/account',
              templateUrl : parentStateDir.concat('accountManagement/accountManagement.template.html')
            })
            .state('admin.church', {
              url : '/churchsettings',
              templateUrl : parentStateDir.concat('churchSettings/churchSettings.template.html')
            })
            .state('admin.system', {
              url : '/systemconfig',
              templateUrl : parentStateDir.concat('systemConfig/systemConfig.template.html')
            })

            // Account Management States
            .state('admin.account.users', {
              url : '/users',
              templateUrl : accountStatesDir.concat('users.template.html')
            })
            .state('admin.account.roles', {
              url : '/roles',
              templateUrl : accountStatesDir.concat('roles.template.html')
            })
            
            // System Configuration States
            .state('admin.system.interests', {
              url : '/interests',
              templateUrl : systemStatesDir.concat('interests.template.html')
            })
            .state('admin.system.skills', {
              url : '/skills',
              templateUrl : systemStatesDir.concat('skills.template.html')
            })
            .state('admin.system.spiritual', {
              url : '/spiritual',
              templateUrl : systemStatesDir.concat('spiritual.template.html')
            })
            .state('admin.system.member', {
              url : '/member',
              templateUrl : systemStatesDir.concat('member.template.html')
            })
            .state('admin.system.ministries', {
              url : '/ministries',
              templateUrl : systemStatesDir.concat('ministries.template.html')
            })
            .state('admin.system.churches', {
              url : '/churches',
              templateUrl : systemStatesDir.concat('church.template.html')
            });

          // Set default state when entering Admin view
          $urlRouterProvider.when('/admin', '/admin/account/users')
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

  };

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  };

}());

