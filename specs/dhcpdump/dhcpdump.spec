# $Id: $
# Authority: dries
# Upstream: Edwin Groothuis <edwin@mavetju.org>

Summary: Parse tcpdump DHCP packets
Name: dhcpdump
Version: 1.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://sf.net/projects/mavetju/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.mavetju.org/download/dhcpdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A post-processor of tcpdump output to analyze sniffed DHCP packets.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed May 26 2004 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
