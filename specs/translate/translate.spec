# $Id: $

# Authority: dries
# Upstream: 

Summary: Aids with localization of software and conversion between different translation formats
Name: translate
Version: 0.8b1
Release: 1
License: GPL
Group: Development/Tools
URL: http://translate.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/translate/translate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

%description
Translate is a project to aid in localization of software. It deals with 
conversion between different translation formats (such as gettext-based 
.po formats, OpenOffice.org formats, and Mozilla formats). It also contains 
tools to help process localizations etc.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install --root=%{buildroot} 
# --install-lib=%{_libdir}/translate --install-scripts=%{_bindir}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_libdir}/python*/site-packages/_csv.*
%{_libdir}/python*/site-packages/translate

%changelog
* Sat May 23 2004 Dries Verachtert <dries@ulyssis.org> 0.8b1-1
- Initial package.
