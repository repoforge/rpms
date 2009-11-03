# $Id$
# Authority: dries
# Upstream: Roderick Colenbrander <thunderbir2k$gmx,net>

%define real_version 0.8b

Summary: Change settings of a Nvidia card
Name: nvclock
Version: 0.8
Release: 0.b.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.linuxhardware.org/nvclock/

Source: http://www.linuxhardware.org/nvclock/nvclock%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gtk2-devel

%description
Nvclock allows you to tweak your Nvidia card under Linux and FreeBSD.
It features overclocking, hardware monitoring, tweaking of OpenGL
settings, and much more.

Use this program at your own risk!

%prep
%setup -n nvclock%{real_version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=nvclock
Comment=Change Nvidia settings
Exec=nvclock_qt
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%{__rm} -Rf %{buildroot}%{_datadir}/doc/nvclock

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/nvclock
%{_bindir}/nvclock_qt
%{_bindir}/nvclock_gtk
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-0.b.2
- Rebuild for Fedora Core 5.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-0.b
- Initial package.
