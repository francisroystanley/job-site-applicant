import { memo, useContext, useEffect } from "react";
import ReactDOM from 'react-dom';
import { Container, Nav, Navbar, NavDropdown } from "react-bootstrap";
import { Link } from "react-router-dom";
import { createSelector } from "reselect";
import { useSelector } from "react-redux";

import sm from './assets/images/sm/logo.png';
import goldilocks from './assets/images/goldilocks/logo.png';
import talentmatch from './assets/images/talentmatch/logo.png';
import titanium from './assets/images/titanium/logo.png';
import wilcon from './assets/images/sm/logo.png';


// const stateSelector = createSelector(getBusinessUnit, state => state);

const NavBar = () => {
  let el = document.createElement('div');
  const entities = [];
  // const entities = useSelector(stateSelector);
  // const entities = useContext(BusinessUnit);
  const env = process.env;
  const client_code = env.REACT_APP_CLIENT_CODE;
  let isLoggedIn = false;
  const Logos = {
    sm,
    goldilocks,
    talentmatch,
    titanium,
    wilcon
  };
  let parentElem = document.body;
  window.onscroll = () => addSticky();

  useEffect(() => {
    parentElem.appendChild(el);
    return () => {
      parentElem.removeChild(el);
    };
  });

  const addSticky = () => {
    if (window.pageYOffset) {
      el.classList.add("sticky");
    } else {
      el.classList.remove("sticky");
    }
  };

  const logout = () => {
    console.log('Log out!');
  };

  return ReactDOM.createPortal(
    <Navbar expand="lg" fixed="top" className="wow fadeInUp" data-wow-delay="0s">
      <Container>
        <div className="col-2 col-lg-3 px-0">
          <Navbar.Brand
          // ui-sref="home"
          ><img id="navbar-brand" src={Logos[client_code.toLowerCase()]} alt="" className="d-inline-block align-middle" style={{ 'width': client_code == 'TITANIUM' ? '40vw !important' : '' }} /></Navbar.Brand>
        </div>
        {isLoggedIn ?
          <div className="col d-lg-none d-flex px-0 justify-content-end">
            <NavDropdown className="white-md" title={<span className="navdropdown-name">HI, KRISH
              {/* {[user_info['person']['firstname']]} */}
            </span>} id="basic-nav-dropdown" alignRight>
              <NavDropdown.Item
              // ui-sref="myaccount"
              >My Account</NavDropdown.Item>
              <NavDropdown.Item
              // ui-sref="myaccount.changepassword"
              >Change Password</NavDropdown.Item>
              <NavDropdown.Item href="" onClick={logout}
              >Logout</NavDropdown.Item>
            </NavDropdown>
          </div>
          : ['SM', 'TALENTMATCH'].includes(client_code) &&
          <div className="col text-right d-lg-none">
            <a
              // ui-sref="signin"
              className="btn mr-1">Sign In</a>
            <a
              // ui-sref="register"
              className="btn btn-outline-light">Register</a>
          </div>
        }
        <div className="w-auto ml-3 d-flex p-0 justify-content-end d-lg-none">
          <Navbar.Toggle aria-controls="basic-navbar-nav" className="p-0" children={
            <>
              <span className="icon-bar bg-white"></span>
              <span className="icon-bar bg-white"></span>
              <span className="icon-bar bg-white"></span>
            </>
          } />
        </div>
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Item>
              <Nav.Link as={Link} to="/">Home</Nav.Link>
            </Nav.Item>
            <NavDropdown title="About Us" id="basic-nav-dropdown">
              {client_code == 'SM' ?
                entities.map(entity =>
                  // ui-sref="landingpage_{{entity.code}}"
                  <NavDropdown.Item key={entity.businessunit_code} href="">{entity.businessunit_name}</NavDropdown.Item>
                )
                :
                entities.map(entity =>
                  // ui-sref="landingpage({businessunit_code: entity.code})"
                  <NavDropdown.Item key={entity.businessunit_code} href="">{entity.businessunit_name}</NavDropdown.Item>
                )
              }
            </NavDropdown>
            <Nav.Item>
              <Nav.Link as={Link} to="/career">Careers</Nav.Link>
            </Nav.Item>
          </Nav>
          {isLoggedIn ?
            <NavDropdown className="white" title={<span className="navdropdown-name">HI, KRISH
              {/* {[user_info['person']['firstname']]} */}
            </span>} id="basic-nav-dropdown" alignRight>
              <NavDropdown.Item
              // ui-sref="myaccount"
              >My Account</NavDropdown.Item>
              <NavDropdown.Item
              // ui-sref="myaccount.changepassword"
              >Change Password</NavDropdown.Item>
              <NavDropdown.Item href="" onClick={logout}
              >Logout</NavDropdown.Item>
            </NavDropdown>
            : ['SM', 'TALENTMATCH'].includes(client_code) &&
            <>
              <a
                // ui-sref="signin"
                className="btn d-none d-lg-inline">Sign In</a>
              <a
                // ui-sref="register"
                className="btn btn-outline-light d-none d-lg-inline">Register</a>
            </>
          }
        </Navbar.Collapse>
      </Container>
    </Navbar>,
    el
  );
};

export default memo(NavBar);
