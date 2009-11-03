# $Id$
# Authority: dries

Summary: Graphical frontend to doodle
Name: kdoodle
Version: 0.2.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.c2root.be/kdoodle/

Source: http://www.c2root.be/kdoodle/KDoodle-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext, doodle-devel

%description
KDoodle is a graphical frontend to doodle. It provides indexed lookups and 
automatic opening of a returned file as well as saving configuration files.

%prep
%setup -n KDoodle-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=KDoodle
Comment=Frontend for doodle
Exec=/usr/bin/KDoodle
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Utility;
Encoding=UTF-8
EOF

%build
qmake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D KDoodle %{buildroot}%{_bindir}/KDoodle

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/KDoodle
%{_datadir}/applications/*-kdoodle.desktop

%changelog
* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.3
- Initial package.
