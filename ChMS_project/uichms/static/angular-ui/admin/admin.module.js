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
      $state.go('accountState');
    }
  };

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  };

}());

