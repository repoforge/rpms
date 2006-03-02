# $Id$
# Authority: dries
# Upstream: Henrik Sandklef

Summary: Record, distribute and replay X protocol data
Name: xnee
Version: 2.04
Release: 1
License: GPL
Group: User Interface/X
URL: http://www.gnu.org/software/xnee/

Source: ftp://ftp.gnu.org/gnu/xnee/Xnee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, desktop-file-utils

%description
Xnee can record, distribute, and replay X (X11) protocol data. This is 
useful for automated tests of applications or benchmarking of applications. 
Think of it as a robot.

%prep
%setup -n Xnee-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=xnee
Comment=Record, distribute and replay X protocol data
Exec=gnee
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
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README TODO
%{_bindir}/cnee
%{_bindir}/gnee
%{_libdir}/libxnee*
%{_datadir}/Xnee/
%{_datadir}/applications/*.desktop

%changelog
* Tue Feb 28 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
