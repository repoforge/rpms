# $Id$
# Authority: dries
# Upstream: "David L. Parsley" <parsley$linuxjedi,org>

Summary: Dhcp/omapi tool for operating on a running dhcp server
Name: omcmd
Version: 0.4.3
Release: 1
License: GPL
Group: Applications/Internet
URL: ftp://dist.taolinux.org/pub/projects/omcmd

Source: ftp://dist.taolinux.org/pub/projects/omcmd/omcmd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dhcp-devel

%description
omcmd is a CLI utility for querying and updating omapi objects in a running
ISC dhcp server. It can be used to dynamically create/modify/remove/lookup
hosts and leases.

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
* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Added summary/description from David's package. (David L. Parsley)

* Fri Aug 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.3-1
- Initial package.
