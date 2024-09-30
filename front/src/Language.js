import Dropdown from 'react-bootstrap/Dropdown';
import './index.css';
function Language() {
  return (
    <Dropdown>
      <Dropdown.Toggle id="dropdown-basic" className="drp">
        Language
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item href="#/action-1">English</Dropdown.Item>
        <Dropdown.Item href="#/action-2">Hindi</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Marathi</Dropdown.Item>
        <Dropdown.Item href="#/action-4">Gujarati</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
}

export default Language;