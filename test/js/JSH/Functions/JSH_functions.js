"use strict";
class JSH_functions{

    constructor(){
        this.max=0;
        this.count=0;       
    };
    
    setMax(in_max){
        this.max=in_max;
    }
    
    getMax(){
        return this.max;
    }

    setCount(in_count){
        this.count=in_count;
    }
    
    getCount(){
        return this.count;
    }

    incCount(){
        this.setCount(this.getCount()+1);
        return this.getCount();
    }

    resetCount(){
        this.setCount(0);
    }

    seekMax(inc_val){
        if (inc_val>this.getMax()){
            this.setMax(inc_val);
        }
        return this.getMax();
    }

    functionExist(pObject,name=""){
        if(typeof pObject === name){
            return true;
        }else{
            return false;
        }
    }
    prototypeOf(pOject,name){
        let result;
        result=pOject.isPrototypeOf(name);
        return result;
    }
    isObject(obj) {
  		return obj === Object(obj);
    }

    isInstanteOf(pObjet,clasObject){
		let result=false;
		if(pObjet instanceof clasObject) result=true;
		return result; 
	}
    
    
}