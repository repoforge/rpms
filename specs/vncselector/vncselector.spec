# $Id: $

# Authority: dries
# Upstream: 

Summary: Manage a list of currently active VNC server sessions
Name: vncselector
Version: 1.2
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://www.dooglio.net/VncSelector/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://www.dooglio.net/VncSelector/VncSelector_%{version}.tar.gz
BuildRequires: fltk-devel, gcc-c++, XFree86-devel
Requires: fltk

# Screenshot: http://www.dooglio.net/VncSelector/screenshot.png

%description
VncSelector allows a user to manage his/her list of currently active VNC
server sessions. This can be useful in a thin client situation (run from
.Xsession, for example). 

%prep
%{__rm} -rf %{buildroot}
%setup -n VncSelector_%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 755 VncSelector %{buildroot}%{_bindir}/VncSelector

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc RELEASE_NOTES
%{_bindir}/VncSelector

%changelog
* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- first packaging for Fedora Core 1
