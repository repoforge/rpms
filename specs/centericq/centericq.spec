# $Id$
# Authority: rudolf


Summary: Console ncurses based ICQ2000, Yahoo!, MSN, AIM, IRC client
Name: centericq
Version: 4.21.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://konst.org.ua/centericq/

Source: http://konst.org.ua/download/centericq-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gpgme-devel, curl-devel, libjpeg-devel
BuildRequires: ncurses-devel

%description
centericq is a text mode menu- and window-driven IM interface.

Currently ICQ2000, Yahoo!, MSN, AIM TOC, IRC, Gadu-Gadu and Jabber
protocols are supported. centericq allows you to send, receive,
and forward messages, URLs and, SMSes, mass message send, search
for users (including extended "whitepages search"), view users'
details, maintain your contact list directly from the program
(including non-icq contacts), view the messages history, register
a new UIN and update your details, be informed on receiving email
messages, automatically set away after the defined period of
inactivity (on any console), and have your own ignore, visible and
invisible lists. It can also associate events with sounds, has support
for Hebrew and Arabic languages and allows to arrange contacts into
groups. Internal RSS reader and a client for LiveJournal are provided.

%prep
%setup

%build
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*.?.gz
%{_bindir}/centericq
%{_bindir}/cicqconv
%{_bindir}/cicqsync
%{_datadir}/centericq/

%changelog
* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 4.21.0-1
- Updated to release 4.21.0.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 4.20.0-1
- Updated to release 4.20.0.

* Mon Jan 20 2003 Che
- version upgrade

* Thu Dec 18 2002 Che
- version upgrade

* Thu Dec 05 2002 Che
- version upgrade

* Sat Nov 02 2002 Che
- initial rpm release
