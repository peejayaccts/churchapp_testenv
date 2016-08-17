// Admin module

(function() {

  angular
    .module('AdminModule', [])
  
    .controller('AdminController', ['$scope', '$http',
      AdminController
    ]);

  function AdminController($scope, $http) {
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

