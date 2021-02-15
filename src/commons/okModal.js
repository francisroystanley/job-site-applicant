import { Button, Modal } from 'react-bootstrap';
import PropTypes from 'prop-types';


const OkModal = ({ title, message, onClose, backdrop, keyboard }) => {
  return (
    <Modal show onExited={onClose} backdrop={backdrop} keyboard={keyboard}>
      <Modal.Header>
        <Modal.Title>{title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>{message}</p>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="primary" onClick={onClose}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
};

OkModal.defaultProps = {
  backdrop: "static",
  keyboard: false
};

OkModal.propTypes = {
  backdrop: PropTypes.string,
  keyboard: PropTypes.bool
};

export default OkModal;
