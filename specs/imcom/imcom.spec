# $Id: $

# Authority: dries
# Upstream: Casey Crabb <crabbkw@nafai.dyndns.org>

Summary: A command line Jabber client written in Python
Name: imcom
Version: 1.32
Release: 2
License: Other
Group: Applications/Internet
URL: http://imcom.floobin.cx/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://imcom.floobin.cx/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: python
Requires: python

%description
IMCom is a command-line Jabber client written in Python by Casey Crabb.
IMCom supports the following Jabber technologies:
* Sending/Receiving Messages
* Presence Updates
* File Transfer
* SSL Connections
* vCard retrieval and submission
* Basic Support of the jabber:iq:admin namespace
* Agent and Transport Registration
* Handles Jabber Resources properly
* Jabber Group Chat
* Jabber Multi-User-Chat (JEP0045)
* Jabber:x:data (JEP0004) (Only partial support, submit only, not retrieve)

IMCom supports the following UI stuffs:
* Command customization
* Multi-line messages
* Sending a message to a particular resource a user is logged in from
* ignore and lurker group support
* Auto-Status
* Reply/Again (sending a message to the last person to message you and sending
  a message to the last person you messaged
* Color customization
* Command Customization
* Multiple profile support
* Generic module support

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall docdir=%{buildroot}/tmpdoc
rm -Rf %{buildroot}/tmpdoc

%files
%defattr(-,root,root,0755)
%doc README CONTRIBUTORS LICENSE README.autostatus WHATSNEW TODO docs/advanced.html docs/commands.html docs/download.html docs/imcomrc.html docs/news.html docs/template.html docs/whatis.html docs/jabberbutton.png docs/style.css
%{_bindir}/imcom
%{_datadir}/imcom
%{_datadir}/man/man1/imcom.1.gz

%changelog
* Mon Jan 26 2004 Dries Verachtert <dries@ulyssis.org> 1.32-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.32-1
- first packaging for Fedora Core 1
