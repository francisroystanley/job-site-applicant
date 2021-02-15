import { memo, useEffect } from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';


const BlockUI = ({ elem, message }) => {
  let parentElem = elem.current;
  let el = document.createElement('div');
  el.className = 'block-ui-container';

  useEffect(() => {
    parentElem.classList.add('block-ui', 'block-ui-anim-fade', 'block-ui-active', 'block-ui-visible');
    parentElem.appendChild(el);
    return () => {
      parentElem.classList.remove('block-ui-active', 'block-ui-visible');
      parentElem.removeChild(el);
    };
  });

  return ReactDOM.createPortal(
    <>
      <div className="block-ui-overlay"></div>
      <div className="block-ui-message-container">
        <div className="block-ui-message">{message}</div>
      </div>
    </>,
    el,
  );
};

BlockUI.propTypes = {
  elem: PropTypes.shape({ current: PropTypes.instanceOf(Element) }),
  message: PropTypes.string
};

BlockUI.defaultProps = {
  elem: { current: document.body },
  message: "Loading ..."
};

export default memo(BlockUI);
