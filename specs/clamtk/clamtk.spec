# $Id$
# Authority: dag
# Upstream: Dave M <dave,nerd$gmail,com>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Easy to use front-end for ClamAV
Name: clamtk
Version: 2.13
Release: 1.2
License: Perl
Group: Applications/File
URL: http://clamtk.sourceforge.net/

Source: http://dl.sf.net/clamtk/clamtk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: perl-Gtk2, perl-File-Find-Rule, perl-Date-Calc, perl-libwww-perl
Requires: clamav >= 0.83, clamav-db

Obsoletes: clamtk2

%description
ClamTk is a front-end, point and click gui for ClamAV on Linux systems.
It supports easy signature-updates.

%prep
%setup

%{__cat} <<EOF >clamtk.desktop
[Desktop Entry]
Name=ClamTk Virus Scanner
Comment=Scan your system for viruses.
Exec=clamtk
Icon=clam.xpm
Terminal=false
Type=Application
Categories=Application;Utility;
StartupNotify=false
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 clamtk %{buildroot}%{_bindir}/clamtk
%{__install} -Dp -m0644 clam.xpm %{buildroot}%{_datadir}/pixmaps/clam.xpm

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 clamtk.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/clamtk.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --delete-original \
		--vendor %{desktop_vendor}                 \
		--dir %{buildroot}%{_datadir}/applications \
		--add-category X-Red-Hat-Base              \
		clamtk.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES clamtk clamtk.pl DISCLAIMER LICENSE README
%{_bindir}/clamtk
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-clamtk.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/clamtk.desktop}
%{_datadir}/pixmaps/clam.xpm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.13-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Sun Aug 21 2005 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Thu May 19 2005 Dag Wieers <dag@wieers.com> - 1.99-1
- Updated to release 1.99.

* Thu May 05 2005 Dag Wieers <dag@wieers.com> - 1.97-1
- Updated to release 1.97.
- Added changes from Dave M.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 1.0.10-1
- Initial package. (using DAR)
