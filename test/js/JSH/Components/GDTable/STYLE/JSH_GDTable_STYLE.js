
class JSH_GDTable_STYLE {

  getStrIniClass(classname) {
    return `.${classname} { `;
  }

  getStrEndClass(classname) {
    return "}";
  }

  getStrDisplayType() {
    return "display: grid;";
  }
  getStrGridGap(value) {
    return `grid-gap: ${value}; `;
  }

  getStrGridTempCols(value) {
    return "grid-template-columns: repeat(" + value + ",1fr);";
  }
  getStrGridTempRows(value) {
    return "grid-template-rows: repeat(" + value + ",1fr);";
  }
  /*
    .contenedor {
        display: grid;
        grid-gap: 20px;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(4, 1fr);
    }
    */
  /*
   
   */

  /*   
    .contenedor .item {
  background: #ff8000;

  grid-column: span 3;
    grid-row: 3 / span 2;
    }
    */

  getStrBackColor(value) {
    return "background: " + value + "; ";
  }

  getStrGridSpanCols(start, count) {
    return "grid-column: " + start + " / span " + count + "; ";
  }

  getStrGridSpanRows(start, count) {
    return "grid-row: " + start + " / span " + count + "; ";
  }
}
