# $Id$
# Authority: fabian
# Upstream: 

Summary: GTK frontend for anyRemote
Name: ganyremote
Version: 5.9
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
Source0: http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
URL: http://anyremote.sourceforge.net/
Requires: pygtk2 >= 2.10
Requires: python-bluez >= 0.9.1
Requires: bluez-utils >= 3.7
Requires: anyremote >= 4.18.1
BuildRequires: desktop-file-utils
BuildRequires: gettext-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
gAnyRemote package is GTK GUI frontend for anyRemote 
(http://anyremote.sourceforge.net/). The overall goal of this project is to 
provide remote control service on Linux through Bluetooth, InfraRed, Wi-Fi 
or TCP/IP connection.

%prep
%setup -q

%build
%configure

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
desktop-file-install --vendor=""          \
  --add-category="System"                      \
  --delete-original                             \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_flash.png
%{_datadir}/pixmaps/%{name}_off.png
%{_datadir}/pixmaps/%{name}_light.png
%{_datadir}/pixmaps/%{name}.png
%{_defaultdocdir}/%{name}


%changelog

* Sun Jun 21 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 5.9-1
- Updated to 5.9 + Requires: correction for RPMforge inclusion (pybluez vs python-bluez)

* Mon Mar 30 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.8
- Add GuiAppModes tag handling

* Wed Mar 11 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.7
- Finnish and Swedish translation were added (thanks to Matti Jokinen)

* Mon Jan 19 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.6-1
- Check java client version on the web site

* Sun Dec 21 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.5.1-1
- Fix upload from web feature

* Sun Dec 14 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.5-1
- Handle GuiAppVersion parameter in configuration files. Add possibility
  to download java client from Web. Small Ubuntu-specific fixes.

* Wed Dec 3 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.4.2-1
- Fix detection of activity of bluetooth service

* Wed Nov 12 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.4.1-1
- Small corrections

* Fri Oct 17 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.4-1
- Enhanced edit configuration file window. Support application details 
  auto wrap. Added Bulgarian translation (thanks to Stanislav Popov)

* Wed Sep 24 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.3-1
- Add icons to menu and buttons.

* Mon Sep 8 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.2.1-1
- Small bugfixes.

* Thu Sep 4 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.2-1
- Added "Details" field to the main window.
  Added French translation.

* Tue Aug 19 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.1-1
- Added Czech and  Dutch translations.

* Mon Jul 21 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.0-1
- Fixed to work properly under RHEL4. Internationalization support.
  Added Austrian, Brazilian Portuguese, German, Hungarian, Spanish, Italian, 
  Polish and Russian translation.

* Sun Jun 29 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.0-1
- Small enhancements

* Sun May 25 2008 Mikhail Fedotov <anyremote at mail.ru> - 3.0-1
- Bugfixes and enhancements to better support anyremote-J2ME client v4.6 and
  anyremote2html v0.5.

* Sun Apr 20 2008 Mikhail Fedotov <anyremote at mail.ru> - 2.8-2
- Spec file correction.

* Sat Apr 19 2008 Mikhail Fedotov <anyremote at mail.ru> - 2.8-1
- Some small enhancements. Spec file correction.

* Mon Mar 03 2008 Mikhail Fedotov <anyremote at mail.ru> - 2.7-1
- Some small enhancements. Corrected to work properly with anyRemote v4.4.

* Tue Feb 26 2008 Mikhail Fedotov <anyremote at mail.ru> - 2.6-3
- Spec file correction

* Sun Feb 17 2008 Mikhail Fedotov <anyremote at mail.ru> - 2.6-2
- Spec file correction

* Mon Feb 15 2008 Mikhail Fedotov <anyremote at mail.ru> - 2.6-1
- Motorola RIZR Z3 support enhanced

