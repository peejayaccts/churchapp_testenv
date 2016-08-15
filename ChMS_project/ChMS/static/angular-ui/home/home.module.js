// Home module
var homeModule = angular.module('HomeModule', []);

homeModule.controller('HomeController', ['$scope', '$http',
		function($scope, $http) {
      $scope.HomeModel ={};
			$scope.HomeModel.eventList = [
        {
          title : 'Camp 2016 "Led by the Holy Spirit"',
          body : 'Dear all, greetings. lorem ipsum lorem ipsum'
        },
        {
          title : 'Event 2',
          body : 'Event 2, greetings. lorem ipsum lorem ipsum'
        },
        {
          title : 'Event 3',
          body : 'Event 3, greetings. lorem ipsum lorem ipsum'
        },
        {
          title : 'Event 4',
          body : 'Event 4, greetings. lorem ipsum lorem ipsum'
        },
        {
          title : 'Event 5',
          body : 'Event 5, greetings. lorem ipsum lorem ipsum'
        }
      ];
		}
]);
