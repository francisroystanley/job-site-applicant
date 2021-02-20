import { Link } from "react-router-dom";


const LegitimatePurpose = () => {
  window.scrollTo(0, 0);

  return (
    <>
      <div className="bodyContents pt-0">
        <section className="bodyContents-section -bg-light">
          <div className="container">
            <h3 className="text-center" style={{ 'padding': '30px' }}>Legitimate Purpose for requesting Personal Information</h3>
            <div className="legitimate_purpose">
              <h5>Why Ayala asks for certain info to create your Ayala Careers account</h5>
              <p>When you create an Ayala Careers account, we ask for some personal information. This information helps keep your account secure and makes our services more useful.</p>
              <p>To learn more about how we use this info, read the <Link to="/privacy_policy">Ayala Privacy Policy</Link>.</p>
            </div>
            <div className="legitimate_purpose">
              <h5>What we ask for</h5>
              <h5 className="text-decoration-none">Name</h5>
              <p>Enter the name you want to use on Ayala Careers website. When you apply for a job, the Hiring Managers will know how to address you properly.</p>
              <h5 className="text-decoration-none">E-mail</h5>
              <p>Use your own e-mail account that you will use to sign in, like <span style={{ 'textDecoration': 'underline' }}>myname@email.com</span>. We can also contact you for the latest job openings with your email address.</p>
              <h5 className="text-decoration-none">Password</h5>
              <p className="mb-0">To help keep your account safe, choose a strong password that is at least eight (8) characters long:</p>
              <ul style={{ 'color': 'rgba(0, 0, 0, 0.6)' }}>
                <li>Mix of letters (lower and upper cases), numbers, and symbols.</li>
                <li>Avoid personal information or common words that are easy to guess, like your favorite color or mother’s name.</li>
                <li>Do not use a password you have used for other accounts or websites. Likewise, do not use this password anywhere else.</li>
              </ul>
              <h5 className="text-decoration-none">Phone Number</h5>
              <p>If you have a mobile phone, this info is optional but highly recommended. Depending on how you add a phone number to your account, your number can be used to help us reach out to you regarding your job applications.</p>
              <h5 className="text-decoration-none">Ability to update your information later</h5>
              <p>After you create an Ayala Careers Account, you can change some of this information and control who sees it. You may change or update this by going to your “My Profile.”</p>
              <h5 className="text-decoration-none">Ability to opt out or delete your Ayala Careers account</h5>
              <p>You have the option to unsubscribe from the website updates by clicking on “Unsubscribe” via “My Profile” or you may send an email to our Customer Care department for the removal of your Personal Information from our database.</p>
            </div>
          </div>
        </section>
      </div>
      <div className="push"></div>
    </>
  );
};

export default LegitimatePurpose;
