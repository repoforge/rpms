# $Id$
# Authority: dag
# Upstream: Yusuke Shinyama

Summary: Recording tool for VNC
Name: vnc2swf
Version: 0.4.1
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://www.unixuser.org/~euske/vnc2swf/

Source: http://www.unixuser.org/~euske/vnc2swf/vnc2swf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386
BuildRequires: ming-devel, libdnet-devel, XFree86-devel, libstdc++-devel, zlib-devel

%description
vnc2swf is a recoding tool for Flash.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* *.html
%{_bindir}/vnc2swf

%changelog
* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)

