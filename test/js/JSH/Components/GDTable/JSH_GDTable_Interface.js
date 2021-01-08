"use strict";
class JSH_GDTable_Interface extends JSH_Components{

  addTable(className = "") {
    let tObjet = new HTML_GDTable();    
    tObjet.setClassName(className);
    // tObjet.setStringTabs(this.getStrToTabs());
    this.add(tObjet);
    // this.incTabs();
    return this;
  }

  addRow(text = "", className = "") {
    let tObjet = new HTML_GDRow();
    tObjet.setText(text); 
    // tObjet.setStringTabs(this.getStrToTabs());       
    this.add(tObjet);  
    // this.incTabs();
    return this;
  }

  addTitle(text = "", className = "") {
    let tObjet = new HTML_GDTitle();
    tObjet.setText(text);
    tObjet.setClassName(className);
    // tObjet.setStringTabs(this.getStrToTabs());
    this.add(tObjet);
    return this;
  }

  addCol(text = "", className = "") {
    let tObjet = new HTML_GDCol();
    tObjet.setText(text);
    tObjet.setClassName(className);
    // tObjet.setStringTabs(this.getStrToTabs());
    this.add(tObjet);
    return this;
  }
  
  addEnd() {
    let tObjet = new HTML_GDEnd();
    // tObjet.setStringTabs(this.getStrToTabs());
    this.add(tObjet);
    // this.decTabs();
    return this;
  }
}
