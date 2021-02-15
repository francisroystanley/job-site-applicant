import { Modal } from 'react-bootstrap';
import PropTypes from 'prop-types';


const VideoModal = ({ onHide }) => {
  return (
    <Modal show onHide={onHide} size="lg">
      <div className="modal-body video-modal" id="modal-body">
        <iframe id="iframeYoutube" width="100%" height="400px" allow="autoplay;" src="https://www.youtube.com/embed/Zmc49Ei_UkA?autoplay=1" frameBorder="0" allowFullScreen></iframe>
      </div>
    </Modal>
  );
};

export default VideoModal;
