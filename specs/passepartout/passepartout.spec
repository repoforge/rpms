# $Id$
# Authority: dag
# Upstream: Fredrik Arnerup <e97_far$e,kth,se>

%define desktop_vendor rpmforge

Summary: Open Source desktop publishing application
Name: passepartout
Version: 0.6
Release: 1.2%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://www.stacken.kth.se/project/pptout/

Source: http://www.stacken.kth.se/project/pptout/files/passepartout-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm2, gcc-c++
BuildRequires: libxml++ >= 1.0

%description
Passepartout is an Open Source Desktop Publishing application for the
X Windows environment. The goal of this project is to create a system
capable of producing pre-press material of professional quality, but
also a useful tool for any enthusiast with access to a printer.

The main focus is on making it easy for the user to create publications
with a flexible layout, typical examples being magazines, brochures and
leaflets.

%prep
%setup

%{__cat} <<EOF >passepartout.desktop
[Desktop Entry]
Name=Passepartout Desktop Publishing
Comment=Create publications for magazines, brochures or leaflets
Icon=redhat-presentations.png
Exec=passepartout
Terminal=false
Type=Application
Categories=GNOME;Application;Graphics;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	passepartout.desktop

### Clean up docdir
%{__rm} -f doc/examples/Makefile*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING NEWS README
%doc doc/*.html doc/*.pp doc/*.xml doc/examples/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/xml/passepartout/
%exclude %{_docdir}/passepartout/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 12 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.4-0
- Updated to release 0.4.

* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Fixed desktop-file to start passepartout. (Peter Robertson)

* Thu Nov 20 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
