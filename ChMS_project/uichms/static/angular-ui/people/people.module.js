// People module

(function() {

  angular
    .module('PeopleModule', [])
  
    .controller('PeopleController', ['$scope', '$http',
      PeopleController
    ]);

  function PeopleController($scope, $http) {
    var peopleVm = this;
    peopleVm.PeopleModel = {};
    // peopleVm.PeopleModel.peopleList = [];

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

