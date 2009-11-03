# $Id$
# Authority: dries
# Upstream: Edwin Groothuis <edwin$mavetju,org>

Summary: Parse tcpdump DHCP packets
Name: dhcpdump
Version: 1.7
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sourceforge.net/projects/mavetju/

Source: http://www.mavetju.org/download/dhcpdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
dhcpdump is a tool to post-process tcpdump output in order analyse
sniffed DHCP packets.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTACT LICENSE
%doc %{_mandir}/man1/dhcpdump.1*
%{_bindir}/dhcpdump

%changelog
* Fri Jan 27 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Wed May 26 2004 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
