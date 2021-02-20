import { Link } from "react-router-dom";

const TermsCondition = () => {
  window.scrollTo(0, 0);

  return (
    <>
      <div className="bodyContents pt-0">
        <section className="bodyContents-section -bg-light">
          <div className="container">
            <h3 className="text-center" style={{ 'padding': '30px' }}>Terms and Condition</h3>
            <div>
              <b>Agreement to terms</b>
              <p>Welcome to this website hosted by <b>Ayala Careers</b> (we, our, us). When we use the terms you and your, we are referring to any organization or person who accesses the website. By accessing and using this site, you are agreeing to be bound by these terms of use and our privacy statement.</p>

              <b>We Are Committed to Your Privacy</b>
              <p>Ayala Careers Website is committed to protecting your privacy. This privacy statement sets forth our current privacy practices with regard to the information we collect when you or your computer interact with our website. By accessing ayala.careerfinder.online, you acknowledge and fully understand Ayala's privacy statement and freely consent to the information collection and use practices described in the privacy statement (see <Link to="/privacy_policy">Ayala’s Privacy Policy</Link>).</p>

              <b>Changes</b>
              <p>We may change our terms of use and copyright and our privacy statement at any time. If we consider that these changes are significant, we will provide you with notice of such changes, whether on this site or by email. You accept that notice of a change on this site is sufficient notice to you. Your continued use of the site after such changes means you consent to those changes.</p>

              <b>Accuracy of your information</b>
              <p>You must provide true and current information in your dealings with us, including setting up an account. We recommend using a personal email address for your account to ensure continued access.</p>

              <b>Account security - your responsibilities</b>
              <p className="mb-0">If you register for an account to gain access to certain parts of the site, we will provide you with a username and password. You are responsible for:</p>
              <ul className="custom-ul">
                <li>Keeping your username and password confidential;</li>
                <li>Protecting and securing your username and password from unauthorized access and use; and</li>
                <li>Protecting your computing environment from unauthorized access, viruses and malicious software.</li>
              </ul>
              <p>Your username and password are personal to you. You are not permitted to share them with others. We may suspend or disable your username and password if we consider it necessary for security reasons or if you breach these terms.</p>

              <b className="d-block mb-3">Copyright</b>
              <b>Your content</b>
              <p className="mb-0">If you add content to this site, you must have all the rights you need to add that content and to ensure that our use of that content in accordance with these terms will not:</p>
              <ul className="custom-ul">
                <li>Breach any laws or legally binding codes;</li>
                <li>Infringe any person's intellectual property rights or other legal rights or protected interests; or</li>
                <li>Give rise to any legal cause of action against us or you or any third party.</li>
              </ul>
              <p>If we suspect that you have breached these requirements, we may remove, suspend, amend or delete the relevant content. We do not claim ownership of your content but you grant us a non-exclusive, irrevocable license to process, store, copy, reformat, publish and otherwise use that content for recruitment, reporting, and other purposes required in operating this site and exercising our rights under these terms.</p>

              <b>Our content and your use of it</b>
              <p>Except for your content, and unless otherwise indicated, we or our licensors are the owners of the intellectual property rights in this site and the content on this site. You may not use our intellectual property rights and content unless authorized to do so under these terms or by us in writing and without obtaining our specific permission.</p>
              <p className="mb-0">You must also not:</p>
              <ul className="custom-ul">
                <li>Sell or distribute any material on a commercial basis</li>
                <li>Alter any material or use it in a misleading manner</li>
                <li>Alter, use or distribute any third party copyright material in any manner that would infringe copyright in that material.</li>
              </ul>
              <p>In addition, the license above does not apply to the website’s design elements or to any government or other organization’s emblems or logos. These elements, emblems and logos may not be reproduced without our written consent.</p>

              <b>Third party content</b>
              <p>Where copyright material is owned by a third party, which will be indicated. You may not do anything with material owned by a third party that would breach their intellectual property rights.</p>

              <b>Indemnity</b>
              <p>You agree to indemnify us for any loss or costs we incur due to your breaching these terms of use. This clause does not apply to Government agencies, entities, and their staff.</p>

              <b>Publishing content</b>
              <p className="mb-0">The content on this website is continually updated to ensure our information and advice reflects current careers and employment practices and trends. For this reason, we recommend you link to our website to ensure you are getting the most up-to-date version of our content.</p>
              <p>We make a lot of our job and industry information available for use via a free API (application program interface).</p>

              <b>Find out more about our Terms and Conditions</b>
              <p>For all queries about our website, including an intent to publish or issue material from our publications or website for commercial use, you must first get written permission from us by sending an email to our Support Team at <a href="mailto:support@ayalacareers.com">support@ayalacareers.com</a>.</p>

              <b>Disclaimer</b>
              <p>The Ayala Careers website is designed to help you make better informed work, training and career decisions. However, we recommend you also refer to other sources of information such as relevant training providers, or professional or trade organizations before making any decisions about your career.</p>
              <p>Although Ayala Careers makes every effort to ensure all material on our website is reliable and accurate at the time of publishing, we cannot accept any liability for its accuracy or content. Use of our website is at your own risk.</p>

              <b>Linking policy</b>
              <p>Ayala Careers provides links to other websites when we think you may be interested in what they offer. We do not necessarily endorse those websites or their content, and we have no control over the conduct of the companies or organizations operating those websites.</p>

              <b>Changes to the website</b>
              <p>Ayala Careers may change, suspend or discontinue any aspect of the website at any time, including any service or content offered by or through this website.</p>

              <b>Feedback</b>
              <p>We value your comments and opinions. If you have comments, questions or complaints about any of our services or website policies please contact <a href="mailto:support@ayalacareers.com">support@ayalacareers.com</a>.</p>
            </div>
          </div>
        </section>
      </div>
      <div className="push"></div>
    </>
  );
};

export default TermsCondition;
