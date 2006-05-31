# $Id$
# Authority: dries
# Upstream: Nikolay Pultsin <geometer$mawhrin,net>

%define desktop_vendor rpmforge

Summary: E-book reader
Name: fbreader
Version: 0.7.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://only.mawhrin.net/fbreader/

Source: http://only.mawhrin.net/fbreader/fbreader-sources-%{version}.tgz
Patch: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: enca, qt-devel >= 3.2, kdelibs-devel, gcc-c++

%description
FBReader is an e-book reader for Linux PDAs and desktop computers.
FBReader supports several e-book formats: plucker, palmdoc, zTXT, 
HTML, fb2, and plain text.  

%prep
%setup
%patch -p1

%{__cat} <<EOF >fbreader.desktop
[Desktop Entry]
Name=FBReader
Comment=Read various ebook formats
Exec=FBReader
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%{__make} %{?_smp_mflags} EXTERNALINCLUDE=-I${QTDIR}/include MOC=moc UILIBS="-L${QTDIR}/lib -lqt-mt" INSTALLDIR=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%makeinstall EXTERNALINCLUDE=-I${QTDIR}/include MOC=moc UILIBS="-L${QTDIR}/lib -lqt-mt" INSTALLDIR=%{_prefix} DESTDIR=%{buildroot}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	fbreader.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/FBReader
%{_datadir}/FBReader/
%{_datadir}/applications/%{desktop_vendor}-fbreader.desktop

%changelog
* Fri May 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Updated to release 0.7.3.

* Fri Feb 17 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Wed Dec 07 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-0.b
- Initial package.
