import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';
import Headd from './Headd.js';
import Language from './Language.js';
import logo from './logo.png';
import Input from './Input.js';
import Option1 from './Option1.js';
import Response from './response.jsx';
import Background from './background.jpg';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid'; //to set unique ids

function App() {
  const [showResponse, setShowResponse] = useState(false);
  const [responseQuery, setresponseQuery] = useState([{}])


  function changeCss(){
    let text = document.getElementsByClassName('txt');
    for (let i = 0; i < text.length; i++) {
      text[i].innerHTML = '';
    }
    let pic = document.getElementsByClassName('logo');
    if (pic.length > 0) {
        pic[0].style.position = 'absolute'; 
        pic[0].style.top = '0';   
        pic[0].style.left = '160px';   
        pic[0].style.width = '100px';
    }
    const inputGrp = document.querySelector('.input-grp');
if (inputGrp) {
  inputGrp.style.position = 'fixed';
  inputGrp.style.bottom = '50px'; 
  inputGrp.style.left = '0';      
  inputGrp.style.right = '0'; 
  inputGrp.style.padding = '0 50px'; 
  
  inputGrp.style.border = 'none'; 
  inputGrp.style.boxShadow = 'none'; 
  inputGrp.style.maxWidth = '100%'; 
  

}


  let optionElements = document.getElementsByClassName('options');
    for (let i = 0; i < optionElements.length; i++) {
      optionElements[i].style.display = 'none';
    }
}


  
  async function clear() {

    var text;
    var response;

    // Set the state to show the Response component
    let elements = document.getElementsByClassName('input');
    if (elements.length > 0) {
      let inputElement = elements[0]; 
      text=inputElement.value
      //axios request to node server
    try {
      response = await axios.post('http://127.0.0.1:5000/ask_question', {
        question: text,
        language: "English" // Use the appropriate language
      });
      setresponseQuery(responseQuery.concat({id: uuidv4(), query: text, response: response.data.answer }));
      setShowResponse(true);
    } catch (error) {
      console.error("There was an error making the request:", error);
    }

  }
}

  function autofill(text) {
    let elements = document.getElementsByClassName('input');
    if (elements.length > 0) {
      let inputElement = elements[0]; // Assuming there is only one element with this class
      inputElement.value = text; // Set the value of the first element
      changeCss();
      clear()
    }
  }

  let text1 = 'What Services does the Department of Justice offer?';
  let text2 = 'How do I report a crime to the DOJ?';
  let text3 = 'What is the DOJ doing to combat human trafficking?';

  return (
    <React.StrictMode>
      <Container fluid>
        <Row className="roww">
          <Col><Headd /></Col>
          <Col className='drop'><Language /></Col>
        </Row>
        {showResponse && <Response responseQuery={responseQuery} />}
        <Row className='name_logo'>
          <Col>
            <div><img src={logo} className='logo' /></div>
          </Col>
          <Col>
            <Row className='txt' id="txt1">DOJ</Row>
            <Row className='txt' id="txt2">ChatBot</Row>
          </Col>
        </Row>
      </Container>
      <Container>
        <Row>
          <Input className='input-grp' id="inp" clear={clear} changeCss={changeCss} />
        </Row>
        <Row>
          <Col><Option1 autofill={autofill} text={text1} /></Col>
          <Col><Option1 autofill={autofill} text={text2} /></Col>
          <Col><Option1 autofill={autofill} text={text3} /></Col>
        </Row>
      </Container>
    </React.StrictMode>
  );
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

reportWebVitals();
