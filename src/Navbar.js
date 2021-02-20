import { memo, useEffect } from "react";
import ReactDOM from 'react-dom';
import { Container, Nav, Navbar, NavDropdown } from "react-bootstrap";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";


const NavBar = () => {
  let el = document.createElement('div');
  const entities = useSelector(({ businessUnit }) => businessUnit);
  const env = useSelector(({ env }) => env);
  let isLoggedIn = false;
  let parentElem = document.body;

  window.onscroll = () => addSticky();

  useEffect(() => {
    parentElem.appendChild(el);
    return () => {
      parentElem.removeChild(el);
    };
  });

  const addSticky = () => {
    if (!el) return;
    if (window.pageYOffset) {
      el.classList.add("sticky");
    } else {
      el.classList.remove("sticky");
    }
  };

  const logout = () => {
    console.log('Log out!');
  };

  return env.client_code ? ReactDOM.createPortal(
    <Navbar expand="lg" fixed="top" className="wow fadeInUp" data-wow-delay="0s">
      <Container>
        <div className="col-6 d-flex col-lg-3 px-0">
          <Navbar.Brand>
            <img id="navbar-brand" src="/assets/images/ayala/ayala-label-logo.svg" alt="" className="d-inline-block align-middle" style={{ 'width': '178px' }} />
          </Navbar.Brand>
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
          :
          <div className="col text-right d-lg-none">
            <Link to="/signin" className="btn mr-1">Sign In</Link>
            <Link to="/register" className="btn btn-outline-secondary">Register</Link>
          </div>
        }
        <div className="w-auto ml-3 d-flex p-0 justify-content-end d-lg-none">
          <Navbar.Toggle aria-controls="basic-navbar-nav" className="p-0" children={
            <>
              <span className="icon-bar bg-dark"></span>
              <span className="icon-bar bg-dark"></span>
              <span className="icon-bar bg-dark"></span>
            </>
          } />
        </div>
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Item>
              <Nav.Link as={Link} to="/">Home</Nav.Link>
            </Nav.Item>
            <NavDropdown title="About Us" id="basic-nav-dropdown">
              {entities.map(entity =>
                <NavDropdown.Item key={entity.businessunit_code} as={Link} to={`${ entity.businessunit_code.toLowerCase() }`}>
                  {entity.businessunit_name}
                </NavDropdown.Item>
              )}
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
            :
            <>
              <Link className="btn text-dark d-none d-lg-inline mr-1" to="/signin">Sign In</Link>
              <Link className="btn btn-outline-secondary d-none d-lg-inline mr-1" to="/register">Register</Link>
            </>
          }
        </Navbar.Collapse>
      </Container>
    </Navbar>,
    el
  ) : null;
};

export default memo(NavBar);
