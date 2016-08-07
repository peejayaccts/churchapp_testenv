'use strict';

/**
 * @ngdoc overview
 * @name appsApp
 * @description
 * # appsApp
 *
 * Main module of the application.
 */
angular.module('appsApp')
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'components/home/homeView.html',
        controller: 'HomeCtrl',
        controllerAs: 'homeController'
      })
      .when('/people', {
        templateUrl: 'components/people/peopleView.html',
        controller: 'PeopleCtrl',
        controllerAs: 'peopleController'
      })
      .when('/ministries', {
        templateUrl: 'components/ministries/ministriesView.html',
        controller: 'MinistriesCtrl',
        controllerAs: 'ministriesController'
      })
      .when('/admin', {
        templateUrl: 'components/admin/adminView.html',
        controller: 'AdminCtrl',
        controllerAs: 'adminController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
