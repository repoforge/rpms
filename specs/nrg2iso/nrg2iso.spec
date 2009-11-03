# $Id$
# Authority: matthias

Summary: NRG to ISO 9660 CD image file converter
Name: nrg2iso
Version: 0.4
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://gregory.kokanosky.free.fr/v4/linux/nrg2iso.en.html
Source: http://gregory.kokanosky.free.fr/v4/linux/%{name}-%{version}.tar.gz
Patch0: nrg2iso-0.4-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Converts Images created by Nero Burning Rom to standard .iso (ISO9660) Files. 


%prep
%setup
%patch0 -p0 -b .makefile


%build
%{__make} %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} PREFIX=%{buildroot}%{_prefix} install


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGELOG gpl.txt
%{_bindir}/nrg2iso


%changelog
* Sun Oct 29 2006 Matthias Saou <http://freshrpms.net/> 0.4-1
- Initial RPM release.

