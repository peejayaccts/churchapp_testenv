// Ministries module

(function() {

  angular
    .module('MinistriesModule', [])
  
    .controller('MinistriesController', ['$scope', '$http',
      MinistriesController
    ]);

  function MinistriesController($scope, $http) {
    var ministryStatus = ['Active', 'Inactive'];
    var ministryCtrl = this;
    

    ministryCtrl.MinistryModel = {};
    ministryCtrl.MinistryModel.ministryList = [];

    for (var i=0; i<20; i++) {
      ministryCtrl.MinistryModel.ministryList.push({
        no : i,
        name : 'Ministry ' + i,
        status : ministryStatus[getRandomInt(0,2)],
        leaders : 'Leader ' + i,
      });
    }

    
  };

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  };

}());

