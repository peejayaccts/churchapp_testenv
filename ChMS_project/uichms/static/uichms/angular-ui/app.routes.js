// App routing
(function() {

  angular
    .module('ChMS-ui')

    // All API Request will call this function to check authentication
	.factory('authInterceptor', function ($rootScope, $q, $window, $location) {
	return {
	    request: function (config) {
		config.headers = config.headers || {};
		if ($window.sessionStorage.token) {
		    config.headers.Authorization = 'JWT ' + $window.sessionStorage.token;
		}
		return config;
	    },
	    responseError: function (response) {
		console.log('ERROR');
		console.log(response);
		if (response.status === 401) {
		    // handle the case where the user is not authenticated
		    alert('Please Log-in first');
		    $location.path('/login')
		}
		return $q.reject(response);
	    }
	};
    })
    
	.config(['$routeProvider', '$stateProvider', '$urlRouterProvider', '$httpProvider',
  		 function($routeProvider, $stateProvider, $urlRouterProvider, $httpProvider) {
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

		     // Set All API Request to go to function
		     $httpProvider.interceptors.push('authInterceptor');

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
