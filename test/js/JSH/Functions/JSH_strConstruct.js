"use strict";
class JSH_strConstruct extends JSH_Counter_Tabs{
  constructor() {
    super();
    this.returnStr = "";
    this.endln = "\n";
    this.tabln = "        ";
    this.contTab = 0;
    this.endIsEnabled = true;
    this.tabIsEnabled = true;
  }
  
  getEndLine() {
    return this.endln;
  }

  getTabLine() {
    return this.tabln;
  }

  oneLineEnd(text) {
    let retStr;
    if (text.substr(this.getEndLine().length * -1) == this.getEndLine()) {
      retStr = text;
    } else {
      retStr = text + this.getEndLine();
    }
    return retStr;
  }

  setString(text) {
    this.returnStr = text;
    
  }

  getString() {
    return this.returnStr;
  }

  resetString() {
    this.returnStr = "";
  }

  addString(text) {   
    this.setStringFilter(this.getString()+text);    
  }


  setStringFilter(text){
    // text = text.trim();
    if (text != "") {                
        this.setString(this.oneLineEnd(text));
    }
  }

  setHtmlToTag(contentId = "") {
    document.getElementById(contentId).innerHTML = this.getEndLine()+this.getString();
  }

  replaceString(searchSourceText, valToReplace) {
    let result = super.getString();
    return result.replace(searchSourceText, valToReplace, "gi");
  }

}