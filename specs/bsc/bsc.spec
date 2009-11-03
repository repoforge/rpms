# $Id$
# Authority: dries
# Upstream: PiotrPsz <piotr$beesoft,org>

%define desktop_vendor rpmforge

Summary: Beesoft Commander file manager
Name: bsc
Version: 2.27
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.beesoft.org/index.html

Source: http://www.beesoft.org/download/bsc_%{version}_src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, kdelibs-devel, qt-devel >= 3.2

%description
Beesoft Commander is a file manager (like Norton Commander) for Linux.

%prep
%setup -n bsc

%{__cat} <<EOF >bsc.desktop
[Desktop Entry]
Name=bsc
Comment=File manager
Exec=bsc
Type=Application
Categories=Application;Utilities;
Encoding=UTF-8
EOF

%build
qmake bsc.pro
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bsc %{buildroot}%{_bindir}/bsc

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	bsc.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#doc readme.txt
%{_bindir}/bsc
%{_datadir}/applications/%{desktop_vendor}-bsc.desktop

%changelog
* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 2.27-2
- Fix group tag.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.27-1
- Updated to release 2.27.

* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.26-1
- Updated to release 2.26.

* Sat Jul 29 2006 Dries Verachtert <dries@ulyssis.org> - 2.25-1
- Updated to release 2.25.

* Tue May 23 2006 Dries Verachtert <dries@ulyssis.org> - 2.22.-1
- Updated to release 2.22.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.21.-1
- Updated to release 2.21.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 2.20.-1
- Updated to release 2.20.

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 2.18.1.-1
- Updated to release 2.18.1.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.18.-1
- Updated to release 2.18.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.17.-1
- Updated to release 2.17.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.16.-1
- Updated to release 2.16.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.15.-1
- Updated to release 2.15.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.14.-1
- Updated to release 2.14.

* Mon Feb 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.13.1.-1
- Updated to release 2.13.1.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.12.1.-1
- Updated to release 2.12.1.

* Tue Feb 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Updated to release 2.12.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Mon Jan 16 2006 Dries Verachtert <dries@ulyssis.org> - 2.07-1
- Updated to release 2.07.

* Fri Jan 13 2006 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Updated to release 2.05.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Sat Dec 17 2005 Dries Verachtert <dries@ulyssis.org> - 2.02.2-1
- Updated to release 2.02.2.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 2.02.1-1
- Initial package.
