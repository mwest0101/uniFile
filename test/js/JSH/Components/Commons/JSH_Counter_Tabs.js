"use strict";
class JSH_Counter_Tabs {
    constructor() {         
        var stringTabs="";
        var contTab=0;
    }

    static setContTab(value) {
        this.contTab = value;
    }
    
    static getContTab() {
        return this.contTab;
    }
    
    static incTabs() {
        this.setContTab(this.getContTab() + 1);
    }
    
    static decTabs() {
        this.setContTab(this.getContTab() - 1);
    }

    static getStringTabs(){
        return this.stringTabs;
    }

    static setStringTabs(int_text){
        return this.stringTabs = int_text;
    }
      
    
    static getStrToTabs() {
        let strRes = "";
        for (let i = 0; i < super.getContTab(); i++) {
            strRes = strRes + "\n";
        }
        return strRes;
    }
      
  }