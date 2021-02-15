import { Button, Modal } from 'react-bootstrap';
import PropTypes from 'prop-types';


const ConfirmModal = ({ title, message, onClose, onSave, backdrop, keyboard }) => {
  return (
    <Modal show backdrop={backdrop} keyboard={keyboard}>
      <Modal.Header>
        <Modal.Title>{title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>{message}</p>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="danger" onClick={onClose}>Cancel</Button>
        <Button variant="success" onClick={onSave}>Save Changes</Button>
      </Modal.Footer>
    </Modal>
  );
};

ConfirmModal.defaultProps = {
  backdrop: "static",
  keyboard: false
};

ConfirmModal.propTypes = {
  backdrop: PropTypes.string,
  keyboard: PropTypes.bool
};

export default ConfirmModal;
