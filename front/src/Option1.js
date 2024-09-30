function Option1({autofill,text}) {
    
    return (
      <div className='options descriptionText' id="op1" onClick={()=>{autofill(text)}}>{text}</div>
    );
}
export default Option1;