# $Id: $

# Authority: dries
# Upstream: 

Summary: Intuitive GUI for PostgreSQL management
Name: pgst
Version: 1.2.2
Release: 1
License: Artistic
Group: Applications/Databases
URL: http://sourceforge.net/projects/pgst/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/pgst/pgst-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires: 

%description
Pgst is an intuitive graphical user interface for PostgreSQL management.

%prep
%setup -n %{name}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=PostgreSQL SQL Tool
Comment=PostgreSQL database management tool
Icon=%{_datadir}/pgst/pixmaps/db-editor.png
Exec=/bin/bash %{_datadir}/pgst/pgst.sh
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Database;X-Red-Hat-Extra;
EOF

%build
# python prog

%install
# strange install script
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}
%{__tar} -xf setup.tar -C %{buildroot}%{_datadir}
%{__sed} -i 's/python2\.2/python/g;' %{buildroot}%{_datadir}/pgst/pgst.py*
%{__sed} -i 's|cd .*|cd %{_datadir}/pgst|g;' %{buildroot}%{_datadir}/pgst/pgst.sh

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
# %doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%{_datadir}/pgst
%{_datadir}/applications/*.desktop

%changelog
* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Initial package.
