import { Button, Modal } from 'react-bootstrap';
import PropTypes from 'prop-types';


const VideoModal = ({ onHide }) => {
  return (
    <Modal show onHide={onHide} size="lg">
      <Modal.Body className="p-0" style={{ 'marginBottom': '-8px' }}>
        <iframe id="iframeYoutube" width="100%" height="400px" allow="autoplay" src="https://www.youtube.com/embed/HpsrwIVSzbY?autoplay=1" frameBorder="0" allowFullScreen></iframe>
      </Modal.Body>
    </Modal>
  );
};

export default VideoModal;
