#importing requied library
import requests
import re
from bs4 import BeautifulSoup
import json

#raw HTML content
html_content = """
<html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN">
  <head></head>
  <body data-new-gr-c-s-check-loaded="14.1156.0" data-gr-ext-installed="">
    <div id="twoseven-scripts" data-info="Scripts added by TwoSeven extension" style="display: none !important; position: static !important; top: 0px !important; left: 0px !important; width: 0px !important; height: 0px !important;"></div>
    <meta http-equiv="origin-trial" content="Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <link rel="icon" href="//static.naukimg.com/s/7/112/favicon.ico">
    <link rel="preconnect" href="https://static.naukimg.com">
    <link rel="dns-prefetch" href="https://static.naukimg.com">
    <link rel="preload" as="style" href="//static.naukimg.com/s/7/112/c/resdex_app.1251c2a5.css">
    <link rel="preload" as="style" href="//static.naukimg.com/s/7/112/c/common_resdex_app.d30cddc4.css">
    <title>Sakib Ali - 4 Year(s) 1 Month(s)</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="theme-color" content="#000000">
    <meta name="Resdex" content="Resdex">
    <title>Resdex</title>
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/resdex_app.1251c2a5.css" media="all">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/common_resdex_app.d30cddc4.css" media="all">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/6479.f7ab9148.css" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/557.7e59eef3.css" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/7108.86365da6.css" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/5087.1ddde256.css" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/112/c/CvPreview.eb8a447e.css" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/102/c/gnb_modal_listener.af2e3414.css" crossorigin="anonymous">
    <link href="chrome-extension://cjdnfmjmdligcpfcekfmenlhiopehjkd/web_resources/modal/modal.css" rel="stylesheet" id="__tmpStyle">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/102/c/gnb_recruiter_chat.8a337f94.css" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="//static.naukimg.com/s/7/102/c/gnb_notification.0ab96fcf.css" crossorigin="anonymous">
    <link href="//static.naukimg.com/s/7/0/j/naukri-widget_v12.14-modern.min.js" rel="preload" as="script">
    <style>
      .naukri-wdgt-shimmer {
        height: 100%;
        margin: 15px 0px;
        width: 100%
      }

      .naukri-wdgt-shimmer .header-shimmer {
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        border-radius: 4px;
        background: white;
        padding: 24px
      }

      .naukri-wdgt-shimmer .shimmer-cont {
        margin-top: 30px
      }

      .naukri-wdgt-shimmer .animated-background {
        -webkit-animation-duration: 1s;
        animation-duration: 1s;
        -webkit-animation-fill-mode: forwards;
        animation-fill-mode: forwards;
        -webkit-animation-iteration-count: infinite;
        animation-iteration-count: infinite;
        -webkit-animation-name: placeHolderShimmer;
        animation-name: placeHolderShimmer;
        -webkit-animation-timing-function: linear;
        animation-timing-function: linear;
        background: #f6f7f8;
        background: -webkit-gradient(linear, left top, right top, color-stop(8%, #f4f5f7), color-stop(18%, #e5e5e5), color-stop(33%, #f4f5f7));
        background: linear-gradient(to right, #f4f5f7 8%, #e5e5e5 18%, #f4f5f7 33%);
        background-size: 800px 104px;
        position: relative;
        height: 14px;
        border-radius: 7px
      }

      .naukri-wdgt-shimmer .animated-background:first-of-type {
        width: 85%
      }

      .naukri-wdgt-shimmer .animated-background:nth-of-type(2n) {
        width: 70%;
        margin-top: 10px
      }

      .naukri-wdgt-shimmer .animated-background:nth-of-type(3n) {
        width: 70%;
        margin-top: 10px
      }

      @-webkit-keyframes placeHolderShimmer {
        0% {
          background-position: -200px 0
        }

        100% {
          background-position: 468px 0
        }
      }

      @keyframes placeHolderShimmer {
        0% {
          background-position: -200px 0
        }

        100% {
          background-position: 468px 0
        }
      }
    </style>
    <style>
      .naukri-wdgt {
        min-width: 50px;
        min-height: 50px;
        width: 100%;
        overflow-x: auto;
        overflow-y: hidden
      }

      .naukri-wdgt .wdgt-track-view {
        line-height: 1px;
        height: 1px
      }

      .naukri-html-wdgt {
        overflow-x: auto;
        overflow-y: hidden;
        width: 100%
      }

      .naukri-js-wdgt {
        background-color: #ffffff;
        border-radius: 4px;
        -webkit-box-shadow: 0 1px 4px 0 rgba(0, 106, 194, 0.2);
        box-shadow: 0 1px 4px 0 rgba(0, 106, 194, 0.2);
        margin: 0px 0px 10px 0px;
        padding: 0px 24px;
        -webkit-box-sizing: border-box;
        box-sizing: border-box
      }

      .naukri-js-wdgt * {
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        padding: 0px;
        margin: 0px;
        word-break: break-word
      }

      .naukri-js-wdgt ul {
        list-style: none
      }

      .naukri-js-wdgt ul li {
        list-style-type: none
      }

      .naukri-js-wdgt a,
      .naukri-js-wdgt a:hover,
      .naukri-js-wdgt a:visited,
      .naukri-js-wdgt a:focus {
        text-decoration: none
      }

      #document-section-widgets .naukri-wdgt {
        min-width: auto !important;
        min-height: auto !important;
        width: 0 !important;
        height: 0 !important
      }

      .wdgt-overlay-container {
        position: fixed;
        z-index: 999999
      }

      .wdgt-overlay-container.wdgt-overlay-top-left {
        top: 100px;
        left: 36px
      }

      .wdgt-overlay-container.wdgt-overlay-bottom-left {
        bottom: 100px;
        left: 36px
      }

      .wdgt-overlay-container.wdgt-overlay-bottom-right {
        bottom: 100px;
        right: 36px
      }

      .wdgt-overlay-container.wdgt-overlay-top-right {
        top: 100px;
        right: 36px
      }

      .wdgt-overlay-container .wdgt-overlay-inventory {
        margin-bottom: 10px
      }

      .wdgt-overlay-container .wdgt-overlay-inventory:last-child {
        margin-bottom: 0
      }

      @media only screen and (max-width: 668px) {

        .wdgt-overlay-container.wdgt-overlay-bottom-left,
        .wdgt-overlay-container.wdgt-overlay-bottom-right {
          right: 36px;
          bottom: 100px;
          left: 36px
        }

        .wdgt-overlay-container.wdgt-overlay-top-right,
        .wdgt-overlay-container.wdgt-overlay-top-left {
          left: 36px;
          top: 100px;
          right: 36px
        }
      }
    </style>
    <div class="headGNBWrap">
      <div class="gnb_app_header">
        <div class="iYqiL" style="background-color: rgb(255, 255, 255);">
          <div class="qSSbv">
            <div class="HjuAK">
              <a href="//recruit.naukri.com/homePage/index">
                <div class="bJw_J l1s4P"></div>
              </a>
              <div class="tv8bL">
                <div class="N1vWk ">
                  <div class="bJfsh">
                    <div class="xzaIN">Jobs &amp; Responses</div>
                  </div>
                  <div class="Z851_ ">
                    <a class="I3sTS " href="//hiring.naukri.com/hiring/job/h">Post a Hot Vacancy</a>
                    <a class="I3sTS " href="//hiring.naukri.com/hiring/job/c">Post a Classified</a>
                    <a class="I3sTS " href="//hiring.naukri.com/hiring/job/i">Post an Internship</a>
                    <a class="I3sTS " href="//hiring.naukri.com/hiring/job/p">Post a Private Job</a>
                    <a class="I3sTS " href="//hiring.naukri.com/hiring/job-listing">Manage Jobs</a>
                  </div>
                </div>
                <div class="N1vWk ">
                  <div class="bJfsh">
                    <div class="xzaIN">Resdex</div>
                    <div class="active-widget" style="background-color: rgb(245, 107, 109);"></div>
                  </div>
                  <div class="Z851_ ">
                    <a class="I3sTS " href="//resdex.naukri.com/v3">Search Resumes</a>
                    <a class="I3sTS " href="//resdex.naukri.com/v3/search/savedSearches">Manage Searches</a>
                    <a class="I3sTS " href="//resdex.naukri.com/v3/folder/list">Folders</a>
                    <a class="I3sTS " href="//resdex.naukri.com/v3/hiringFor/list">Resdex Requirements</a>
                    <a class="I3sTS " href="//resdex.naukri.com/v2/mailCenter/mails?mailType=rmjMails">Mail Center</a>
                    <a class="I3sTS " href="//resdex.naukri.com/ManageTemplates/listTemplates">Email Templates</a>
                  </div>
                </div>
                <div class="N1vWk ">
                  <div class="bJfsh">
                    <div class="xzaIN">Analytics</div>
                  </div>
                  <div class="Z851_ ">
                    <a class="I3sTS " href="//posting.naukri.com/MIS/mis">Job Posting</a>
                    <a class="I3sTS " href="//resdex.naukri.com/mis/usageMis">Resdex</a>
                    <a class="I3sTS " href="//posting.naukri.com/nfl/nflReport">NFL Report</a>
                    <a class="I3sTS " href="//resdex.naukri.com/instaMIS/selectDate">Mobile Solutions</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="Gk5tL">
              <div class="fehet ">
                <div class="Iy_Bg">
                  <svg class="themed-icon" width="20" height="20" viewBox="0 0 20 20" fill="hsl(218deg 25% 35%)" xmlns="http://www.w3.org/2000/svg">
                    <path d="M11.25 2.5C7.10833 2.5 3.75 5.85833 3.75 10H1.25L4.49167 13.2417L4.55 13.3583L7.91667 10H5.41667C5.41667 6.775 8.025 4.16667 11.25 4.16667C14.475 4.16667 17.0833 6.775 17.0833 10C17.0833 13.225 14.475 15.8333 11.25 15.8333C9.64167 15.8333 8.18333 15.175 7.13333 14.1167L5.95 15.3C7.30833 16.6583 9.175 17.5 11.25 17.5C15.3917 17.5 18.75 14.1417 18.75 10C18.75 5.85833 15.3917 2.5 11.25 2.5ZM10.4167 6.66667V10.8333L13.9583 12.9333L14.6 11.8667L11.6667 10.125V6.66667H10.4167Z" fill="#42526E"></path>
                  </svg>
                  <div class="UJC3M" style="color: rgb(67, 83, 112);">Recent</div>
                </div>
                <div class="g19dS">
                  <div class="G7pbF">
                    <div class="XpWEq">
                      <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid" class="lds-ripple" style="background: 0px 0px;">
                        <circle cx="50" cy="50" r="4.719" fill="none" stroke="#1d3f72" stroke-width="2">
                          <animate attributeName="r" calcMode="spline" values="0;40" keyTimes="0;1" dur="3" keySplines="0 0.2 0.8 1" begin="-1.5s" repeatCount="indefinite"></animate>
                          <animate attributeName="opacity" calcMode="spline" values="1;0" keyTimes="0;1" dur="3" keySplines="0.2 0 0.8 1" begin="-1.5s" repeatCount="indefinite"></animate>
                        </circle>
                        <circle cx="50" cy="50" r="27.591" fill="none" stroke="#5699d2" stroke-width="2">
                          <animate attributeName="r" calcMode="spline" values="0;40" keyTimes="0;1" dur="3" keySplines="0 0.2 0.8 1" begin="0s" repeatCount="indefinite"></animate>
                          <animate attributeName="opacity" calcMode="spline" values="1;0" keyTimes="0;1" dur="3" keySplines="0.2 0 0.8 1" begin="0s" repeatCount="indefinite"></animate>
                        </circle>
                      </svg>
                    </div>
                  </div>
                </div>
              </div>
              <div class="Srkko" id="search_parent">
                <div class="TFWbH" style="border-color: rgb(219, 221, 230);"></div>
                <div class="yluSq " style="border-color: rgb(219, 221, 230);">
                  <div class="CAMFU" style="color: rgb(67, 83, 112);">Search</div>
                  <svg class="themed-icon" width="20" height="20" viewBox="0 0 20 20" fill="hsl(218deg 25% 35%)" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2583 11.6667H12.9167L17.075 15.8333L15.8333 17.075L11.6667 12.9167V12.2583L11.4417 12.025C10.4917 12.8417 9.25833 13.3333 7.91667 13.3333C4.925 13.3333 2.5 10.9083 2.5 7.91667C2.5 4.925 4.925 2.5 7.91667 2.5C10.9083 2.5 13.3333 4.925 13.3333 7.91667C13.3333 9.25833 12.8417 10.4917 12.025 11.4417L12.2583 11.6667ZM4.16667 7.91667C4.16667 9.99167 5.84167 11.6667 7.91667 11.6667C9.99167 11.6667 11.6667 9.99167 11.6667 7.91667C11.6667 5.84167 9.99167 4.16667 7.91667 4.16667C5.84167 4.16667 4.16667 5.84167 4.16667 7.91667Z" fill="#42526E"></path>
                  </svg>
                  <form>
                    <button type="button" class="jJK7z">
                      <div class="jNjm4"></div>
                    </button>
                  </form>
                </div>
                <div class="_teh1" style="background-color: rgb(255, 255, 255);"></div>
              </div>
              <div class="IAQ74" id="user_actions">
                <div class="r5T09">
                  <div class="ff2eP ">
                    <svg class="themed-icon" width="25" height="26" viewBox="0 0 25 26" fill="hsl(218deg 25% 35%)" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M7.29232 3.62598H17.709C18.8548 3.62598 19.7923 4.56348 19.7923 5.70931V22.376L12.5007 19.251L5.20898 22.376V5.70931C5.20898 4.56348 6.14648 3.62598 7.29232 3.62598ZM12.5007 16.9801L17.709 19.251V5.70931H7.29232V19.251L12.5007 16.9801Z" fill="#42526E"></path>
                    </svg>
                  </div>
                  <div class="sfl_parent ">
                    <div class="sfl_head">Profiles saved for later</div>
                    <div class="no_data">
                      <div class="illustration"></div>
                      <div class="text1">No profiles saved for later</div>
                      <div class="text2">Now you can save the candidates in Resdex for your reference. All such profiles will be stored here.</div>
                    </div>
                    <div class="sfl_close"></div>
                  </div>
                </div>
                <div class="r5T09">
                  <div class="ff2eP ">
                    <svg class="themed-icon" width="24" height="24" viewBox="0 0 24 24" fill="hsl(218deg 25% 35%)" xmlns="http://www.w3.org/2000/svg">
                      <path d="M17.3366 1.90625L21.9436 5.75125L20.6636 7.28625L16.0536 3.44325L17.3366 1.90625ZM6.66264 1.90625L7.94464 3.44225L3.33664 7.28625L2.05664 5.75025L6.66264 1.90625ZM11.9996 4.09625C7.02964 4.09625 2.99964 8.12625 2.99964 13.0963C2.99964 18.0662 7.02964 22.0963 11.9996 22.0963C16.9696 22.0963 20.9996 18.0662 20.9996 13.0963C20.9996 8.12625 16.9696 4.09625 11.9996 4.09625ZM11.9996 20.0963C8.13964 20.0963 4.99964 16.9563 4.99964 13.0963C4.99964 9.23625 8.13964 6.09625 11.9996 6.09625C15.8596 6.09625 18.9996 9.23625 18.9996 13.0963C18.9996 16.9563 15.8596 20.0963 11.9996 20.0963ZM12.9996 9.09625H10.9996V12.0963H7.99964V14.0963H10.9996V17.0963H12.9996V14.0963H15.9996V12.0963H12.9996V9.09625Z" fill="#A13A7E"></path>
                    </svg>
                  </div>
                  <div class="ArIEF "></div>
                  <div class="cC9Zg" id="gnb_reminders_parent"></div>
                </div>
                <div class="r5T09">
                  <div class="ff2eP ">
                    <svg class="themed-icon" width="24" height="24" viewBox="0 0 24 24" fill="hsl(218deg 25% 35%)" xmlns="http://www.w3.org/2000/svg">
                      <path d="M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM20 16H6L4 18V4H20V16Z" fill="#A13A7E"></path>
                    </svg>
                  </div>
                </div>
                <div class="r5T09">
                  <div class="ff2eP ">
                    <svg class="themed-icon" width="24" height="24" viewBox="0 0 24 24" fill="hsl(218deg 25% 35%)" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 21.75C13.1 21.75 14 20.85 14 19.75H10C10 20.85 10.9 21.75 12 21.75ZM18 15.75V10.75C18 7.68 16.37 5.11 13.5 4.43V3.75C13.5 2.92 12.83 2.25 12 2.25C11.17 2.25 10.5 2.92 10.5 3.75V4.43C7.64 5.11 6 7.67 6 10.75V15.75L4 17.75V18.75H20V17.75L18 15.75ZM16 16.75H8V10.75C8 8.27 9.51 6.25 12 6.25C14.49 6.25 16 8.27 16 10.75V16.75Z" fill="#A13A7E"></path>
                    </svg>
                  </div>
                  <div class="e7cSU "></div>
                </div>
              </div>
              <div class="Z3LpC" id="profile_parent">
                <div class="RqqrG">
                  <span class="gnbr-avatar gnbr-avatar-image gnbr-avatar-40">
                    <img src="https://naukrirecruiter.naukri.com/profilePic/getpic?pid=1580560609rp1758176_medium4" alt="recruiter profile" class=" " data-src="https://naukrirecruiter.naukri.com/profilePic/getpic?pid=1580560609rp1758176_medium4">
                    <span class="__badge undefined"></span>
                  </span>
                </div>
                <div class="XsvM4 ">
                  <div class="DXj9k">
                    <div class="RqqrG">
                      <span class="gnbr-avatar gnbr-avatar-image gnbr-avatar-56">
                        <img src="https://naukrirecruiter.naukri.com/profilePic/getpic?pid=1580560609rp1758176_medium4" alt="recruiter profile" class=" " data-src="https://naukrirecruiter.naukri.com/profilePic/getpic?pid=1580560609rp1758176_medium4">
                        <span class="__badge undefined"></span>
                      </span>
                    </div>
                    <div class="qStIV">
                      <div class="oe3fW">justcall1</div>
                      <div class="GofdI"></div>
                      <div class="GofdI"></div>
                      <div class="vx2JY">om@justcallindia.com</div>
                      <div class="HwXp7">91 9880011111</div>
                    </div>
                  </div>
                  <div class="tiTzt">
                    <div>
                      <div class="qGPuZ">
                        <div class="zcyqy ">
                          <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_settings"></i>
                        </div>
                        <div class="m6pBk ">
                          <div class="flgBn">Settings <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_arrow"></i>
                          </div>
                          <div class="uWI5D ">
                            <div class="CDmwG">
                              <a class="NcSAn" href="//recruit.naukri.com/homePage/productSettings">Product Settings</a>
                            </div>
                            <div class="CDmwG">
                              <a class="NcSAn" href="//rms.naukri.com/questionnaire/showList" target="_blank">Manage Questionnaires</a>
                            </div>
                            <div class="CDmwG">
                              <a class="NcSAn" href="//rms.naukri.com/mailTemplate/list" target="_blank">Apply Mail Templates</a>
                            </div>
                            <div class="CDmwG">
                              <a class="NcSAn" href="//recruit.naukri.com/company/password">Change Password</a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div>
                      <div class="qGPuZ">
                        <div class="zcyqy ">
                          <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_help"></i>
                        </div>
                        <div class="m6pBk ">
                          <div class="flgBn">Help <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_arrow"></i>
                          </div>
                          <div class="uWI5D ">
                            <div class="CDmwG">
                              <a class="NcSAn" href="https://www.naukri.com/faq/recruiter" target="_blank">FAQs</a>
                            </div>
                            <div class="CDmwG">
                              <a class="NcSAn" href="http://w5.naukri.com/fdbck/main/feedback.php?app_id=10" target="_blank">Report a Problem</a>
                            </div>
                            <div class="CDmwG">
                              <a class="NcSAn" href="//recruit.naukri.com/company/security" target="_blank">Usage Guidelines</a>
                            </div>
                            <div class="NcSAn">
                              <div class="y4S_a">Contact us on</div>
                              <div class="pZhA1">1800 102 5558</div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div>
                      <div class="qGPuZ">
                        <div class="zcyqy ">
                          <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_feedback"></i>
                        </div>
                        <a class="flgBn" href="javascript:void()">Give Feedback</a>
                      </div>
                      <div class="qpJkT"></div>
                    </div>
                    <div>
                      <div class="qGPuZ">
                        <div class="zcyqy ">
                          <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_logout"></i>
                        </div>
                        <a class="flgBn" href="//resdex.naukri.com/logout/resdex">Logout from Resdex</a>
                      </div>
                    </div>
                    <div>
                      <div class="qGPuZ">
                        <div class="zcyqy ">
                          <i class="ico ico-info profile-expand-link gnbr-icon gnbr-icon-profile_logout"></i>
                        </div>
                        <a class="flgBn" href="//resdex.naukri.com/logout/naukri">Logout from Naukri</a>
                      </div>
                    </div>
                  </div>
                  <div class="gdhqq"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="form-row p0 mb10 err dispN wrap" id="brwsMsg">
      <input type="hidden" rel="custom:1006|submit">
      <div class="msgBar yellow">
        <div id="commonErrBrw" class="erLbl cnt p0">
          <div class="cnt">It appears you're using an unsupported browser. <br> Old browsers can put your security at risk, slow you down or prevent you from using all Naukri features. To get the best of Naukri please upgrade to a <a href="http://www.naukri.com/tieups/tieups.php?othersrcp=29039">supported browser</a> (recommended). <br>
            <a href="http://www.naukri.com/tieups/tieups.php?othersrcp=29041">View list of new features not available in your current browser.</a>
          </div>
        </div>
      </div>
    </div>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="modalRoot"></div>
    <div id="rdxRoot">
      <div class="app">
        <div class="pages">
          <div>
            <div class="cv-preview">
              <div class="cv-prev-header ">
                <div class="cv-hd-container">
                  <div class="cv-hd-row">
                    <div class="hd-left">
                      <div class="bread-crumbs flex-row flex-aic">
                        <div class="bread-crumb flex-row flex-aic">
                          <i class="person_search ico-info naukri-icon naukri-icon-person_search"></i>
                          <a class="link int " href="/v3">
                            <div class="hd-link ellipsis" title="Advanced Search">Advanced Search</div>
                          </a>
                        </div>
                        <i class="ico ico-crumb naukri-icon naukri-icon-expand-more"></i>
                        <div class="bread-crumb flex-row flex-aic">
                          <a class="link int " href="/v3/search?sid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;flowId=2dad2395c7d750d0d79d3eb54e39926f">
                            <div class="hd-link ellipsis" title="521 profiles found">521 profiles found</div>
                          </a>
                        </div>
                        <i class="ico ico-crumb naukri-icon naukri-icon-expand-more"></i>
                        <div class="bread-crumb flex-row flex-aic">
                          <div class="hd-link ellipsis" title="Sakib Ali">
                            <div class="cv-name ellipsis" title="Sakib Ali">Sakib Ali</div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="hd-right">
                      <a target="_blank" href="preview/print?phoneStatus=true&amp;uniqId=b0a076519f571af25369e1f0e3f500e05c580c04431b0b475712440e595a0248415b420643470a555a51481b0915564552595a09594c1b081102156" class="link ext print rdx-action">
                        <i class="ico ico-info cv-print naukri-icon naukri-icon-print_icon"></i>
                        <span class="label">Print</span>
                      </a>
                      <div>
                        <button class="report-profile rdx-action naukri-btn-tertiary naukri-btn-x-small" type="button">
                          <i class="ico ico-flag naukri-icon naukri-icon-flag"></i>
                          <span class="label">Report profile</span>
                        </button>
                        <div id="report-profile-promo-section" class="naukri-wdgt-section">
                          <div id="report-profile-promo-section.inventory-1"></div>
                        </div>
                      </div>
                      <div class="navigation-wrapper">
                        <button class="prev-btn-wrapper disabled naukri-btn-tertiary naukri-btn-x-small" type="button">
                          <span class="prev-cv">
                            <i class="ico ico-expand naukri-icon naukri-icon-expand-more"></i>
                            <span class="label">Prev</span>
                          </span>
                        </button>
                        <button class="next-btn-wrapper  naukri-btn-tertiary naukri-btn-x-small" type="button">
                          <span class="next-cv">
                            <span class="label">Next</span>
                            <i class="ico ico-expand naukri-icon naukri-icon-expand-more"></i>
                          </span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="container ">
                <div class="observed scroll-observed"></div>
                <div class="actionbar-wrapper sticky-style ">
                  <div class="cv-action-bar">
                    <div class="dropdown-selected add-to-dd action-tuple rdx-action">
                      <i class="ico ico-info naukri-icon naukri-icon-note_add"></i>
                      <span class="label">Add to</span>
                      <i class="ico ico-expand naukri-icon naukri-icon-expand-more"></i>
                    </div>
                    <div class="dropdown-selected email-dd action-tuple rdx-action one-click-action">
                      <i class="ico ico-info  naukri-icon naukri-icon-email"></i>
                      <span class="label">
                        <div>
                          <div class="drop-layer email-drop-layer">
                            <li role="menuitem" class="opt mail-opt" tabindex="0" aria-label="Send email">Send email</li>
                          </div>
                        </div>
                      </span>
                    </div>
                    <div class="dropdown-selected set-reminder-dd rdx-action">
                      <i class="ico ico-info naukri-icon naukri-icon-access_time"></i>
                      <span class="label">Set reminder</span>
                      <i class="ico ico-expand naukri-icon naukri-icon-expand-more"></i>
                    </div>
                    <button class="forward add-to-dd action-tuple rdx-action naukri-btn-tertiary naukri-btn-regular" type="button">
                      <i class="ico ico-info naukri-icon naukri-icon-forward"></i>
                      <span class="label">Forward</span>
                    </button>
                    <div class="schedule-video-call add-to-dd action-tuple rdx-action" id="schedule-video-call" data-tnr-addvideotask="Call No UG for discussion|later|[{&quot;key&quot;:&quot;aefb0c44372c4bd1a91ac3f593695f06090150121b4850430b1848280a5400134f17425c4c0d145c01544d160c170b176&quot;,&quot;jsUserName&quot;:&quot;Sakib Ali&quot;}]||prev iew|CALLED_LATER">
                      <i class="ico ico-info naukri-icon naukri-icon-videocam"></i>
                      <span class="label">Schedule video call</span>
                    </div>
                  </div>
                </div>
                <div class="content-container">
                  <div class="left-section">
                    <div class="_1aggh">
                      <div class="v-SMv">
                        <div class="Elo9y flex-row">
                          <div class="jW8TV">
                            <div class="aEFIr">
                              <div role="presentation" class="I5S4M">
                                <img src="https://p.naukri.com/jphoto/l3bdccde6a9e363933d1d38798f0e8364183ed3c4c6ebe66d5ca09f331f8b42f921" alt="candidate profile" class=" _9OsDp" data-src="https://p.naukri.com/jphoto/l3bdccde6a9e363933d1d38798f0e8364183ed3c4c6ebe66d5ca09f331f8b42f921">
                                <span class="flex-row flex-aic _2sJeP"></span>
                              </div>
                            </div>
                          </div>
                          <div class="yZ5OX">
                            <div class="flex-row">
                              <div class="gD7Fy">
                                <div class="_33yhC flex-row flex-aic">
                                  <span class="_6Yd-L ellipsis" title="Sakib Ali">
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit">Sakib Ali</span>
                                    </span>
                                  </span>
                                  <button class="review-later-btn naukri-btn-tertiary naukri-btn-small" type="button">
                                    <div class="naukri-tooltip-wrapper"></div>
                                  </button>
                                  <button class="save-later-wrapper naukri-btn-tertiary naukri-btn-regular" type="button">
                                    <i class="save-ico naukri-icon naukri-icon-bookmark_border"></i>
                                    <span class="save-later-btn label">Save</span>
                                  </button>
                                </div>
                              </div>
                              <div class="vOrcj flex-row flex-aic">
                                <div class="_5F14a">
                                  <i title="Experience" class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span title="4y 1m">4y 1m</span>
                                </div>
                                <div class="_5F14a">
                                  <i title="Annual salary" class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span title="₹ 9.50 Lacs (expects: ₹ 10.0 Lacs)">₹ 9.50 Lacs (expects: ₹ 10.0 Lacs)</span>
                                </div>
                                <div class="_5F14a">
                                  <i title="Current location" class="ico ico-place naukri-icon naukri-icon-place"></i>
                                  <span class="location" title="Noida">Noida</span>
                                </div>
                              </div>
                              <div class="xxthQ">
                                <div class="undefined flex-row">
                                  <div class="cp4Ii">
                                    <span class="lbl">Current</span>
                                    <span class="ellipsis" title="Fullstack Developer  at  Girikon Solutions Pvt Ltd  since Apr '23">
                                      <span class="hlite-inherit">
                                        <span class="hlite-inherit">Fullstack </span>
                                      </span>
                                      <span class="hlite">
                                        <span class="hlite-inherit">Developer</span>
                                      </span>
                                      <span class="hlite-inherit">
                                        <span class="hlite-inherit"></span>
                                      </span> at <span class="hlite-inherit">
                                        <span class="hlite-inherit">Girikon Solutions Pvt Ltd</span>
                                      </span> since Apr '23 </span>
                                  </div>
                                  <div class="cp4Ii C4unx">
                                    <i title="Notice period" class="ico ico-place naukri-icon naukri-icon-timer"></i>
                                    <span>15 Days or less</span>
                                  </div>
                                </div>
                                <div class="cp4Ii">
                                  <span class="lbl">Highest degree</span>
                                  <span class="ellipsis" title="BCA Ch Charan Singh University (CCSU), Meerut, 2020">
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit">BCA Ch Charan Singh University (CCSU), Meerut, 2020</span>
                                    </span>
                                  </span>
                                </div>
                                <div class="detail pref-loc">
                                  <span class="lbl">Pref. locations</span>
                                  <span class="ellipsis" title="Noida,Remote,Delhi / NCR">
                                    <span class="read-more">
                                      <span>Noida,&nbsp;</span>
                                      <span>Remote,&nbsp;</span>
                                      <span>Delhi / NCR</span>
                                    </span>
                                  </span>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="flex-row flex-aic g1lY2">
                            <div class="VdVHl flex-col">
                              <div class="flex-row">
                                <div class="Y4fsF flex-col flex-aic KkXNJ">
                                  <div class="flex-row vc9LM">
                                    <div class="wOGA7">
                                      <button class="vFAV- flex-row flex-aic  naukri-btn-secondary naukri-btn-small" type="button" label="Small">
                                        <div class="GSKIi">
                                          <span class="_6-1WA">View phone number</span>
                                        </div>
                                      </button>
                                    </div>
                                  </div>
                                  <div class="call-from-app-cta">
                                    <div class="naukri-tooltip-wrapper">
                                      <button class="call-candidate-button naukri-btn-secondary naukri-btn-regular" type="button">
                                        <i class="ico naukri-icon naukri-icon-phone"></i>
                                        <span class="cta-text">Call candidate</span>
                                      </button>
                                    </div>
                                  </div>
                                </div>
                                <div class="pGKXV">
                                  <span title="Verified by naukri.com on 1 Jan, '13">Verified phone</span> &amp; email
                                </div>
                              </div>
                              <div class="AvmSa ellipsis" title="alisakib899@gmail.com">
                                <i title="Email" class="ico ico-email naukri-icon naukri-icon-email"></i>
                                <span class="hlite-inherit">
                                  <span class="hlite-inherit">alisakib899@gmail.com</span>
                                </span>
                              </div>
                            </div>
                            <div class="social-media flex-row flex-aife">
                              <div class="qWcZx flex-row flex-aic">
                                <div class="naukri-tooltip-wrapper">
                                  <a target="_blank" href="https://www.linkedin.com/in/sakib-ali-97b6061a3/" class="link ext DOVr- ei3rX">
                                    <i class="ico naukri-icon naukri-icon-linkedin"></i>
                                  </a>
                                </div>
                              </div>
                              <span class="epGP0 ellipsis" title="Linkedin">Linkedin</span>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="career-timeline">
                        <hr class="horizontal-divider">
                        <div class="timeline flex-row">
                          <div class="naukri-tooltip-wrapper">
                            <div class="horizontal-line flex-row flex-aic flex-jcc even 
                         
                        hover-style
                        
                        " style="width: 9.43396%;">
                              <span class="flex-row flex-aic">
                                <span class="ico-timeline flex-row flex-aic flex-jcc">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                </span>
                                <span class="date ">Sep '19</span>
                              </span>
                            </div>
                          </div>
                          <div class="naukri-tooltip-wrapper">
                            <div class="horizontal-line flex-row flex-aic flex-jcc even 
                         
                        hover-style
                        
                        " style="width: 54.717%;">
                              <span class="flex-row flex-aic">
                                <div class="flex-row flex-aic tooltip-edu">
                                  <span class="ico-timeline school-small flex-row flex-aic flex-jcc">
                                    <i class="ico naukri-icon naukri-icon-school"></i>
                                  </span>
                                </div>
                                <span class="date ">2020</span>
                              </span>
                            </div>
                          </div>
                          <div class="naukri-tooltip-wrapper">
                            <div class="horizontal-line flex-row flex-aic flex-jcc odd 
                         
                        hover-style
                        
                        " style="width: 22.6415%;">
                              <span class="flex-row flex-aic">
                                <span class="ico-timeline flex-row flex-aic flex-jcc">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                </span>
                                <span class="date ">May '22</span>
                              </span>
                            </div>
                          </div>
                          <div class="naukri-tooltip-wrapper">
                            <div class="horizontal-line flex-row flex-aic flex-jcc even 
                        last-child 
                        hover-style
                        
                        " style="width: 20.7547%;">
                              <span class="flex-row flex-aic">
                                <span class="ico-timeline flex-row flex-aic flex-jcc">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                </span>
                                <span class="date ">Apr '23</span>
                                <span class="endDate">till date</span>
                              </span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="tuple-footer_tuple-footer__khXId">
                      <span class="flex-row flex-aic tuple-footer_left-item__hwtGz" title="Views">
                        <i class="ico naukri-icon naukri-icon-remove_red_eye"></i>
                        <span>312</span>
                      </span>
                      <span class="flex-row flex-aic tuple-footer_left-item__hwtGz" title="Downloads">
                        <i class="ico naukri-icon naukri-icon-file_download"></i>
                        <span>78</span>
                      </span>
                      <div class="tuple-footer_tuple-meta__XsAi9 fr">
                        <span class="tuple-footer_download-status__pR9w5 fl">
                          <span class="flex-row flex-aic tuple-footer_item__3AY0U">Modified in last 2 months</span>
                        </span>
                        <span class="flex-row flex-aic tuple-footer_item__3AY0U">Active in last 2 months</span>
                      </div>
                    </div>
                  </div>
                  <div class="profile-summary">
                    <div class="profile-tabs">
                      <div class="naukri-tabs naukri-tabs-top tracker">
                        <div role="tablist" class="naukri-tabs-nav">
                          <div class="naukri-tabs-nav-wrap">
                            <div class="naukri-tabs-nav-list" style="transform: translate(0px, 0px);">
                              <div class="naukri-tabs-tab naukri-tabs-tab-active">
                                <div role="tab" aria-selected="true" class="naukri-tabs-tab-btn" tabindex="0" id="rc-tabs-0-tab-profile" aria-controls="rc-tabs-0-panel-profile">Profile detail</div>
                              </div>
                              <div class="naukri-tabs-tab">
                                <div role="tab" aria-selected="false" class="naukri-tabs-tab-btn" tabindex="0" id="rc-tabs-0-tab-videoAndCv" aria-controls="rc-tabs-0-panel-videoAndCv">Attached CV</div>
                              </div>
                              <div class="naukri-tabs-ink-bar naukri-tabs-ink-bar-animated" style="left: 28px; width: 87px;"></div>
                            </div>
                          </div>
                          <div class="naukri-tabs-nav-operations naukri-tabs-nav-operations-hidden">
                            <button type="button" class="naukri-tabs-nav-more" tabindex="-1" aria-hidden="true" aria-haspopup="listbox" aria-controls="rc-tabs-0-more-popup" id="rc-tabs-0-more" aria-expanded="false" style="visibility: hidden; order: 1;">
                              <i class=" naukri-icon naukri-icon-elipsis"></i>
                            </button>
                          </div>
                        </div>
                        <div class="naukri-tabs-content-holder">
                          <div class="naukri-tabs-content naukri-tabs-content-top">
                            <div role="tabpanel" tabindex="0" aria-hidden="false" class="naukri-tabs-tabpane naukri-tabs-tabpane-active profile-detail-tab" id="rc-tabs-0-panel-profile" aria-labelledby="rc-tabs-0-tab-profile"></div>
                            <div role="tabpanel" tabindex="-1" aria-hidden="true" class="naukri-tabs-tabpane" style="display: none;" id="rc-tabs-0-panel-videoAndCv" aria-labelledby="rc-tabs-0-tab-videoAndCv"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="profile-content">
                      <div class="profile-width-content">
                        <blockquote class="BsG0Z  ">
                          <span class="hlite-inherit">
                            <span class="hlite-inherit">I am a </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">full</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"></span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"></span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">developer</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> working with LAMP </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> (Laravel Framework) and </span>
                            <span style="font-weight: bold;">Node</span>
                            <span class="hlite-inherit">.js, Express.js, </span>
                            <span style="font-weight: bold;">React.js</span>
                            <span class="hlite-inherit"> (</span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">MERN</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"></span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit">).</span>
                          </span>
                        </blockquote>
                        <div class="_1icem">
                          <div class="mRRK4">Keyskills</div>
                          <span class="XNIdD _9JtKk">
                            <span class="read-more">
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Express">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Express</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="CSS">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">CSS</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="jQuery">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">jQuery</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Ajax">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Ajax</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="HTML">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">HTML</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Node.js">
                                  <span class="hlite-inherit">
                                    <span style="font-weight: bold;">Node</span>
                                    <span class="hlite-inherit">.js</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="React.js">
                                  <span class="hlite-inherit">
                                    <span style="font-weight: bold;">React.js</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Javascript">
                                  <span class="hlite-inherit">
                                    <span style="font-weight: bold;">Javascript</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Laravel">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Laravel</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="PHP">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">PHP</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="MySQL">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">MySQL</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Django">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Django</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="SOAP">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">SOAP</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="GIT">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">GIT</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Rest">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Rest</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="API">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">API</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="Python">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Python</span>
                                  </span>
                                </span>
                              </div>
                              <div class="focusable suggestor-tag   " tabindex="0">
                                <span class="txt ellipsis" title="JIRA">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">JIRA</span>
                                  </span>
                                </span>
                              </div>
                            </span>
                          </span>
                          <a class="link int unmwb" href="/">View IT skills</a>
                          <div class="woDo4">
                            <div class="_7ASUd">May also know</div>
                            <span class="XNIdD _9JtKk">
                              <span class="read-more">
                                <div class="focusable suggestor-tag   " tabindex="0">
                                  <span class="txt ellipsis" title="Mern Stack">
                                    <span class="hlite">
                                      <span class="hlite-inherit">Mern</span>
                                    </span>
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit"></span>
                                    </span>
                                    <span class="hlite">
                                      <span class="hlite-inherit">Stack</span>
                                    </span>
                                  </span>
                                </div>
                                <div class="focusable suggestor-tag   " tabindex="0">
                                  <span class="txt ellipsis" title="Python Development">
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit">Python Development</span>
                                    </span>
                                  </span>
                                </div>
                                <div class="focusable suggestor-tag   " tabindex="0">
                                  <span class="txt ellipsis" title="Fullstack Development">
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit">Fullstack Development</span>
                                    </span>
                                  </span>
                                </div>
                                <div class="focusable suggestor-tag   " tabindex="0">
                                  <span class="txt ellipsis" title="LAMP">
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit">LAMP</span>
                                    </span>
                                  </span>
                                </div>
                                <button class="more rdx-link naukri-btn-tertiary naukri-btn-x-small" type="button">+6 more</button>
                              </span>
                            </span>
                          </div>
                        </div>
                        <div class="_2NDnc">
                          <h4>Work summary</h4>
                          <div class="Ju-0N">
                            <span class="hlite-inherit">
                              <span class="hlite-inherit">I am a </span>
                            </span>
                            <span class="hlite">
                              <span class="hlite-inherit">full</span>
                            </span>
                            <span class="hlite-inherit">
                              <span class="hlite-inherit"></span>
                            </span>
                            <span class="hlite">
                              <span class="hlite-inherit">stack</span>
                            </span>
                            <span class="hlite-inherit">
                              <span class="hlite-inherit"></span>
                            </span>
                            <span class="hlite">
                              <span class="hlite-inherit">developer</span>
                            </span>
                            <span class="hlite-inherit">
                              <span class="hlite-inherit"> working with LAMP </span>
                            </span>
                            <span class="hlite">
                              <span class="hlite-inherit">Stack</span>
                            </span>
                            <span class="hlite-inherit">
                              <span class="hlite-inherit"> (Laravel Framework) and </span>
                              <span style="font-weight: bold;">Node</span>
                              <span class="hlite-inherit">.js, Express.js, </span>
                              <span style="font-weight: bold;">React.js</span>
                              <span class="hlite-inherit"> (</span>
                            </span>
                            <span class="hlite">
                              <span class="hlite-inherit">MERN</span>
                            </span>
                            <span class="hlite-inherit">
                              <span class="hlite-inherit"></span>
                            </span>
                            <span class="hlite">
                              <span class="hlite-inherit">Stack</span>
                            </span>
                            <span class="hlite-inherit">
                              <span class="hlite-inherit">).</span>
                            </span>
                          </div>
                          <div class="zhh5C">
                            <div class="XBZjy">
                              <div class="-Zm3Z">Industry</div>
                              <div class="OesXg">IT Services &amp; Consulting</div>
                            </div>
                            <div class="XBZjy">
                              <div class="-Zm3Z">Department</div>
                              <div class="OesXg">Engineering - Software &amp; QA</div>
                            </div>
                            <div class="XBZjy">
                              <div class="-Zm3Z">Role</div>
                              <div class="OesXg">Full Stack Developer</div>
                            </div>
                          </div>
                        </div>
                        <div class="work-exp">
                          <h4>Work experience</h4>
                          <div class="career-timeline">
                            <div class="timeline flex-row">
                              <div class="naukri-tooltip-wrapper">
                                <div class="horizontal-line flex-row flex-aic flex-jcc even 
                         
                        hover-style
                        
                        " style="width: 62.2642%;">
                                  <span class="flex-row flex-aic">
                                    <span class="ico-timeline-ellipse even"></span>
                                    <span class="date no-icon">Sep '19</span>
                                  </span>
                                </div>
                              </div>
                              <div class="naukri-tooltip-wrapper">
                                <div class="horizontal-line flex-row flex-aic flex-jcc odd 
                         
                        hover-style
                        
                        " style="width: 22.6415%;">
                                  <span class="flex-row flex-aic">
                                    <span class="ico-timeline-ellipse odd"></span>
                                    <span class="date no-icon">May '22</span>
                                  </span>
                                </div>
                              </div>
                              <div class="naukri-tooltip-wrapper">
                                <div class="horizontal-line flex-row flex-aic flex-jcc even 
                        last-child 
                        hover-style
                        
                        " style="width: 20.7547%;">
                                  <span class="flex-row flex-aic">
                                    <span class="ico-timeline-ellipse even"></span>
                                    <span class="date no-icon">Apr '23</span>
                                    <span class="endDate">till date</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="work-exp-card">
                            <div class="exp-head">
                              <div class="exp-icon flex-row flex-aic flex-jcc  
                exp-icon-even">
                                <img src="https://img.naukimg.com/logo_images/groups/v1/4598093.gif" alt="Girikon Solutions Pvt Ltd logo" class=" " data-src="https://img.naukimg.com/logo_images/groups/v1/4598093.gif">
                              </div>
                              <div class="exp-label">
                                <div class="desig">
                                  <span>
                                    <span>Fullstack </span>
                                  </span>
                                  <span class="hlite">
                                    <span>Developer</span>
                                  </span> at <span>
                                    <span>Girikon Solutions Pvt Ltd</span>
                                  </span>
                                </div>
                                <div class="dates">
                                  <span>Apr '23 till date ( 10m )</span>
                                </div>
                              </div>
                            </div>
                            <div class="desc">
                              <span>
                                <span>• Developing front end website architecture. • Designing user interactions on web pages. • Developing back-end website applications. • Creating servers and databases for functionality. • Ensuring cross-platform optimization for mobile phones. • Ensuring responsiveness of applications. • Working alongside graphic designers for web design features. • Seeing through a project from conception to finished product. • Designing and developing APIs. • Meeting both technical and consumer needs. • Staying abreast of developments in web applications and programming languages.</span>
                              </span>
                            </div>
                          </div>
                          <div class="work-exp-card">
                            <div class="exp-head">
                              <div class="exp-icon flex-row flex-aic flex-jcc fallback-img 
                exp-icon-odd">
                                <img src="//static.naukimg.com/s/7/112/i/exp_build.eb093b23.svg" alt="Leadingdots Solutions Pvt Ltd logo" class=" " data-src="https://img.naukimg.com/logo_images/groups/v1/8317097.gif">
                              </div>
                              <div class="exp-label">
                                <div class="desig">
                                  <span>
                                    <span>Web </span>
                                  </span>
                                  <span class="hlite">
                                    <span>Developer</span>
                                  </span> at <span>
                                    <span>Leadingdots Solutions Pvt Ltd</span>
                                  </span>
                                </div>
                                <div class="dates">
                                  <span>May '22 till Mar '23 ( 10m )</span>
                                </div>
                              </div>
                            </div>
                            <div class="desc">
                              <span>
                                <span>Designed and developed web applications across multiple APIs, third-party integrations and databases. Passionate and hardworking with penchant for developing customized interfaces that factor in unique demands for accessibility, reachability and security.</span>
                              </span>
                            </div>
                          </div>
                          <div class="work-exp-card">
                            <div class="exp-head">
                              <div class="exp-icon flex-row flex-aic flex-jcc  
                exp-icon-even">
                                <img src="https://img.naukimg.com/logo_images/groups/v1/4483868.gif" alt="Apponward Technologies logo" class=" " data-src="https://img.naukimg.com/logo_images/groups/v1/4483868.gif">
                              </div>
                              <div class="exp-label">
                                <div class="desig">
                                  <span>
                                    <span>Senior Php </span>
                                  </span>
                                  <span class="hlite">
                                    <span>Developer</span>
                                  </span> at <span>
                                    <span>Apponward Technologies</span>
                                  </span>
                                </div>
                                <div class="dates">
                                  <span>Sep '19 till May '22 ( 2y 8m )</span>
                                </div>
                              </div>
                            </div>
                            <div class="desc">
                              <span>
                                <span>I have good in hand experience in php language and laravel I am working in backend and i use php,python,django,laravel Skills : PHP, JQUERY, MYSQL, AJAX, LARAVEL, PAYMENT GATEWAYS, HTML, CSS, SOAP AND REST API'S, ANGULAR, </span>
                                <span style="font-weight: bold;">JAVASCRIPT</span>
                                <span>, CI,PYTHON,DJANGO,DJANGO REST FRAMEWORK my recent completed projects : https://www.urwagon.com/fly/public/ -&gt; project to ship packages internationally (in laravel) https://flowmixx.com/ -&gt; music website (backend in laravel and frontend in angular https://www.oxygentimes.com/ -&gt; projects for comparing oxygen Concentrator</span>
                              </span>
                            </div>
                            <div class="exp-card">
                              <div class="card-head">
                                <div class="exp-text">Wypwise</div>
                                <div class="exp-label"> Aug '21 till date </div>
                              </div>
                              <div class=" exp-text">
                                <span class="hlite-inherit">
                                  <span class="hlite-inherit">Mr. Magik(</span>
                                </span>
                                <span class="hlite">
                                  <span class="hlite-inherit">Full</span>
                                </span>
                                <span class="hlite-inherit">
                                  <span class="hlite-inherit"> time, Offsite)</span>
                                </span>
                              </div>
                              <span class="read-more">
                                <div class="role-desc exp-text proj-desc line-clamp">
                                  <span class="exp-label">Project description: </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Wypwise is an mobile application for two different users Customer and Car Owner. The concept is similar to Zoomcar. Customers can book a car for a trip and car owner will accept their car booking or car owner can reject. Admin portal and REST API's are build by me. Payment gateway APIs are in Braintree. </span>
                                  </span>
                                </div>
                                <button class="more  naukri-btn-tertiary naukri-btn-x-small" type="button">... Read More</button>
                              </span>
                            </div>
                          </div>
                        </div>
                        <div class="cv-educ">
                          <h4 class="educ-title">Education</h4>
                          <div class="edu-wrapper">
                            <div class="edu-head">
                              <div class="edu-icon flex-row flex-aic flex-jcc">
                                <i class="ico ico-info educ-logo naukri-icon naukri-icon-school-1"></i>
                              </div>
                              <div class="edu-label">
                                <div class="desig">BCA,Computers,2020 <div class="edu-type">UG</div>
                                </div>
                                <div class="dates">
                                  <span class="institue">
                                    <span class="hlite-inherit">
                                      <span class="hlite-inherit">Ch Charan Singh University (CCSU), Meerut</span>
                                    </span>
                                  </span>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div id="cv-prev-it-skills" class="cv-prev-it-skills">
                          <h4>IT skills</h4>
                          <div class="table-wrapper">
                            <div style="position: relative; overflow: hidden; width: 100%; height: auto; min-height: 0px; max-height: 100%;">
                              <div style="position: relative; overflow: scroll; margin-right: -17px; margin-bottom: -17px; min-height: 17px; max-height: calc(100% + 17px);">
                                <div class="table view-all-table">
                                  <div class="thead ">
                                    <div tabindex="0" class="tr tab-row table-tuple table-tuple-0 s">
                                      <div class="th cell col col-0 ">
                                        <div class="head-cell Skills-hd">Skills</div>
                                      </div>
                                      <div class="th cell col col-1 ">
                                        <div class="head-cell Version-hd">Version</div>
                                      </div>
                                      <div class="th cell col col-2 ">
                                        <div class="head-cell Last Used-hd">Last Used</div>
                                      </div>
                                      <div class="th cell col col-3 last">
                                        <div class="head-cell Experience-hd">Experience</div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="tbody ">
                                    <div tabindex="0" class="tr tab-row table-tuple table-tuple-1 odd ">
                                      <div class="td cell col  col-0">
                                        <div class="data-cell skills">
                                          <span>
                                            <span>Laravel</span>
                                          </span>
                                        </div>
                                      </div>
                                      <div class="td cell col  col-1">
                                        <div class="data-cell version">9</div>
                                      </div>
                                      <div class="td cell col  col-2">
                                        <div class="data-cell lastUsed">2023</div>
                                      </div>
                                      <div class="td cell col last col-3">
                                        <div class="data-cell exp">4y</div>
                                      </div>
                                    </div>
                                    <div tabindex="0" class="tr tab-row table-tuple table-tuple-2 even ">
                                      <div class="td cell col  col-0">
                                        <div class="data-cell skills">
                                          <span>
                                            <span style="font-weight: bold;">Node</span>
                                            <span>.js</span>
                                          </span>
                                        </div>
                                      </div>
                                      <div class="td cell col  col-1">
                                        <div class="data-cell version">18.14</div>
                                      </div>
                                      <div class="td cell col  col-2">
                                        <div class="data-cell lastUsed">2023</div>
                                      </div>
                                      <div class="td cell col last col-3">
                                        <div class="data-cell exp">2y</div>
                                      </div>
                                    </div>
                                    <div tabindex="0" class="tr tab-row table-tuple table-tuple-3 odd last">
                                      <div class="td cell col  col-0">
                                        <div class="data-cell skills">
                                          <span>
                                            <span>PHP</span>
                                          </span>
                                        </div>
                                      </div>
                                      <div class="td cell col  col-1">
                                        <div class="data-cell version">8</div>
                                      </div>
                                      <div class="td cell col  col-2">
                                        <div class="data-cell lastUsed">2023</div>
                                      </div>
                                      <div class="td cell col last col-3">
                                        <div class="data-cell exp">4y</div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div class="horizontalTrack" style="position: fixed; height: 6px; bottom: 2px; left: 2px; right: 2px; border-radius: 6px; background-color: rgb(226, 226, 226);">
                                <div class="horizontalThumb" style="position: fixed; display: block; height: 6px; bottom: 0px; background-color: rgb(179, 179, 179); border-radius: 6px; width: 0px;"></div>
                              </div>
                              <div style="position: absolute; width: 6px; right: 2px; bottom: 2px; top: 2px; border-radius: 3px;">
                                <div style="position: relative; display: block; width: 100%; cursor: pointer; border-radius: inherit; background-color: rgba(0, 0, 0, 0.2); height: 0px;"></div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="YQo1I">
                          <h4 class="ZIJkF">Other details</h4>
                          <div class="_88wuB">
                            <h4>Languages known</h4>
                            <div class="_9FKxR">hindi - Expert <span class="_5F2Uo"> ( Read,Write,Speak )</span>
                            </div>
                            <div class="_9FKxR">english - Expert <span class="_5F2Uo"> ( Read,Write,Speak )</span>
                            </div>
                          </div>
                          <div class="nqhGZ">
                            <h4>Personal details</h4>
                            <div class="table-wrapper details-prev">
                              <div style="position: relative; overflow: hidden; width: 100%; height: auto; min-height: 0px; max-height: 100%;">
                                <div style="position: relative; overflow: scroll; margin-right: -17px; margin-bottom: -17px; min-height: 17px; max-height: calc(100% + 17px);">
                                  <div class="table view-all-table">
                                    <div class="thead ">
                                      <div tabindex="0" class="tr tab-row table-tuple table-tuple-0 s">
                                        <div class="th cell col col-0 ">
                                          <div class="table-head RwJYw">Date of Birth</div>
                                        </div>
                                        <div class="th cell col col-1 ">
                                          <div class="table-head gOeNe">Gender</div>
                                        </div>
                                        <div class="th cell col col-2 ">
                                          <div class="table-head _0YyRI">Marital status</div>
                                        </div>
                                        <div class="th cell col col-3 ">
                                          <div class="table-head _9HpRi">Category</div>
                                        </div>
                                        <div class="th cell col col-4 last">
                                          <div class="table-head _64mvN">Physically Challenged</div>
                                        </div>
                                      </div>
                                    </div>
                                    <div class="tbody ">
                                      <div tabindex="0" class="tr tab-row table-tuple table-tuple-1 odd last">
                                        <div class="td cell col  col-0">
                                          <div class="table-cell RwJYw">8 Nov 1998</div>
                                        </div>
                                        <div class="td cell col  col-1">
                                          <div class="table-cell gOeNe">Male</div>
                                        </div>
                                        <div class="td cell col  col-2">
                                          <div class="table-cell _0YyRI">Single/unmarried</div>
                                        </div>
                                        <div class="td cell col  col-3">
                                          <div class="table-cell _9HpRi">OBC - Creamy</div>
                                        </div>
                                        <div class="td cell col last col-4">
                                          <div class="table-cell _64mvN">No</div>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                                <div class="horizontalTrack" style="position: fixed; height: 6px; bottom: 2px; left: 2px; right: 2px; border-radius: 6px; background-color: rgb(226, 226, 226); visibility: hidden;">
                                  <div class="horizontalThumb" style="position: fixed; display: block; height: 6px; bottom: 0px; background-color: rgb(179, 179, 179); border-radius: 6px; width: 0px;"></div>
                                </div>
                                <div style="position: absolute; width: 6px; right: 2px; bottom: 2px; top: 2px; border-radius: 3px; visibility: hidden;">
                                  <div style="position: relative; display: block; width: 100%; cursor: pointer; border-radius: inherit; background-color: rgba(0, 0, 0, 0.2); height: 0px;"></div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="hmFnB">
                            <h4>Desired job detail</h4>
                            <div class="table-wrapper details-prev">
                              <div style="position: relative; overflow: hidden; width: 100%; height: auto; min-height: 0px; max-height: 100%;">
                                <div style="position: relative; overflow: scroll; margin-right: -17px; margin-bottom: -17px; min-height: 17px; max-height: calc(100% + 17px);">
                                  <div class="table view-all-table">
                                    <div class="thead ">
                                      <div tabindex="0" class="tr tab-row table-tuple table-tuple-0 s">
                                        <div class="th cell col col-0 ">
                                          <div class="table-head job-type">Job Type</div>
                                        </div>
                                        <div class="th cell col col-1 last">
                                          <div class="table-head emp-status">Employment status</div>
                                        </div>
                                      </div>
                                    </div>
                                    <div class="tbody ">
                                      <div tabindex="0" class="tr tab-row table-tuple table-tuple-1 odd last">
                                        <div class="td cell col  col-0">
                                          <div class="table-cell job-type">Permanent / Temporary</div>
                                        </div>
                                        <div class="td cell col last col-1">
                                          <div class="table-cell emp-status">Full Time, Part Time</div>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                                <div class="horizontalTrack" style="position: fixed; height: 6px; bottom: 2px; left: 2px; right: 2px; border-radius: 6px; background-color: rgb(226, 226, 226); visibility: hidden;">
                                  <div class="horizontalThumb" style="position: fixed; display: block; height: 6px; bottom: 0px; background-color: rgb(179, 179, 179); border-radius: 6px; width: 0px;"></div>
                                </div>
                                <div style="position: absolute; width: 6px; right: 2px; bottom: 2px; top: 2px; border-radius: 3px; visibility: hidden;">
                                  <div style="position: relative; display: block; width: 100%; cursor: pointer; border-radius: inherit; background-color: rgba(0, 0, 0, 0.2); height: 0px;"></div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="U2nyl">
                        <div class="FjXHl">
                          <div>
                            <h4>Attached CV</h4>
                            <div class="Gv2G4">
                              <div class="mLnzp">Last updated on 2 Nov, '23</div>
                            </div>
                          </div>
                          <div class="TYRll">
                            <button class="HiggM naukri-btn-tertiary naukri-btn-regular" type="button" aria-label="Download Resume">
                              <i class="ico ico-info naukri-icon naukri-icon-download"></i>
                            </button>
                          </div>
                        </div>
                        <div class="DBDnQ">
                          <span class="hlite-inherit">
                            <span class="hlite-inherit">Sakib Ali Web </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Developer</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> H.No.449 pasonda, Sahibabad,GZB +919015894872 alisakib899@gmail.com EXPERIENCE (4+ yrs) SKILLS Apponward Technologies Pvt. Ltd., Noida ? Web ?</span>
                            <span style="font-weight: bold;">Node</span>
                            <span class="hlite-inherit">.js Express.js </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Developer</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> ?MongoDB </span>
                            <span style="font-weight: bold;">React.js</span>
                            <span class="hlite-inherit"> ?AWS Jenkins Sep 2019 - May 2022 ? 3 yrs ?PHP LARAVEL I have worked as a Team Lead and I have completed more than 10 HTML </span>
                            <span style="font-weight: bold;">JAVASCRIPT</span>
                            <span class="hlite-inherit"> projects. I have worked with the LAMP </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> and Laravel framework. ?CSS AJAX I have also worked with </span>
                            <span style="font-weight: bold;">Node</span>
                            <span class="hlite-inherit">.js and Express.js (</span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">MERN</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"></span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit">). ?JQUERY GIT ?SOAP API JIRA ?REST API PYTHON Leadingdots Solutions Pvt. Ltd., Noida ? Web ?DJANGO </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Developer</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> ?DJANGO REST FRAMEWORK May 2022 - March 2023 ? 11 months ? I am working with the LAMP </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> (Laravel framework) and </span>
                            <span style="font-weight: bold;">Node</span>
                            <span class="hlite-inherit">.js, ? Express.js, MongoDB, </span>
                            <span style="font-weight: bold;">React.js</span>
                            <span class="hlite-inherit"> (</span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">MERN</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"></span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit">). ? ? Girikon Solutions Pvt. Ltd., Noida ? </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Full</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"></span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Stack</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> ? </span>
                          </span>
                          <span class="hlite">
                            <span class="hlite-inherit">Developer</span>
                          </span>
                          <span class="hlite-inherit">
                            <span class="hlite-inherit"> April 2023 - Present I am working on a Girikon CRM Project. AWARDS I have worked with the whatsapp api?s like sending messages,creating Received Employee of the templates,sending whatsapp templates etc. month in january 2021 Built a whatsapp chatbot. Received Employee of the month in October 2022 EDUCATION HR Institute of Science &amp; Technology, Ghaziabad ? BCA LANGUAGES JUNE 2017 - APRIL 2020 Hindi,English Received 60% overall in bca with no backlogs PROJECTS Go Wagon ? International Shipping Project (https://www.go-wagon.com) I have developed a website and admin portal for international Shipping using the carrier DHL EXPRESS. I have developed an Admin panel and REST API in Laravel and a website also in Laravel. Roles and Responsibilities : ? Designs, writes, and edits website content. ? Communication with colleagues and managers daily. ? Designs assignments with web services like REST, SOAP, etc. ? Evaluates written code to ensure it meets industry standards and is compatible with all devices. ? Communication and demo with client. Key Skills : PHP , LARAVEL , MYSQL, REST API, POSTMAN, </span>
                            <span style="font-weight: bold;">JAVASCRIPT</span>
                            <span class="hlite-inherit">, JQUERY, AJAX, AWS, JIRA. Flowmixx ? The ultimate music source for DJs (https://fowmixx.com) Flowmixx is a music website. I have developed REST API?s and Admin Panel in this Project. Frontend was in Angularjs. Roles and Responsibilities : ? Communication and meetings with colleagues and managers daily. ? Develop and maintain REST API. ? Develop and maintain Admin Portal. ? Manage JIRA of the project. ? Communication and demo with client. Key Skills : PHP , LARAVEL , MYSQL, REST API, POSTMAN, </span>
                            <span style="font-weight: bold;">JAVASCRIPT</span>
                            <span class="hlite-inherit">, JQUERY, AJAX, AWS, JIRA, S3 Bucket. PETPRO ? android ,ios, and web application (https://petpro.co.in) App for booking appointments for pets. I have developed REST API?s and Admin Panel in this Project. I have used an AWS S3 bucket for storage in this project and we have set up the server also over AWS. Roles and Responsibilities : ? Communication and meetings with colleagues and managers daily. ? Develop and maintain REST API. ? Develop and maintain Admin Portal. ? Manage JIRA of the project. ? Communication and demo with client. Key Skills : PHP , LARAVEL , MYSQL, REST API, POSTMAN, </span>
                            <span style="font-weight: bold;">JAVASCRIPT</span>
                            <span class="hlite-inherit">, JQUERY, AJAX, AWS, JIRA, S3 Bucket. WYPWISE ?android,ios app for customer and car owner and Admin portal (https://wypwise.com) I have Developed REST APIs and Admin Portal in Python Django - Customers can book a car for a trip. In this Project also I have used AWS server and S3 bucket for storage. Roles and Responsibilities : ? Communication and meetings with colleagues and managers daily. ? Develop and maintain REST API. ? Develop and maintain Admin Portal. ? Manage JIRA of the project. ? Communication and demo with client. Key Skills : PYTHON , DJANGO , DJANGO REST FRAMEWORK, MYSQL, REST API, POSTMAN, </span>
                            <span style="font-weight: bold;">JAVASCRIPT</span>
                            <span class="hlite-inherit">, JQUERY, AJAX, AWS, JIRA, S3 Bucket. RIGHTHANDS ? android ,ios, and web application (https://betaweb.myrighth.com) Application using which users can book appointments for home cleaning services. I have developed REST API in </span>
                            <span style="font-weight: bold;">Node</span>
                            <span class="hlite-inherit">.js and integrated them in </span>
                            <span style="font-weight: bold;">React.js</span>
                            <span class="hlite-inherit">. We have used AWS in this project. Roles and Responsibilities : ? Communication and meetings with colleagues and managers daily. ? Develop and maintain REST API. ? Integrate REST API in Website (</span>
                            <span style="font-weight: bold;">React.js</span>
                            <span class="hlite-inherit">). ? Manage JIRA of the project. ? Communication and demo with client. Key Skills : </span>
                            <span style="font-weight: bold;">Node</span>
                            <span class="hlite-inherit">.js , Express.js , MongoDB, </span>
                            <span style="font-weight: bold;">React.js</span>
                            <span class="hlite-inherit"> , REST API, POSTMAN, </span>
                            <span style="font-weight: bold;">JAVASCRIPT</span>
                            <span class="hlite-inherit">, JQUERY, AJAX, AWS, JIRA, S3 Bucket.</span>
                          </span>
                        </div>
                        <div style="height: 36px;"></div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="right-section sticky">
                  <div class="side-widget-wrapper card-bg side-widget requirement-widget">
                    <div class="collapser-wrapper">
                      <div class="collapser collapsed " tabindex="0">
                        <div class="collapser-header ">
                          <div class="flex-row flex-jcsb flex-aic">
                            <h4 class="heading">Exists in 2 Folders</h4>
                            <span class="expand-ico">
                              <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path d="M16.59 8.59 12 13.17 7.41 8.59 6 10l6 6 6-6z"></path>
                              </svg>
                            </span>
                          </div>
                        </div>
                        <div class="collapsible-content">
                          <div class="children-wrapper">
                            <div style="position: relative; overflow: hidden; height: auto; min-height: 0px; max-height: 200px;">
                              <div style="position: relative; overflow: auto scroll; margin-right: -17px; margin-bottom: 0px; min-height: 17px; max-height: 200px;">
                                <span class="entity-type">Folders</span>
                                <div class="folder">
                                  <h3 class="ellipsis" title="My Accessed CVs">My Accessed CVs</h3>
                                  <span class="description">
                                    <span class="default"> by <span class="highlighted"> You</span>
                                      <span class="highlighted">, 3 days ago</span>
                                    </span>
                                  </span>
                                </div>
                                <div class="folder">
                                  <h3 class="ellipsis" title="test folder">test folder</h3>
                                  <span class="description">
                                    <span class="default"> by <span class="highlighted"> You</span>
                                      <span class="highlighted">, 3 days ago</span>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class="track-horizontal" style="display: none; visibility: hidden;">
                                <div class="track-horizontal" style="display: none; width: 0px;"></div>
                              </div>
                              <div class="verticalTrack" style="position: absolute; width: 6px; right: 2px; bottom: 2px; top: 2px; border-radius: 6px; background-color: rgb(226, 226, 226); visibility: hidden;">
                                <div class="verticalThumb" style="position: relative; display: block; width: 100%; background-color: rgb(179, 179, 179); border-radius: 6px; height: 0px;"></div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comments notes">
                    <div class="comments-header">
                      <div class="add-comment">
                        <div class="num-comments font-prop">No comments</div>
                        <button class="add-comm-btn font-prop rdx-link naukri-btn-tertiary naukri-btn-x-small" type="button">Add comments</button>
                      </div>
                    </div>
                  </div>
                  <div class="simcv-wrapper ">
                    <div class="header flex-row flex-aic ">1922 similar profiles <a target="_blank" href="/v3/simcv?uniqueId=8b679266d1382e73c90795d14293125a5c580c04431b0b475712440e595a0248415b420643470a555a51481b0915564552595a09594c1b081002196&amp;activeIn=3650&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;uname=undefined&amp;parentHighLightingKey=6650051176-1&amp;principalUserId=185755686&amp;hfFlowName=simcv&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;pageNo=1&amp;resPerPage=40" class="link ext view-all">View all</a>
                    </div>
                    <div class="suggested-profile">
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=46ca894d3b98b9d978&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=46ca894d3b98b9d978&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=897bd442b0fe7a9b0a2c6d24bf226b96515b0d574d160a1810104658550f594b1208186" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <div id="sim-cv-promo-section"></div>
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s327dcaf2e4e9c4040c473321f759ad0e259d1c1b63c2d78014fc1bcaec07969dc1">
                              </div>
                              <div class="headline">
                                <div class="name">Pankaj Joshi</div>
                                <div class="current ellipsis" title="PHP Developer at Teknobuild pvt ltd ">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">PHP </span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Developer</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">Teknobuild pvt ltd</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="4y 6m">4y 6m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 4.60 Lacs">₹ 4.60 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="New Delhi (prefers Gurugram,Noida,Delhi / NCR)">New Delhi (prefers Gurugram,Noida,Delhi / NCR)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">sqlserver</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">plsql</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">laravel</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">digital marketing</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">php</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">codeigniter</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">javascript</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">web development</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">css</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">mysql</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">jquery</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <button class="more rdx-link naukri-btn-tertiary naukri-btn-x-small" type="button">+19 more</button>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active in last 2 months</span>
                              </div>
                            </div>
                          </div>
                        </a>
                        <hr class="horizontal-divider">
                      </div>
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=1b5d567f5aea16fd91&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=1b5d567f5aea16fd91&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=fb749916c5d202af3d3c63be660cf220595f0b5942110f110002405f5d0157421208100a6" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s3344767dbfacdded21d460494310315976012a875435d4f17d501e61a0fa3df611">
                              </div>
                              <div class="headline">
                                <div class="name">Dilip yadav</div>
                                <div class="current ellipsis" title="PHP Developer at technodroidz pvt lmt ">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">PHP </span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Developer</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">technodroidz pvt lmt</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="5y 8m">5y 8m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 8 Lacs">₹ 8 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="Noida (prefers Bengaluru,Delhi / NCR,Noida,Pune,Mumbai,Gurugram)">Noida (prefers Bengaluru,Delhi / NCR,Noida,Pune,Mumbai,Gurugram)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">React.js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">sql</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">html</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">php</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">codeigniter</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">jquery</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">javascript</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">mysql</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">laravel</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">node</span>
                                            <span class="hlite-inherit">.js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">mongodb</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Bootstrap</span>
                                          </span>
                                        </span>
                                      </span>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active in last 15 days</span>
                              </div>
                            </div>
                          </div>
                        </a>
                        <hr class="horizontal-divider">
                      </div>
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=6b12a64c7c86026958&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=6b12a64c7c86026958&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=058d5f764bdd14dc523ca2b532d3d804595c0f534d100b140002405f5d0157421208100a6" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s3a7b5399034ce4923203fd08b0338b21e2582c5384f0add723cca963134b2ccd21">
                              </div>
                              <div class="headline">
                                <div class="name">Deepak goswami</div>
                                <div class="current ellipsis" title="Full Stack Web Developer at Waffle Bytes Pvt Ltd ">
                                  <span class="hlite">
                                    <span class="hlite-inherit">Full</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Stack</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"> Web </span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Developer</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">Waffle Bytes Pvt Ltd</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="4y 0m">4y 0m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 5 Lacs">₹ 5 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="Noida (prefers Gurugram,Delhi / NCR)">Noida (prefers Gurugram,Delhi / NCR)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite">
                                            <span class="hlite-inherit">Mern</span>
                                          </span>
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit"></span>
                                          </span>
                                          <span class="hlite">
                                            <span class="hlite-inherit">Stack</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">React.Js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">Node</span>
                                            <span class="hlite-inherit">.Js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">Node</span>
                                            <span class="hlite-inherit"> Api</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">Node</span>
                                            <span class="hlite-inherit"> Express</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Nextjs</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Pwa</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">MongoDB</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">MySQL</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <button class="more rdx-link naukri-btn-tertiary naukri-btn-x-small" type="button">+3 more</button>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active in last 15 days</span>
                              </div>
                            </div>
                          </div>
                        </a>
                        <hr class="horizontal-divider">
                      </div>
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=f82ee83696ec4db4b01e99b276346fdc&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=f82ee83696ec4db4b01e99b276346fdc&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=9b9075085867b09227ec3c11941f180d595a0a5943170a190702405f5d0157421208100a6" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s339952a56221594849406ececc6caff5fe60d771a37b1b0bfb70e7fb492673bce1">
                              </div>
                              <div class="headline">
                                <div class="name">Vinay Rana</div>
                                <div class="current ellipsis" title="Fullstack Software Developer at IDC Technologies ">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Fullstack Software </span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Developer</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">IDC Technologies</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="4y 0m">4y 0m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 9.50 Lacs">₹ 9.50 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="New Delhi (prefers Gurugram,Noida,Delhi / NCR,Remote,Bengaluru)">New Delhi (prefers Gurugram,Noida,Delhi / NCR,Remote,Bengaluru)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite">
                                            <span class="hlite-inherit">Full</span>
                                          </span>
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit"></span>
                                          </span>
                                          <span class="hlite">
                                            <span class="hlite-inherit">Stack</span>
                                          </span>
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit"></span>
                                          </span>
                                          <span class="hlite">
                                            <span class="hlite-inherit">Developer</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">MEAN</span>
                                            <span class="hlite-inherit"></span>
                                          </span>
                                          <span class="hlite">
                                            <span class="hlite-inherit">Stack</span>
                                          </span>
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit"></span>
                                          </span>
                                          <span class="hlite">
                                            <span class="hlite-inherit">Developer</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">javascript</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">java</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">python</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">html</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">aws</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">node</span>
                                            <span class="hlite-inherit">.js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">jenkins</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">docker</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <button class="more rdx-link highlight naukri-btn-tertiary naukri-btn-x-small" type="button">+21 more</button>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active in last 7 days</span>
                              </div>
                            </div>
                          </div>
                        </a>
                        <hr class="horizontal-divider">
                      </div>
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=45e8e82510a34135b4f8888cb778c1e9&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=45e8e82510a34135b4f8888cb778c1e9&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=7c380a3b8283c1b4700337d7bb0b890d59550856481b08130102405f5d0157421208100a6" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s37222cf4a81f177056aa4f845efbc780dc394802c698e48344e37360be50f14d11">
                              </div>
                              <div class="headline">
                                <div class="name">deepak kumar</div>
                                <div class="current ellipsis" title="Full Stack Laravel Developer at Insight LCS Pvt. Ltd. ">
                                  <span class="hlite">
                                    <span class="hlite-inherit">Full</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Stack</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"> Laravel </span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Developer</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">Insight LCS Pvt. Ltd.</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="4y 6m">4y 6m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 4.80 Lacs">₹ 4.80 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="Noida (prefers Remote)">Noida (prefers Remote)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">OOP</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">MySQL</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">Javascript</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Laravel PHP Framework</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Rest Api Development</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">JQuery</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">React.Js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Docker</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <button class="more rdx-link naukri-btn-tertiary naukri-btn-x-small" type="button">+9 more</button>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active 2 days ago</span>
                              </div>
                            </div>
                          </div>
                        </a>
                        <hr class="horizontal-divider">
                      </div>
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=1d1abd1c5d1b94f389&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=1d1abd1c5d1b94f389&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=8f6d3ae5c7fc7933d0871c1c48f08fa6505c0d584d10081410104658550f594b1208186" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s32df329f9eefa874fee4363428bb826a2662b8a7ae53f696511e9705feb5a8cae1">
                              </div>
                              <div class="headline">
                                <div class="name">Sunil Maury</div>
                                <div class="current ellipsis" title="PHP Web Developer at Halcom Marketing Pvt Ltd ">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">PHP Web </span>
                                  </span>
                                  <span class="hlite">
                                    <span class="hlite-inherit">Developer</span>
                                  </span>
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit"></span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">Halcom Marketing Pvt Ltd</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="6y 6m">6y 6m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 7 Lacs">₹ 7 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="Ghaziabad (prefers Noida,Delhi / NCR,Remote)">Ghaziabad (prefers Noida,Delhi / NCR,Remote)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">SEO</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Pyspark</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Numpy</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Pandas</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">HTML</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">CSS</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">MySQL</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">PHP</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Bootstrap</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">jQuery</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Laravel</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">API</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Ajax</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Python</span>
                                          </span>
                                        </span>
                                      </span>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active in last 15 days</span>
                              </div>
                            </div>
                          </div>
                        </a>
                        <hr class="horizontal-divider">
                      </div>
                      <div>
                        <a target="_blank" href="/v3/preview?uniqId=4e92a3110e3bc7c697&amp;sid=6650051176&amp;hfFlowName=simcv&amp;pageUid=4e92a3110e3bc7c697&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;parentHighLightingKey=6650051176-1&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;tabKey=profile&amp;principalUserId=185755686&amp;uresid=d2188a98fe15cf652c7209f8bea50134595e0a534e1a0a130602405f5d0157421208100a6" class="link ext profile-card">
                          <div class="miniTuple">
                            <div class="summary flex-row flex-aic">
                              <div class="profile-image">
                                <img class="avatar-image" alt="candidate profile" src="https://p.naukri.com/jphoto/s3572bfbdd0479c4ef7f384c02a6995e7501719e11b9555fd318b270041d7874411">
                              </div>
                              <div class="headline">
                                <div class="name">AKANSHA BHARGAVA</div>
                                <div class="current ellipsis" title="Consultant at EY ">
                                  <span class="hlite-inherit">
                                    <span class="hlite-inherit">Consultant </span>
                                  </span> at <span class="hlite-inherit">
                                    <span class="hlite-inherit">EY</span>
                                  </span>
                                </div>
                              </div>
                            </div>
                            <div class="body">
                              <div class="exp-ctc flex-row flex-aic">
                                <div class="meta-data">
                                  <i class="ico ico-work naukri-icon naukri-icon-work"></i>
                                  <span class="card-detail" title="5y 0m">5y 0m</span>
                                </div>
                                <div class="meta-data">
                                  <i class="ico naukri-icon naukri-icon-account_balance_wallet"></i>
                                  <span class="card-detail" title="₹ 8.50 Lacs">₹ 8.50 Lacs</span>
                                </div>
                              </div>
                              <div class="location meta-data">
                                <i class="ico ico-place naukri-icon naukri-icon-place"></i>
                                <span class="loc ellipsis card-detail" title="New Delhi (prefers New Delhi)">New Delhi (prefers New Delhi)</span>
                              </div>
                              <div class="skills meta-data">
                                <div class="detail  key-skills-wrap">
                                  <span class="key-skills">
                                    <span class="read-more">
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="assessed-key-skill">
                                            <div class="naukri-tooltip-wrapper">
                                              <i class="verified_badges naukri-icon naukri-icon-verified_badges"></i>
                                            </div>
                                            <span class="txt assessedSkill">
                                              <span class="hlite-inherit">
                                                <span class="hlite-inherit">HTML</span>
                                              </span>
                                            </span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">React.js</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Laravel PHP</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">CSS</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span style="font-weight: bold;">Javascript</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Bootstrap</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">MySQL</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">MVC</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">PHP</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">jQuery</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">Ajax</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <span class="cand-skill">
                                        <span class="skill">
                                          <span class="hlite-inherit">
                                            <span class="hlite-inherit">PHP </span>
                                          </span>
                                          <span class="hlite">
                                            <span class="hlite-inherit">Developer</span>
                                          </span>
                                          <span class="pipe">|</span>
                                        </span>
                                      </span>
                                      <button class="more rdx-link naukri-btn-tertiary naukri-btn-x-small" type="button">+4 more</button>
                                    </span>
                                  </span>
                                </div>
                              </div>
                              <div class=" mini-tuple-footer">
                                <span class="attach-cv-info" title="CV Attached">
                                  <i class="ico naukri-icon naukri-icon-attach_file"></i>
                                  <span class="item-value text">CV</span>
                                </span>
                                <span class="active-date-info text">Active in last 15 days</span>
                              </div>
                            </div>
                          </div>
                        </a>
                      </div>
                      <a target="_blank" href="/v3/simcv?uniqueId=8b679266d1382e73c90795d14293125a5c580c04431b0b475712440e595a0248415b420643470a555a51481b0915564552595a09594c1b081002196&amp;activeIn=3650&amp;pFlow=SEARCH_ID&amp;pFlowId=2dad2395c7d750d0d79d3eb54e39926f&amp;uname=undefined&amp;parentHighLightingKey=6650051176-1&amp;principalUserId=185755686&amp;hfFlowName=simcv&amp;parentSid=6650051176&amp;sidGroupId=2dad2395c7d750d0d79d3eb54e39926f&amp;pageNo=1&amp;resPerPage=40" class="link ext view-all-sim-cv">
                        <button class="view-all-button naukri-btn-tertiary naukri-btn-regular" type="button">View all similar profiles <i class="arrow-forward naukri-icon naukri-icon-arrow_forward icon"></i>
                        </button>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="scroll ">
              <div class="icon scroll-ico">
                <svg width="36" height="36" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="18" cy="18" r="18" fill="#253858"></circle>
                  <path d="m11.334 18 1.175 1.175 4.658-4.65v10.142h1.667V14.525l4.65 4.658L24.667 18l-6.666-6.667L11.334 18Z" fill="#fff"></path>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="alerts-wrapper" aria-live="polite" aria-atomic="true"></div>
      <output aria-live="polite" id="announcement"></output>
      <div class="captcha" style="display: none;">
        <div class="overlay"></div>
        <div class="wrap">
          <img src="//static.naukimg.com/s/7/112/2e35af7018fdf3cb5849.png" alt="">
          <p>To continue your request please check the box to const us know you’re human</p>
          <div class="recaptcha">
            <div id="g-recaptcha"></div>
          </div>
        </div>
      </div>
    </div>
    <div id="cap-container">
      <a href="https://resdex.naukri.com/v2/click-detect/frontend?pageName=preview">
        <div style="height:0px; width:0px;"></div>
      </a>
      <a id="product5678" href="https://resdex.naukri.com/v2/click-detect/frontend?pageName=preview">
        <span style="display:none;"></span>
      </a>
      <a href="https://resdex.naukri.com/v2/click-detect/frontend?pageName=preview">
        <div style="position:absolute; left:-1250px;"></div>
      </a>
      <a href="https://resdex.naukri.com/v2/click-detect/frontend?pageName=preview" style="display:none;"></a>
    </div>
    <div class="footerHtml">
      <div class="gnb_app_footer">
        <div class="tTkDq" style="background-color: rgb(255, 255, 255);">
          <div class="C3K7B">
            <div class="Z1l0y">
              <a href="//recruit.naukri.com/homePage/index">
                <div class="bJw_J TTHbd l1s4P"></div>
              </a>
              <div class="VdhxH">Recruiter Helpline</div>
              <div class="VdhxH">1800 102 5558</div>
              <div class="yWg34">10:00 AM to 6:00 PM, Mon - Sat</div>
              <div class="QAmJR">
                <div class="eHaig">Contact Us</div>
                <div class="eGGSW">&nbsp;-&nbsp;</div>
                <div class="eHaig">Report a Problem</div>
              </div>
            </div>
            <div class="Z1l0y">
              <div class="dRFuF">Recruiter Solutions</div>
              <div class="eHaig">Home</div>
              <div class="eHaig">Jobs &amp; Responses</div>
              <div class="eHaig">Resdex</div>
              <div class="eHaig">Analytics</div>
            </div>
            <div class="Z1l0y">
              <div class="dRFuF">Information</div>
              <div class="eHaig">Jobseeker Home</div>
              <div class="eHaig">About Us</div>
              <div class="eHaig">Clients</div>
              <div class="eHaig">Careers</div>
              <div class="eHaig">Terms &amp; Conditions</div>
              <div class="eHaig">Privacy policy</div>
              <div class="eHaig">FAQs</div>
              <div class="eHaig">Site Map</div>
            </div>
            <div class="Z1l0y">
              <div class="dRFuF">Legal</div>
              <div class="eHaig">Grievances</div>
              <div class="eHaig">Summons and Notice</div>
              <div class="eHaig">Trust and Safety</div>
              <div class="eHaig">Whitehat</div>
            </div>
          </div>
          <div class="wLq3h">All rights reserved @2024 Info Edge (India) Ltd.</div>
        </div>
      </div>
    </div>
    <link rel="stylesheet" type="text/css" href="https://static.naukimg.com/s/7/102/c/common_gnb_app.62e3be6e.css" media="all">
    <link rel="stylesheet" type="text/css" href="https://static.naukimg.com/s/7/102/c/gnb_app.49ecdd9f.css" media="all">
    <div>
      <div id="twoseven-ext-tab-media-modal" class="twoseven-ext-tab-media-modal" style="display: none;">
        <!-- Modal content -->
        <div class="twoseven-ext-tab-media-modal-content">
          <div class="iframe-container" style="height: 100%; width: 100%;">
            <span class="close">×</span>
          </div>
        </div>
      </div>
    </div>
    <iframe id="nr-ext-rsicon" style="position: absolute; display: none; width: 50px; height: 50px; z-index: 2147483647; border-style: none; background: transparent;"></iframe>
    <div style="position: absolute; top: 0px; left: 0px; width: 100%;">
      <div>
        <div class="naukri-dropdown naukri-dropdown-show-arrow naukri-dropdown-placement-bottomLeft  naukri-dropdown-hidden" style="left: -757px; top: -936.6px; position: relative;">
          <div class="naukri-dropdown-arrow"></div>
          <div>
            <div>
              <ul class="set-reminder-drop-layer drop-layer" role="menu">
                <li role="menuitem" class="opt reminder-opt" tabindex="0" aria-label="For call later">For call later</li>
                <li role="menuitem" class="opt reminder-opt" tabindex="0" aria-label="For interview follow up">For interview follow up</li>
                <li role="menuitem" class="opt reminder-opt" tabindex="0" aria-label="For sending JD">For sending JD</li>
                <li role="menuitem" class="opt reminder-opt" tabindex="0" aria-label="For other task">For other task</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <input id="addTaskBtn" type="hidden">
    <grammarly-desktop-integration data-grammarly-shadow-root="true"></grammarly-desktop-integration>
    <div style="position: absolute; top: 0px; left: 0px; width: 100%;">
      <div>
        <div class="naukri-tooltip timeline-tooltip   naukri-tooltip-default naukri-tooltip-placement-bottomLeft  naukri-tooltip-hidden" style="left: 513px; top: 1361.4px;">
          <div class="naukri-tooltip-content">
            <div class="naukri-tooltip-arrow"></div>
            <div class="naukri-tooltip-inner" role="tooltip">
              <div class="naukri-tooltip-overlay">
                <div>
                  <div>
                    <div class="flex-row exp">
                      <div class="logo flex-row flex-aic flex-jcc even ">
                        <img src="https://img.naukimg.com/logo_images/groups/v1/4598093.gif" alt="Girikon Solutions Pvt Ltd logo" class=" " data-src="https://img.naukimg.com/logo_images/groups/v1/4598093.gif">
                      </div>
                      <div class="detail-info">
                        <div>
                          <div class="heading">Fullstack Developer</div>
                          <div class="sub-heading">at Girikon Solutions Pvt Ltd</div>
                        </div>
                        <div class="text">Apr '23 till date ( 10m)</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

print("\n****************************************************************************************************************************************************\n")
print("\nPROPER FORMATTING OF JSON DATA:\n")

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize an empty dictionary to store scraped data
scraped_data = {}

# Scrape Full Name
full_name_tag = soup.find('span', {'class': 'hlite-inherit'})
scraped_data['full_name'] = full_name_tag.text.strip() if full_name_tag else ''
print("\n---Full Name---\n")
print(scraped_data['full_name'])

# Scrape First Name
scraped_data['first_name'] = scraped_data['full_name'].split()[0] if scraped_data['full_name'] else ''
print("\n---Frist Name---\n")
print(scraped_data['first_name'])

# Scrape Last Name
scraped_data['last_name'] = scraped_data['full_name'].split()[-1] if scraped_data['full_name'] else ''
print("\n---Last Name---\n")
print(scraped_data['last_name'])

# Scrape Industry
industry_tag = soup.find('div', {'class': 'OesXg'})
scraped_data['industry'] = industry_tag.text.strip() if industry_tag else ''
print("\n---Industry---\n")
print(scraped_data['industry'])

# Scrape Annual Salary
annual_salary_tag = soup.find('span', {'title': '₹ 9.50 Lacs (expects: ₹ 10.0 Lacs)'})
scraped_data['annual_salary'] = annual_salary_tag.text.strip() if annual_salary_tag else ''
scraped_data['annual_salary'] = scraped_data['annual_salary'].replace("\u20b9","")
print("\n---Annual salary---\n")
print(scraped_data['annual_salary'])

# Scrape Current Companyy
soup = BeautifulSoup(html_content, 'html.parser')
# Extracting the company name
company_name = soup.find_all('span', {'class': 'hlite-inherit'})
curr_cmp_tag = company_name[8]
scraped_data['curr_cmp'] = curr_cmp_tag.text.strip() if curr_cmp_tag else ''
print("\n---Current company---\n")
print(scraped_data['curr_cmp'])


# Scrape Education
edu_tag = soup.find('span', {'title': 'BCA Ch Charan Singh University (CCSU), Meerut, 2020'}).find('span',{'class':'hlite-inherit'})
scraped_data['education'] = edu_tag.text.strip() if edu_tag else ''
print("\n---Education---\n")
print(scraped_data['education'])

# Scrape Skills
skill_divs = soup.find_all("div", class_="focusable suggestor-tag")

# Extract skill names from each <div> element and store them in a dictionary
a = {"abc": []}
for div in skill_divs:
    skill_name = div.find("span", class_="txt ellipsis")["title"]
    a["abc"].append(skill_name)
scraped_data['skills'] = a["abc"]
print("\n---Skills---\n")
print(scraped_data['skills'])

# Scrape Work Summary
# Extract work summary
work_summary = soup.find('h4').text.strip()
# Extract individual details
industry = soup.find('div', string='Industry').find_next_sibling('div').text.strip()
industry = industry.replace('\n', '')
department = soup.find('div', string='Department').find_next_sibling('div').text.strip()
department = department.replace('\n', '')
role = soup.find('div', string='Role').find_next_sibling('div').text.strip()
role = role.replace('\n', '')
# Extract technical skills
technical_skills = soup.find('div', class_='Ju-0N').text.strip()
technical_skills = technical_skills.replace('\n', '')
# Combine all information into a single variable
scraped_data['work_sum'] = f"""
Work Summary: {work_summary}
Industry: {industry}
Department: {department}
Role: {role}
Technical Skills: {technical_skills}
"""
scraped_data['work_sum'] = scraped_data['work_sum'].replace('\n', '\n')
print("\n---Work Summary---\n")
print(scraped_data['work_sum'])

# Scrape Work Experience
# Find all work experience cards
work_experience_cards = soup.find_all('div', class_='work-exp-card')
# Initialize a list to store each work experience
work_experience_list = []
# Iterate over each work experience card
company_spans = soup.select('.exp-label > div > span > span')
# Extract company names from each span element
company_names_list = [span.get_text(strip=True) for span in company_spans]
i=2
for card in work_experience_cards:
    # Extract data from the card
    company_name = company_names_list[i]
    i=i+3
    job_title_1 = card.find('div', class_='exp-label').find('span').find('span').text.strip()
    job_title = card.find('div', class_='exp-label').find('span', class_='hlite').find('span').text.strip()
    job_title=job_title_1+" " +job_title
    tenure = card.find('div', class_='dates').text.strip()
    description = card.find('div', class_='desc').text.strip()
    # Store the extracted data in a dictionary
    work_experience = {
        'company_name': company_name,
        'job_title': job_title,
        'tenure': tenure,
        'description': description
    }
    # Append the work experience to the list
    work_experience_list.append(work_experience)
# Store the list of work experiences in the scraped_data dictionary under the key 'work_exp'
scraped_data['work_exp']= work_experience_list 
# Print the scraped data
print("\n---Work Experince---\n")
for exp in scraped_data['work_exp']:
    print(f"Company Name: {exp['company_name']}")
    print(f"Job Title: {exp['job_title']}")
    print(f"Tenure: {exp['tenure']}")
    print(f"Description: {exp['description']}\n")

# # Scrape IT Skills
# Find all rows with class 'tr'
it_skills_list = []
skill_rows = soup.find_all('div', class_='tr')
for row in skill_rows:
    skill_name_element = row.find('div', class_='data-cell skills')
    version_element = row.find('div', class_='data-cell version')
    last_used_element = row.find('div', class_='data-cell lastUsed')
    experience_element = row.find('div', class_='data-cell exp')
    if skill_name_element and version_element and last_used_element and experience_element:
        skill_name = skill_name_element.text.strip()
        version = version_element.text.strip()
        last_used = last_used_element.text.strip()
        experience = experience_element.text.strip()
        it_skills_list.append({
            'Skill': skill_name,
            'Version': version,
            'Last Used': last_used,
            'Experience': experience
        })
scraped_data['it_skills']=it_skills_list
print("\n----IT Skills---\n")
for skill in scraped_data['it_skills']:
    print(f"Skill: {skill['Skill']}")
    print(f"Version: {skill['Version']}")
    print(f"Last Used: {skill['Last Used']}")
    print(f"Experience: {skill['Experience']}\n")

#Scrape Other Details
# Find the section with personal details
personal_details_section = soup.find('div', class_='nqhGZ')
# Extract individual details
date_of_birth = personal_details_section.find('div', class_='table-cell RwJYw').text
gender = personal_details_section.find('div', class_='table-cell gOeNe').text
marital_status = personal_details_section.find('div', class_='table-cell _0YyRI').text
category = personal_details_section.find('div', class_='table-cell _9HpRi').text
physically_challenged = personal_details_section.find('div', class_='table-cell _64mvN').text
# Store the extracted details in a dictionary
scraped_data['other_details'] = f"""
        Date of Birth: {date_of_birth},
        Gender: {gender},
        Marital Status: {marital_status},
        Category: {category},
        Physically Challenged: {physically_challenged}

"""
print("\n---Other Details---\n")
print(scraped_data['other_details'])

json_data = json.dumps(scraped_data, indent=2)

# Print the JSON data
print("\n***************************************************************************************************************************************************\n")
print("\nUNFORMATED VIEW OF JSON OBJECT:\n\n")
print(json_data)
print("\n****************************************************************************************************************************************************\n")
