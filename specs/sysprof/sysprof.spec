# $Id$
# Authority: dag

Summary: System sampling profiler
Name: sysprof
Version: 0.91
Release: 1.2%{?dist}
License: GPL
Group: Development/Debuggers
URL: http://cvs.gnome.org/viewcvs/sysprof/

Source: http://www.daimi.au.dk/~sandmann/sysprof/sysprof-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, gtk2-devel, libglade2-devel

%description
Sysprof is a sampling profiler that uses a kernel module, sysprof-module,
to generate stacktraces which are then interpreted by the userspace
program "sysprof".

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
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.91-1.2
- Rebuild for Fedora Core 5.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.91-1
- Update to release 0.91.

* Mon May 24 2004 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
