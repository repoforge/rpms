# $Id$
# Authority: dries
# Upstream: fefcas$gmail,com

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Typing tutor
Name: klavaro
Version: 1.1.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://klavaro.sourceforge.net/en/

Source: http://dl.sf.net/klavaro/klavaro-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel
BuildRequires: gcc-c++, gettext, bison
BuildRequires: kdelibs-devel, desktop-file-utils
BuildRequires: gtk2-devel >= 2.6

%description
Klavaro  is a touch typing tutor that is very
flexible and supports customizable keyboard
layouts. Users can edit and save new or unknown
keyboard layouts, as the basic course provided by
the program was designed to not depend on specific
layouts.

%prep
%setup
%{__perl} -pi.orig -e 's| /var/games| \$(DESTDIR)/var/games|g;' src/Makefile.*

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Klavaro
Comment=Typing tutor
#Icon=name.png
Exec=klavaro
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=KDE;Application;Education;
EOF

%build
# otherwise it doesn't work
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man?/klavaro.1*
%{_bindir}/klavaro
%{_bindir}/klavaro_helper
%{_datadir}/klavaro/
%{_datadir}/applications/*.desktop

%changelog
* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Fri Jun 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Fri May 30 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.8-1
- Updated to release 1.0.8.

* Wed Jan 23 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1
- Updated to release 1.0.7.

* Sun Jan  6 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1
- Updated to release 1.0.6.

* Wed Dec  5 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Updated to release 1.0.5.

* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Updated to release 1.0.4.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Apr 01 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.9-1
- Updated to release 0.9.9.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Updated to release 0.9.8.

* Thu Apr 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Updated to release 0.9.7.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-3
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Wed Jan 11 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-2
- Changed optflags so it doesn't crash immediately, thanks to Andrew Ziem!

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Sep 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Update to release 0.9.2.

* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Update to release 0.9.1.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Update to release 0.9.

* Sat Sep 17 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Update to release 0.8.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Update to release 0.7.1.

* Sat Aug 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Update to release 0.6.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Update to release 0.5.

* Wed Jul 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Update to release 0.4.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
