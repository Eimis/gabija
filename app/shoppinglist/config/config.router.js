var myApp = angular.module('shoppinglist', ['ui.router', 'oc.lazyLoad', 'ui.toggle', ]);

myApp.config(function($stateProvider) {

  //$urlRouterProvider.otherwise('/');

  $stateProvider

  .state('home', {
    url: '/',
    template: '<shopping-list></shopping-list>',
    resolve: {
      deps: ['$ocLazyLoad', function($ocLazyLoad) {

        //extra css:
        return $ocLazyLoad.load([
          '/static/shoppinglist/components/shoppinglist/shoppinglist.css',
        ])
        .then(function(){
          return $ocLazyLoad.load([
            '/static/shoppinglist/components/shoppinglist/shoppinglist.model.js',
            '/static/shoppinglist/components/shoppinglist/shoppinglist.component.js',
          ]);
        });

      }]
    }

  });

});
