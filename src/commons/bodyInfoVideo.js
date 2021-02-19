import { useState } from 'react';
import VideoModal from './videoModal';


const BodyInfoVideo = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <section className="bodyContents-section my-3 pb-5 5 wow fadeInUp" data-wow-delay="0.1s">
        <div className="container">
          <a onClick={() => setShowModal(true)} data-youtube-id="Zmc49Ei_UkA" className="videoThumbnail -stretched video-banner js-trigger-video-modal">
            <img className="videoPlay" src="/assets/images/icon-video-play.svg" alt="" />
          </a>
        </div>
      </section>
      {showModal && <VideoModal onHide={() => setShowModal(false)} />}
    </>
  );
};

export default BodyInfoVideo;
