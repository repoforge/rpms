# $Id: $

# Authority: dries
# Upstream: 

Summary: The W3C Web browser and editor
Name: amaya
Version: 8.7
Release: 1
License: W3C
Group: Applications/Internet
URL: http://www.w3.org/Amaya/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.w3.org/Amaya/Distribution/amaya-src-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake, libpng-devel, libjpeg-devel
BuildRequires: desktop-file-utils, gcc-c++, ncurses-devel, flex
BuildRequires: zlib-devel, gtk+-devel

%description
Amaya is a Web editor, i.e. a tool used to create and update documents
directly on the Web. Browsing features are seamlessly integrated with the
editing and remote access features in a uniform environment. This follows
the original vision of the Web as a space for collaboration and not just a
one-way publishing medium.

%prep
%setup -n Amaya

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Amaya
Comment=Web browser and editor
Exec=amaya
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
%{__mkdir} linux
cd linux
../configure --prefix=%{_libdir} --exec-prefix=%{_usr}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir}
%{__install} -d %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}
cd linux
%makeinstall prefix=%{buildroot}%{_libdir} exec_prefix=%{buildroot}%{_usr}
%{__rm} -f %{buildroot}%{_bindir}/amaya*
%{__ln_s} %{_bindir}/amaya-gtk %{buildroot}%{_bindir}/amaya
%{__ln_s} %{_libdir}/Amaya/gtk/bin/amaya %{buildroot}%{_bindir}/amaya-gtk
cd ..
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* 
%{_bindir}/amaya*
%{_libdir}/Amaya
%{_datadir}/applications/*.desktop

%changelog
* Wed Jan 05 2005 Dries Verachtert <dries@ulyssis.org> - 8.7-1
- Initial package.

