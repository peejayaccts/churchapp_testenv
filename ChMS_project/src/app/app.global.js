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
  .constant("$API", {
     ministries  : "http://127.0.0.1:8000/api/ministries/",
     churches    : "http://127.0.0.1:8000/api/churches/",
     people      : "http://127.0.0.1:8000/api/people/",
     interests   : "http://127.0.0.1:8000/api/interests/",


  })
  .constant("$HTTP", {

     fields : {
         withCredentials : true
         /*headers: { 'Content-Type' : 'application/json'}*/
     }

  });
