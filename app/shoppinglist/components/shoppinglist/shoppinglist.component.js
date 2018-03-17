'use strict';

var shoppingListController = function($rootScope, $scope, shoppingListModel, localStorageService) {

  var ctrl = this;
  ctrl.model = shoppingListModel;

  //Initial scope values:
  ctrl.currentItem = null;
  ctrl.allItems = [];

  ctrl.$onInit = function() {
    ctrl.loadLocalData();

    ctrl.model.listData(ctrl).then(function(resp){
      ctrl.allItems = resp.items;
    });
  };

  ctrl.addItem = function(addedItem) {
    if (addedItem) {
      ctrl.currentItem = null;

      ctrl.model.submitData(ctrl, addedItem).then(function(resp){
        ctrl.allItems.push(resp.shopping_item);
        ctrl.saveDataLocally();
      });
    }
  };

  ctrl.clearItems = function() {
    ctrl.model.clearData(ctrl).then(function(resp){
      if (resp.ok) {
        ctrl.model.listData(ctrl);
      }
    });
  };

  ctrl.updateItem = function(shopping_item) {
    ctrl.model.updateData(ctrl, shopping_item).then(function(resp){
      if (resp.ok) {
        //Reload data from backend:
        ctrl.model.listData(ctrl);
      }
    });
  };

  ctrl.changeOfflineMode = function() {
    //ctrl.saveDataLocally();
  };

  ctrl.loadLocalData = function() {
    var offlineMode = localStorageService.get('offlineMode');
    ctrl.offlineMode = offlineMode || false;  // can be null
  };

  ctrl.saveDataLocally = function() {
    localStorageService.set('offlineMode', ctrl.offlineMode);
    localStorageService.set('allItems', ctrl.allItems);
  };

};

angular
  .module('shoppinglist')
  .component('shoppingList', {
    templateUrl: 'static/shoppinglist/components/shoppinglist/shopping-list.html',
    controller: shoppingListController,
  });
