# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Automatic clipboard buffers synchronization tool
Name: autocutsel
Version: 0.9.0
Release: 1
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/autocutsel/

Source: http://savannah.nongnu.org/download/autocutsel/autocutsel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libX11-devel, libXaw-devel, libXext-devel, libXt-devel}
%{!?_without_modxorg:BuildRequires: libICE-devel, libSM-devel, libXmu}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Autocutsel tracks changes in the server's cutbuffer and CLIPBOARD selection.
When the CLIPBOARD is changed, it updates the cutbuffer. When the cutbuffer
is changed, it owns the CLIPBOARD selection. The cutbuffer and CLIPBOARD
selection are always synchronized.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/autocutsel
%{_bindir}/cutsel

%changelog
* Fri Feb 01 2008 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
