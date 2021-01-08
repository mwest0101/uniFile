"use strict";
class JSH_Components extends JSH_ObjectDriver {
    
    newGDTable(className = "") {
        let tObjet = new JSH_GDTable_Interface(className);
        tObjet.addTable(className);
        return tObjet;
    }
    
    addGDTable(className = "") {
        let tObjet = new JSH_GDTable_Interface(className);
        tObjet.addTable(className);
        this.add(tObjet);        
        return tObjet;
    }

}
