import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import './index.css';
import submit from './back.png';

function Input({clear, changeCss}) {
  return (
    <>
    <div className='input-grp'>
      <InputGroup className='grp'>
        <Form.Control onFocus={changeCss} className="mb-3 input"
          placeholder="Ask a question"
          aria-label="Recipient's username"
          aria-describedby="basic-addon2"
        />
        <Button variant="outline-secondary" id="button-addon2 sub">
          <img onClick={clear}  src={submit} className="submit"></img>
        </Button>
      </InputGroup>
    </div>
    </>
  );
}

export default Input;