# $Id$
# Authority: dag
# Upstream: 

Summary: System sampling profiler
Name: sysprof
Version: 0.02
Release: 1
License: GPL
Group: Development/System
URL: http://cvs.gnome.org/viewcvs/sysprof/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.daimi.au.dk/~sandmann/sysprof-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: pkgconfig, gtk2-devel, libglade2-devel

%description
Sysprof is a sampling profiler that uses a kernel module, sysprof-module,
to generate stacktraces which are then interpreted by the userspace
program "sysprof".

%prep
%setup -n %{name}

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
* Mon May 24 2004 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
