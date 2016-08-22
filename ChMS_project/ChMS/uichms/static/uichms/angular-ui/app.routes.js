// App routing
(function() {

  angular
    .module('ChMS-ui')

    .config(['$routeProvider', '$stateProvider', '$urlRouterProvider',
  		function($routeProvider, $stateProvider, $urlRouterProvider) {
  			var static_dir = '/static/uichms/angular-ui/';
        var parentStateDir = static_dir.concat('admin/states/');
        var accountStatesDir = parentStateDir.concat('accountManagement/states/');
        var systemStatesDir = parentStateDir.concat('systemConfig/states/');

  			// $routeProvider
  				// .when('/', {
  				//   templateUrl : static_dir.concat('login/login.template.html'),
  				//   controller : 'LoginController'
  				// })
  				// .when('/home', {
  				// 	templateUrl : static_dir.concat('home/home.template.html'),
  				// 	controller : 'HomeController'
  				// })
  				// .when('/login', {
  				// 	templateUrl : static_dir.concat('login/login.template.html'),
  				// 	controller : 'LoginController'
  				// })
  				// .when('/people', {
  				// 	templateUrl : static_dir.concat('people/people.template.html'),
  				// 	controller : 'PeopleController',
          //   controllerAs : 'peopleCtrl'
  				// })
  				// .when('/ministries', {
  				// 	templateUrl : static_dir.concat('ministries/ministries.template.html'),
  				// 	controller : 'MinistriesController',
          //   controllerAs : 'ministryCtrl'
  				// })
  				// .when('/admin', {
  				// 	templateUrl : static_dir.concat('admin/admin.template.html'),
  				// 	controller : 'AdminController',
          //   controllerAs : 'adminCtrl'
  				// });
        
        $urlRouterProvider.otherwise('login');

        $stateProvider
          .state('home', {
            url : '/home',
  					templateUrl : static_dir.concat('home/home.template.html'),
            controller : 'HomeController',
            controllerAs : 'homeCtrl'
          })
  				.state('people', {
            url : '/people',
  					templateUrl : static_dir.concat('people/people.template.html'),
  					controller : 'PeopleController',
            controllerAs : 'peopleCtrl'
  				})
          .state('login', {
            url : '/login',
  					templateUrl : static_dir.concat('login/login.template.html'),
            controller : 'LoginController',
            controllerAs : 'loginCtrl'
          })
          .state('ministries', {
            url : '/ministries',
  					templateUrl : static_dir.concat('ministries/ministries.template.html'),
            controller : 'MinistriesController',
            controllerAs : 'ministryCtrl'
          })
          .state('admin', {
            url : '/admin',
  					templateUrl : static_dir.concat('admin/admin.template.html'),
            controller : 'AdminController',
            controllerAs : 'adminCtrl'
          })
  		}

    ]);

}());
