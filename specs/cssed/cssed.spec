# $Id$

# Authority: dries

Summary: CSS stylesheets editor
Name: cssed
Version: 0.2.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://cssed.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/cssed/cssed-pre0.1-2.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: autoconf, make, gcc, gtk2-devel, gettext, vte-devel
Requires: gtk2, vte

# Screenshot: http://cssed.sourceforge.net/images/screens/screenshor_doc_menu.png
# ScreenshotURL: http://cssed.sourceforge.net/screenshots.html

%description
Cssed is a GTK2 application for creating and maintaining CSS style sheets.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n cssed-pre0.1

%build
autoconf
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
make install-strip
mkdir -p ${DESTDIR}/usr/share/applications/
cat > ${DESTDIR}/usr/share/applications/cssed.desktop <<EOF
[Desktop Entry]
Name=Cssed
Comment=A CSS editor
Exec=cssed
Terminal=0
Type=Application
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Base;
EOF

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/cssed
%{_datadir}/applications/cssed.desktop
%{_datadir}/cssed

%changelog
* Sun May 16 2004 Dries Verachtert <dries@ulyssis.org> 0.2.1-1
- update to 0.2.1

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.1.1pre-1
- first packaging for Fedora Core 1
