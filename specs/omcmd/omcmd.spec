# $Id: $

# Authority: dries
# Upstream: "David L. Parsley" <parsley$linuxjedi,org>

Summary: DHCP query tool
Name: omcmd
Version: 0.4.3
Release: 1
License: GPL
Group: Applications/Internet
URL: ftp://dist.taolinux.org/pub/projects/omcmd

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://dist.taolinux.org/pub/projects/omcmd/omcmd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dhcp-devel

%description
'omcmd' is a tool for operating on a running ISC dhcp server using the
OMAPI protocol.  Functionally, it's not quite as powerful as 'omshell',
but it's easier to use in many respects (human-readable time values, for
instance), and it's designed to be easier to script.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 omcmd %{buildroot}%{_bindir}/omcmd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING README
%{_bindir}/*

%changelog
* Fri Aug 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.3-1
- Initial package.
