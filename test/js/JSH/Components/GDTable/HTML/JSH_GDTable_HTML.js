"use strict";
class HTML_GDTable extends JSH_GDTable_Properties{      
    getStr(){
        return  "<div class="+this.getClassName()+">";	
    }
} 

class HTML_GDRow extends JSH_GDTable_Properties{      
    getStr(){
        return `<!--${this.getText()} -->`;
    }
}

class HTML_GDTitle extends JSH_GDTable_Properties{      
    getStr(){
        return `<header class="${this.getClassName()}" >${this.getText()}</header>`;
    }
}

class HTML_GDCol extends JSH_GDTable_Properties{      
    getStr(){
        return "<div class=\""+this.getClassName()+"\" >"+this.getText()+"</div>";
    }
}

class HTML_GDEnd extends JSH_GDTable_Properties{      
    getStr(){
        return "</div>";	
    }
}
