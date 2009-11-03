# $Id$
# Authority: dries
# Upstream: Casey Crabb <crabbkw$nafai,dyndns,org>

Summary: Command line Jabber client written in Python
Name: imcom
Version: 1.33
Release: 1.2%{?dist}
License: Other
Group: Applications/Internet
URL: http://imcom.floobin.cx/

Source: http://imcom.floobin.cx/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
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

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall docdir=%{buildroot}/tmpdoc
%{__rm} -rf %{buildroot}/tmpdoc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIBUTORS LICENSE README README.autostatus TODO WHATSNEW
%doc docs/advanced.html docs/commands.html docs/download.html docs/imcomrc.html
%doc docs/jabberbutton.png docs/news.html docs/template.html docs/whatis.html
%doc docs/style.css
%{_bindir}/imcom
%{_datadir}/imcom
%{_mandir}/man1/imcom.1.gz

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.33-1.2
- Rebuild for Fedora Core 5.

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> 1.33-1
- Update to release 1.33.

* Mon Jan 26 2004 Dries Verachtert <dries@ulyssis.org> 1.32-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.32-1
- first packaging for Fedora Core 1

