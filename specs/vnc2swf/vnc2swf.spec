# $Id$
# Authority: dag
# Upstream: <vnc2swf-users$lists,sourceforge,net>

Summary: Recording tool for VNC
Name: vnc2swf
Version: 0.4.2
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://www.unixuser.org/~euske/vnc2swf/

Source: http://www.unixuser.org/~euske/vnc2swf/vnc2swf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ming-devel, libdnet, XFree86-devel, libstdc++-devel, zlib-devel

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
%doc LICENCE.TXT README* *.html
#%doc docs/
%{_bindir}/recordwin
%{_bindir}/vnc2swf

%changelog
* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Build against newer ming.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Updated to release 0.4.2.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)
