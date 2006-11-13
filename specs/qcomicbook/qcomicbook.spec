# $Id$
# Authority: dries
# Upstream: Pawel Stolowski <yogin$linux,bydg,org>

Summary: Viewer for comic book archives
Name: qcomicbook
Version: 0.3.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://linux.bydg.org/~yogin/

Source: http://linux.bydg.org/~yogin/qcomicbook-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++, imlib2-devel

%description
QComicBook is a viewer for rar, zip, cbr, and cbz format comic book
archives containing JPEG or PNG images. Its features include
automatic handling of archives, full-screen mode, page scaling, and
mouse or keyboard navigation.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=qcomicbook
Comment=Read comics
Exec=qcomicbook
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF

%build
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/qcomicbook*
%{_bindir}/qcomicbook
%{_datadir}/applications/*qcomicbook.desktop
%{_datadir}/qcomicbook/

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.3-1
- Updated to release 0.3.3.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0-1
- Updated to release 0.3.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.7-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.7-1
- Updated to release 0.2.7.

* Thu Dec 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1
- Updated to release 0.2.6.

* Fri Dec 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.5-1
- Initial package.
